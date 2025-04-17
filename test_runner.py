from typing import List, Optional
import inspect
import sys
import os
import ast
import importlib.util
import argparse

# Add workspace root to Python path
workspace_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(workspace_root)

class TestRunner:
    def __init__(self, selected_people=None):
        self.solutions = {}
        self._load_solutions(selected_people)

    def _load_function_from_file(self, file_path, func_name):
        """Load a function's source code directly from file to check implementation"""
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef) and node.name == func_name:
                        # Check if function has actual implementation
                        body = node.body
                        if len(body) == 1 and isinstance(body[0], ast.Pass):
                            return None
                        # Check for actual code beyond pass and docstrings
                        has_code = any(
                            not isinstance(stmt, (ast.Pass, ast.Expr)) or 
                            (isinstance(stmt, ast.Expr) and not isinstance(stmt.value, ast.Str))
                            for stmt in body
                        )
                        if has_code:
                            # Import and return the actual function
                            spec = importlib.util.spec_from_file_location(
                                f"solutions.{func_name}", 
                                file_path
                            )
                            module = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(module)
                            return getattr(module, func_name)
                        return None
        except Exception as e:
            print(f"Error loading function {func_name} from {file_path}: {e}")
            return None
        return None

    def _load_solution_module(self, person):
        """Load a person's solutions directly from their solution files"""
        solutions_dir = os.path.join(workspace_root, person, 'solutions')
        
        # Create a Solution class for this person's implementations
        solution_dict = {}
        
        # Check and load individual solutions
        solution_files = {
            'hasDuplicate': os.path.join(solutions_dir, 'has_duplicate.py'),
            'isAnagram': os.path.join(solutions_dir, 'is_anagram.py')
        }
        
        for func_name, file_path in solution_files.items():
            if os.path.exists(file_path):
                func = self._load_function_from_file(file_path, func_name)
                if func:
                    solution_dict[func_name] = func
        
        if solution_dict:
            return type('Solution', (), solution_dict)()
        return None

    def _load_solutions(self, selected_people=None):
        # Import all available solutions
        all_people = ['Kazim', 'Jawad', 'Jafer', 'Ilyas', 'Bilal']
        people_to_load = selected_people if selected_people else all_people
        
        # Validate selected people
        invalid_people = [p for p in people_to_load if p not in all_people]
        if invalid_people:
            print(f"Warning: Invalid people selected: {', '.join(invalid_people)}")
            people_to_load = [p for p in people_to_load if p in all_people]
        
        if not people_to_load:
            print("No valid people selected to test!")
            sys.exit(1)
            
        for person in people_to_load:
            try:
                solution = self._load_solution_module(person)
                if solution:
                    self.solutions[person] = solution
            except Exception as e:
                print(f"Failed to load {person}'s solutions: {e}")

    def _is_implemented(self, func):
        if func is None:
            return False
        try:
            source = inspect.getsource(func)
            return 'pass' not in source.strip().split('\n')[-1]
        except:
            return False

    def test_has_duplicate(self):
        print("\nTesting hasDuplicate function:")
        test_cases = [
            ([1, 2, 3, 1], True),
            ([1, 2, 3, 4], False),
            ([], False),
            ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True)
        ]
        
        implemented = False
        for name, solution in self.solutions.items():
            if hasattr(solution, 'hasDuplicate') and self._is_implemented(solution.hasDuplicate):
                implemented = True
                print(f"\n{name}'s implementation:")
                for nums, expected in test_cases:
                    result = solution.hasDuplicate(nums)
                    print(f"Input: {nums}")
                    print(f"Expected: {expected}, Got: {result}")
                    print(f"{'✓ PASS' if result == expected else '✗ FAIL'}")
        
        if not implemented:
            print("No implementations found yet!")

    def test_is_anagram(self):
        print("\nTesting isAnagram function:")
        test_cases = [
            (("anagram", "nagaram"), True),
            (("rat", "car"), False),
            (("", ""), True),
            (("aacc", "ccac"), False)
        ]
        
        implemented = False
        for name, solution in self.solutions.items():
            if hasattr(solution, 'isAnagram') and self._is_implemented(solution.isAnagram):
                implemented = True
                print(f"\n{name}'s implementation:")
                for (s, t), expected in test_cases:
                    result = solution.isAnagram(s, t)
                    print(f"Input: s = '{s}', t = '{t}'")
                    print(f"Expected: {expected}, Got: {result}")
                    print(f"{'✓ PASS' if result == expected else '✗ FAIL'}")
        
        if not implemented:
            print("No implementations found yet!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run coding problem solutions')
    parser.add_argument('-p', '--people', nargs='+', help='Select specific people whose solutions to test')
    parser.add_argument('--list', action='store_true', help='List all available people')
    args = parser.parse_args()

    if args.list:
        print("\nAvailable people:")
        for person in ['Kazim', 'Jawad', 'Jafer', 'Ilyas', 'Bilal']:
            print(f"- {person}")
        sys.exit(0)

    runner = TestRunner(args.people)
    runner.test_has_duplicate()
    runner.test_is_anagram()