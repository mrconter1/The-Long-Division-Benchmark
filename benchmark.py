from fractions import Fraction
import random
import asyncio
import re

# List of models to benchmark
models_to_benchmark = [
    {"provider": "openai", "name": "gpt-3.5-turbo"},
    {"provider": "openai", "name": "gpt-4-turbo"},
    {"provider": "openai", "name": "gpt-4o"},
    {"provider": "google", "name": "gemini-1.5-pro"}
]

# Global variables
evaluations_per_length = 2
max_length = 5
openai_api_key = 'YOUR_KEY'
google_api_key = 'YOUR_KEY'

# OpenAI setup
from openai import AsyncOpenAI
openai_client = AsyncOpenAI(api_key=openai_api_key)

# Google setup
import google.generativeai as genai
genai.configure(api_key=google_api_key)

def generate_long_division_question(length):
    while True:
        A = random.randint(10**(length-1), 10**length - 1)
        numerator = random.randint(1, 10**length - 1)
        B = Fraction(numerator, 10**length)
        C = A * B
        answer = float(C) / A
        answer_str = str(answer).split('.')[-1]
        
        if len(answer_str) <= length:
            break

    question = f"""Use long division to find the exact result of {float(C)} ÷ {A} to full precision. 
        Do not use any tools or calculators. Approximate answers are not allowed. 

        The answer should be in the format 'Answer: x.xxxx' where 'x.xxxx' is the result. 
        Please make sure your answer strictly follows this format. 

        Examples:
        If the result is 3.1415, write 'Answer: 3.1415'
        If the result is 2.7182, write 'Answer: 2.7182'
        """

    return question, round(answer, length)

async def ask_model(question, model):
    try:
        if model["provider"] == "openai":
            response = await openai_client.chat.completions.create(
                model=model["name"],
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": question}
                ],
                temperature=0.5
            )
            answer = response.choices[0].message.content.strip()
        elif model["provider"] == "google":
            google_model = genai.GenerativeModel(model["name"])
            response = google_model.generate_content(question)
            answer = response.text.strip()
        return answer
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

async def benchmark_model(model, evaluations_per_length, max_length):
    results = {}
    print(f"Evaluating model: {model['name']}")

    for length in range(1, max_length + 1):
        correct = 0
        tasks = []

        for _ in range(evaluations_per_length):
            question, correct_answer = generate_long_division_question(length)
            tasks.append((question, correct_answer))

        responses = await asyncio.gather(*[ask_model(q, model) for q, _ in tasks])

        for (question, correct_answer), model_answer in zip(tasks, responses):
            question_str = question.split("of ")[-1].split(" to")[0]
            print(f"Problem: {question_str}")
            print(f"Expected Answer: {correct_answer}")

            if model_answer:
                try:
                    # Use regex to find the answer in the model's response
                    answer_match = re.search(r'Answer:\s*([-+]?\d*\.?\d+|\d+)', model_answer)
                    if answer_match:
                        parsed_answer = float(answer_match.group(1))
                        print(f"Given Answer: {parsed_answer}")
                        if parsed_answer == correct_answer:
                            correct += 1
                            print("Result: Correct\n")
                        else:
                            print("Result: Incorrect\n")
                    else:
                        print("Result: No valid answer found\n")
                        print(model_answer)
                except ValueError:
                    print("Result: Error in parsing model answer\n")
                    print(model_answer)
            else:
                print("Result: No response from model\n")

        success_rate = (correct / evaluations_per_length) * 100
        results[length] = success_rate
        print(f"Success Rate for length {length}: {success_rate:.2f}%\n")

    return model["name"], results


async def main():
    all_results = {}
    for model in models_to_benchmark:
        model_name, results = await benchmark_model(model, evaluations_per_length, max_length)
        all_results[model_name] = results

    # Generating the final results table
    print("\nFinal Results:")
    lengths = list(range(1, max_length + 1))
    headers = ["Length"] + [model["name"] for model in models_to_benchmark]
    table = []

    for length in lengths:
        row = [length]
        for model in models_to_benchmark:
            model_name = model["name"]
            row.append(f"{all_results[model_name][length]:.2f}")
        table.append(row)

    # Print the table
    print("| " + " | ".join(headers) + " |")
    print("| " + " | ".join(["--------"] * len(headers)) + " |")
    for row in table:
        print("| " + " | ".join(map(str, row)) + " |")

if __name__ == "__main__":
    asyncio.run(main())