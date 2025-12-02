# holier-than-prompt
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/loveteshchandra/con-sentry.git
   cd con-sentry
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project is organized as follows:

- **`main.py`**: The entry point of the application. Orchestrates the setup, evaluation, and red teaming demo.
- **`src/`**: Contains the core logic of the Constitutional AI system.
  - **`constitution.py`**: Defines the `Constitution` and `SimpleRetriever` for managing and retrieving principles.
  - **`judge.py`**: Implements the `ConstitutionalJudge` which evaluates interactions against the constitution.
  - **`metrics.py`**: Contains functions for calculating compliance scores (e.g., `calculate_compliance_score`).
  - **`red_team.py`**: Implements the `RedTeamer` for generating adversarial prompts.
  - **`schema.py`**: Defines Pydantic models for data structures like `EvaluationTrace` and `Verdict`.
- **`tests/`**: Contains unit tests for the system.
  - **`test_compliance.py`**: Tests for compliance evaluation and scoring.

## Usage

Run the main application to see the Constitutional AI system in action:

```bash
python3 main.py
```

This will:
1. Initialize the Constitution and Judge.
2. Evaluate a set of predefined interactions.
3. Calculate the Constitutional Compliance Score (CCS).
4. Run a demonstration of automated Red Teaming.

## Running Tests

To run the test suite:

```bash
python3 -m pytest
```
