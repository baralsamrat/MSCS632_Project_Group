import re
import matplotlib.pyplot as plt
import numpy as np

def count_python_metrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    total_lines = len(lines)
    # Count non-empty and non-comment lines as code lines
    code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith("#"))
    # Naively count function definitions (lines starting with "def ")
    function_count = sum(1 for line in lines if re.match(r'\s*def ', line))
    return total_lines, code_lines, function_count

def count_cpp_metrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    total_lines = len(lines)
    # Count non-empty and non-comment lines as code lines (assuming '//' comments)
    code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith("//"))
    # Naively count function definitions by looking for lines that likely start a function declaration
    function_count = sum(1 for line in lines if re.search(r'\w+\s+\w+\s*\(', line))
    return total_lines, code_lines, function_count

# Compute metrics for the C++ and Python files
cpp_total, cpp_code, cpp_functions = count_cpp_metrics("expense_tracker.cpp")
py_total, py_code, py_functions = count_python_metrics("expense_tracker.py")

# Prepare data for plotting
languages = ["C++", "Python"]
loc = [cpp_total, py_total]          # Total lines of code
func_counts = [cpp_functions, py_functions]  # Number of functions

bar_width = 0.35
index = np.arange(len(languages))

# Create bar chart
plt.bar(index, loc, bar_width, label='Total Lines')
plt.bar(index + bar_width, func_counts, bar_width, label='Function Count')

plt.xlabel('Language')
plt.ylabel('Count')
plt.title('Code Metrics Comparison')
plt.xticks(index + bar_width / 2, languages)
plt.legend()
plt.tight_layout()
plt.show()
