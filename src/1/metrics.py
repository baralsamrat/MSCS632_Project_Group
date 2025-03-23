import re

def count_python_metrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    total_lines = len(lines)
    # Ignore blank lines and lines starting with a comment (#)
    code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith("#"))
    # Count function definitions (naively looking for 'def ')
    function_count = sum(1 for line in lines if re.match(r'\s*def ', line))
    return total_lines, code_lines, function_count

def count_cpp_metrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    total_lines = len(lines)
    # Ignore blank lines and lines with only comments (naively using // as a comment marker)
    code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith("//"))
    # Count function definitions (a simple heuristic looking for a return type and a parenthesis)
    function_count = sum(1 for line in lines if re.search(r'\w+\s+\w+\s*\(', line))
    return total_lines, code_lines, function_count

if __name__ == "__main__":
    cpp_file = "expense_tracker.cpp"
    python_file = "expense_tracker.py"

    cpp_total, cpp_code, cpp_functions = count_cpp_metrics(cpp_file)
    py_total, py_code, py_functions = count_python_metrics(python_file)

    print("C++ Metrics:")
    print(f"  Total lines: {cpp_total}")
    print(f"  Code lines: {cpp_code}")
    print(f"  Function definitions: {cpp_functions}\n")

    print("Python Metrics:")
    print(f"  Total lines: {py_total}")
    print(f"  Code lines: {py_code}")
    print(f"  Function definitions: {py_functions}")
