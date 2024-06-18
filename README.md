# The Long Division Benchmark

## Description

In an age of scaled LLMs (Large Language Models), one focus that is getting increased attention is the ability for LLMs to handle large contexts. However, another aspect that arguably has not been explored much is the ability to generate long coherent texts. Writing a book, for instance, requires not only the ability to read long contexts but also the ability to generate long texts. So how would you go about benchmarking this? Generating a book can be challenging to classify as good or bad.

Another potential way that doesn’t require external tools and is scalable is to ask the LLM to simply perform long division. The advantage of this method is that it can be easily scaled and does not necessarily require humans to use a calculator, though the calculation might take longer. Fundamentally, the algorithm of long division consists of simple calculations. In theory, a human can perform a division resulting in many decimals given enough time. This provides a simple yet effective way to benchmark LLMs against tasks that humans can do, simultaneously testing their ability to use long context in a concrete fashion.

## Benchmarking Basis

If we assume:
- The LLM has an infinite context length.
- The LLM can perform long division at the level of a high school student.

Then the following should be true:
- The LLM should be able to compute \( B = C / A \) to an arbitrary number of decimal places accurately using long division.

## Question Creation Process

This process ensures the creation of long division problems with terminating decimals, which have a finite number of decimal places.

1. **Generate an Integer**:
   - **Input**: Length \( n \) (number of digits)
   - **Output**: Integer \( A \)

2. **Generate a Decimal Number**:
   - **Input**: Length \( m \) (number of decimal places)
   - **Output**: Decimal number \( B \) (finite decimal)

3. **Multiply the Integer and Decimal**:
   - **Calculate**: \( C = A \times B \)
   - **Result**: Number \( C \) that, when divided by \( A \), results in \( B \), ensuring a non-repeating finite decimal.

## Long Division Question Creation

1. **Question Format**:
   - Divide \( C \) by \( A \) using long division.

## Python Function to Generate the Question

```python
import random
from fractions import Fraction

def generate_long_division_question(length):
    while True:
        # Generate a random integer of specified length
        A = random.randint(10**(length-1), 10**length - 1)
        
        # Generate a random integer of specified length for the numerator
        numerator = random.randint(1, 10**length - 1)
        
        # Ensure B is a terminating decimal by dividing the numerator by 10^length
        B = Fraction(numerator, 10**length)
        
        # Calculate the product C to ensure it can be divided by A to give B exactly
        C = A * B
        
        # Calculate the answer
        answer = float(C) / A
        
        # Convert the answer to a string to check its length after the decimal point
        answer_str = str(answer).split('.')[-1]
        
        if len(answer_str) <= length:
            break

    # Format the question concisely with emphasis
    question = f"Use long division to find the exact result of {float(C)} ÷ {A} to full precision. Do not use any tools or calculators. Approximate answers are not allowed."
    
    return question, answer

# Example usage: Print five questions with n=5
for _ in range(5):
    question, answer = generate_long_division_question(4)
    print(question)
    print(f"Answer: {answer}")
    print()
    
'''Output
Use long division to find the exact result of 4159.6196 ÷ 8573 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.
Answer: 0.4852

Use long division to find the exact result of 838.8372 ÷ 1284 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.
Answer: 0.6533

Use long division to find the exact result of 4593.402 ÷ 8140 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.
Answer: 0.5643

Use long division to find the exact result of 8026.7451 ÷ 8459 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.
Answer: 0.9489

Use long division to find the exact result of 5861.025 ÷ 8550 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.
Answer: 0.6855
'''
```

This function generates a long division question that ensures the result is a terminating decimal. Adjust the `integer_length` and `decimal_length` parameters to scale the complexity of the question.
