### The Long Division Benchmark

#### Description

In the current landscape of scaled LLMs (Large Language Models), a significant focus has been on their ability to handle large contexts. However, an equally important aspect is their capability to generate long coherent texts. Writing a book, for instance, requires not only the ability to read long contexts but also to generate extensive text. Evaluating such an ability can be challenging, but one scalable and straightforward method is to test the LLMs' ability to perform long division. This task can be done without external tools and is easily scalable. Long division, a fundamental algorithm involving simple calculations, can be performed by humans given enough time, making it a suitable benchmark for LLMs.

#### Benchmarking Basis

Imagine a hypothetical LLM with the following two qualities:

1. It has an infinite context length.
2. It can perform long division at a high school level.

Given these qualities, it should be able to compute \( B = C / A \) to an arbitrary number of decimal places and find the exact value if \( B \) is a terminating decimal.

#### Question Creation Process

The creation process ensures long division problems with terminating decimals, having a finite number of decimal places.

1. **Generate an Integer**:
   - **Input**: Length \( n \) (number of digits)
   - **Output**: Integer \( A \)

2. **Generate a Decimal Number**:
   - **Input**: Length \( m \) (number of decimal places)
   - **Output**: Decimal number \( B \) (finite decimal)

3. **Multiply the Integer and Decimal**:
   - **Calculate**: \( C = A \times B \)
   - **Result**: Number \( C \) that, when divided by \( A \), results in \( B \), ensuring a non-repeating finite decimal.

### Long Division Benchmark Script

The script `benchmark.py` benchmarks different models by generating long division problems and evaluating the models' ability to solve them accurately. The process involves creating a division problem, posing it to the model, and then verifying the precision of the model's answer.

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
