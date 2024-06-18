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
- 
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

def generate_long_division_question(integer_length, decimal_length):
    # Generate a random integer of specified length
    A = random.randint(10**(integer_length-1), 10**integer_length - 1)
    
    # Generate a random decimal of specified length
    decimal_part = random.randint(1, 10**decimal_length - 1)
    B = decimal_part / (10 ** decimal_length)
    
    # Calculate the product to ensure a terminating decimal
    C = A * B
    
    # Format the question
    question = f"Divide {C} by {A} using long division."
    
    return question
```

This function generates a long division question that ensures the result is a terminating decimal. Adjust the `integer_length` and `decimal_length` parameters to scale the complexity of the question.
