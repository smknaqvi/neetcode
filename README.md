# Coding Problems Test Runner

A collaborative coding practice environment where multiple developers can implement solutions to coding problems. Each person's solutions are kept in their own directory and can be tested individually or together using the test runner.

## Project Structure

```
.
├── test_runner.py          # Main test runner script
└── [Person]/              # Individual solution directories
    └── solutions/         
        └── *.py           # Python solution files
```

## Using the Test Runner

The test runner provides flexible ways to run and verify solutions:

1. Test all implementations:
```
python test_runner.py
```

2. Test specific people's solutions:
```
python test_runner.py -p PersonName1 PersonName2
```

3. List all available people:
```
python test_runner.py --list
```

## Adding Your Solutions

1. Create a new directory with your name if it doesn't exist
2. Add your solution files under your `solutions` directory
3. Run the test runner to verify your implementation

## Adding New Problems

To add a new coding problem to the test suite:

1. Add a new test method in `test_runner.py`:
```python
def test_new_problem(self):
    print("\nTesting newProblem function:")
    test_cases = [
        (inputs, expected_output),  # Add your test cases here
        # More test cases...
    ]
    
    implemented = False
    for name, solution in self.solutions.items():
        if hasattr(solution, 'newProblem') and self._is_implemented(solution.newProblem):
            implemented = True
            print(f"\n{name}'s implementation:")
            for test_input, expected in test_cases:
                result = solution.newProblem(*test_input)
                print(f"Input: {test_input}")
                print(f"Expected: {expected}, Got: {result}")
                print(f"{'✓ PASS' if result == expected else '✗ FAIL'}")
    
    if not implemented:
        print("No implementations found yet!")
```

2. Update the solution files mapping in `_load_solution_module()`:
```python
solution_files = {
    'existingProblem': os.path.join(solutions_dir, 'existing_problem.py'),
    'newProblem': os.path.join(solutions_dir, 'new_problem.py'),  # Add new mapping
}
```

3. Add the test call in `__main__`:
```python
runner = TestRunner(args.people)
runner.test_existing_problem()
runner.test_new_problem()  # Add new test call
```

4. Create template solution files for each person:
   - Create `new_problem.py` in each person's `solutions` directory
   - Include function signature and docstring
   - Add basic test cases in `if __name__ == "__main__"` block

## Requirements

- Python 3.x
- No additional packages required