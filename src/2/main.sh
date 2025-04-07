#!/bin/bash
# main.sh
# This script compiles and runs the C++ Expense Tracker using C++14,
# then sets up a Python virtual environment, installs required libraries,
# and finally runs the Python Expense Tracker along with optional metrics and visualization scripts.

# Define file names and variables
CPP_SOURCE="expense_tracker.cpp"
CPP_BINARY="expense_tracker_cpp"
PYTHON_SOURCE="expense_tracker.py"
METRICS_SCRIPT="metrics.py"         # Optional metrics analysis script
VISUALIZE_SCRIPT="visualize.py"     # Optional visualization script
REQUIREMENTS_FILE="requirements.txt"
VENV_DIR="venv"

# ---------------------------
# Compile and Run C++ Program
# ---------------------------
# Check for a C++ compiler (g++ or clang++)
if command -v g++ >/dev/null 2>&1; then
    COMPILER="g++"
elif command -v clang++ >/dev/null 2>&1; then
    COMPILER="clang++"
else
    echo "No C++ compiler found. Please install g++ or clang++."
    exit 1
fi

echo "Compiling ${CPP_SOURCE} using ${COMPILER} with C++14 standard..."
$COMPILER -std=c++14 -o $CPP_BINARY $CPP_SOURCE
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 1
fi

echo "Running C++ Expense Tracker:"
./$CPP_BINARY
echo ""

# ---------------------------
# Set Up Python Environment
# ---------------------------
# Check for a Python3 interpreter
if command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
else
    echo "Python3 is not installed."
    exit 1
fi

# Create a virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating Python virtual environment..."
    $PYTHON_CMD -m venv $VENV_DIR
fi

# Activate the virtual environment
source $VENV_DIR/bin/activate

# Install required Python libraries from requirements.txt
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing required Python packages from ${REQUIREMENTS_FILE}..."
    pip install -r $REQUIREMENTS_FILE
else
    echo "No requirements.txt found. Installing default packages (matplotlib and numpy)..."
    pip install matplotlib numpy
fi

# ---------------------------
# Run Python Programs
# ---------------------------
echo "Running Python Expense Tracker:"
$PYTHON_CMD $PYTHON_SOURCE
echo ""

if [ -f "$METRICS_SCRIPT" ]; then
    echo "Running metrics analysis script:"
    $PYTHON_CMD $METRICS_SCRIPT
else
    echo "Metrics script (${METRICS_SCRIPT}) not found. Skipping metrics analysis."
fi

echo ""

if [ -f "$VISUALIZE_SCRIPT" ]; then
    echo "Running visualization script:"
    $PYTHON_CMD $VISUALIZE_SCRIPT
else
    echo "Visualization script (${VISUALIZE_SCRIPT}) not found. Skipping visualization."
fi

# Deactivate the virtual environment
deactivate

echo "All tasks completed."
