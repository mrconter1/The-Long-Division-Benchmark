from openai import AsyncOpenAI
from fractions import Fraction
import asyncio
import random

# Set up your OpenAI API key
api_key = 'OpenAI API key'
client = AsyncOpenAI(api_key=api_key)
GPT_MODEL = "gpt-3.5-turbo"

# Global variables
evaluations_per_length = 25
max_length = 7

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

    question = f"Use long division to find the exact result of {float(C)} ÷ {A} to full precision. The answer should be in the format 'Answer: x.xxxx' where 'x.xxxx' is the result.."
    return question, round(answer, length)

async def ask_model(question):
    try:
        response = await client.chat.completions.create(
            model=GPT_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that provides exact answers to mathematical questions."},
                {"role": "user", "content": question}
            ],
            temperature=0.5
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        print(f"Error during API call: {e}")
        return None

async def benchmark_model(evaluations_per_length, max_length):
    results = {}

    print(f"Model chosen: {GPT_MODEL}")
    print(f"Number of evaluations for each length: {evaluations_per_length}")
    print("-"*50)
    print("Evaluation starts now:\n")

    for length in range(1, max_length + 1):
        print(f"Evaluating model for length: {length}")
        print("-"*40)
        correct = 0

        tasks = []
        for _ in range(evaluations_per_length):
            question, correct_answer = generate_long_division_question(length)
            tasks.append((question, correct_answer))

        responses = await asyncio.gather(*[ask_model(q) for q, _ in tasks])

        for (question, correct_answer), model_answer in zip(tasks, responses):
            question_str = question.split("of ")[-1].split(" to")[0]
            print(f"Problem: {question_str}")
            print(f"Expected Answer: {correct_answer}")

            if model_answer:
                try:
                    parsed_answer = float(model_answer.split('Answer: ')[-1])
                    print(f"Given Answer: {parsed_answer}")
                    if parsed_answer == correct_answer:
                        correct += 1
                        print("Result: Correct\n")
                    else:
                        print("Result: Incorrect\n")
                except ValueError:
                    print("Result: Error in parsing model answer\n")
            else:
                print("Result: No response from model\n")

        success_rate = (correct / evaluations_per_length) * 100
        results[length] = success_rate
        print(f"Success Rate for length {length}: {success_rate:.2f}%")
        print("-"*40)
        print()

    return results

if __name__ == "__main__":
    try:
        results = asyncio.run(benchmark_model(evaluations_per_length, max_length))
        print("\nFinal Results:")
        print("| Length | Success Rate (%) |")
        print("|--------|------------------|")
        for length, success_rate in results.items():
            print(f"| {length}      | {success_rate:.2f}             |")
    except Exception as e:
        print()
