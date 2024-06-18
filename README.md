### The Long Division Benchmark

#### Premise

Imagine a hypothetical LLM with the following two qualities:

1. It has an infinite context length.
2. It can perform long division at a high school level.

Given these qualities, it should be able to compute B = **C / A** to an arbitrary number of decimal places and find the exact value if **B** is a terminating decimal.

#### Description

In the current landscape of scaled Large Language Models (LLMs), a significant focus has been on their ability to handle large contexts. However, an equally important aspect is their capability to generate long coherent texts. Writing a book, for instance, requires not only the ability to read long contexts but also to generate extensive text. Evaluating such an ability can be challenging, but one scalable and straightforward method is to test the LLMs' ability to perform long division. This task can be done without external tools and is easily scalable. Long division, a fundamental algorithm involving simple calculations, can be performed by humans given enough time, making it a suitable benchmark for LLMs.

For example, consider the long division problem for **n=5**:
> Use long division to find the exact result of 64369.03341 ÷ 95689 to full precision. Do not use any tools or calculators. Approximate answers are not allowed.

The answer to this problem is 0.67269.

### Results

Each entry in the results table represents the percentage of correct answers for 25 samples per number of decimal places.

| Length | GPT-3.5-turbo (%) | GPT-4-turbo (%) | GPT-4o (%) |
|--------|-------------------|-----------------|------------|
| 1      | 92.00             | 96.00           | 92.00      |
| 2      | 60.00             | 72.00           | 60.00      |
| 3      | 20.00             | 56.00           | 52.00      |
| 4      | 16.00             | 28.00           | 32.00      |
| 5      | 0.00              | 4.00            | 4.00       |
| 6      | 0.00              | 0.00            | 0.00       |
| 7      | 0.00              | 0.00            | 0.00       |

Certainly! Here is the revised text with a direct markdown link to the `benchmark.py` script:

### Benchmark Script

[benchmark.py](./benchmark.py) tests different models by generating long division problems and evaluating the models' ability to solve them accurately. The process involves creating a division problem, posing it to the model, and then verifying the precision of the model's answer.

To ensure long division problems with terminating decimals, the question creation process involves three main steps. First, an integer **A** is generated based on the specified number of digits. Next, a decimal number **B** with a finite number of decimal places is generated. Finally, the integer **A** and the decimal **B** are multiplied to calculate **C**, ensuring that dividing **C** by **A** results in **B**, thereby guaranteeing a non-repeating finite decimal.

### Conclusion

This repository offers a scalable method to validate the capability of future LLMs to not only read long contexts but also to constructively use them. By leveraging long division as a benchmark, it provides a straightforward way to evaluate how well LLMs utilize long contexts meaningfully. The results show that newer models can better handle longer contexts, emphasizing the need for continuous improvement. This benchmark ensures that LLMs can perform complex tasks effectively, combining long contexts with straightforward operations to yield exact answers, thus validating their practical application of long-context understanding.
