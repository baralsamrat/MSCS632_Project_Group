#include <iostream>
#include <vector>
#include <map>
#include <memory>
#include <iomanip>
#include <sstream>

struct Expense {
    std::string date;
    double amount;
    std::string category;
    std::string description;
};

std::vector<std::unique_ptr<Expense>> expenses;

// Function to add an expense
void addExpense(const std::string& date, double amount, const std::string& category, const std::string& description) {
    expenses.push_back(std::make_unique<Expense>(Expense{date, amount, category, description}));
}

// Function to filter expenses by category
void filterExpensesByCategory(const std::string& category) {
    std::cout << "\nFiltered by Category (" << category << "):\n";
    std::cout << std::left << std::setw(12) << "Date" << std::setw(10) << "Amount" << std::setw(15) << "Category" << "Description\n";
    std::cout << "----------------------------------------------------------\n";
    
    bool found = false;
    for (const auto& exp : expenses) {
        if (exp->category == category) {
            std::cout << std::setw(12) << exp->date 
                      << "$" << std::setw(9) << exp->amount 
                      << std::setw(15) << exp->category 
                      << exp->description << "\n";
            found = true;
        }
    }
    if (!found) {
        std::cout << "No expenses found for this category.\n";
    }
}

// Function to filter expenses by date range
void filterExpensesByDate(const std::string& startDate, const std::string& endDate) {
    std::cout << "\nFiltered by Date (" << startDate << " to " << endDate << "):\n";
    std::cout << std::left << std::setw(12) << "Date" << std::setw(10) << "Amount" << std::setw(15) << "Category" << "Description\n";
    std::cout << "----------------------------------------------------------\n";
    
    bool found = false;
    for (const auto& exp : expenses) {
        if (exp->date >= startDate && exp->date <= endDate) {
            std::cout << std::setw(12) << exp->date 
                      << "$" << std::setw(9) << exp->amount 
                      << std::setw(15) << exp->category 
                      << exp->description << "\n";
            found = true;
        }
    }
    if (!found) {
        std::cout << "No expenses found in this date range.\n";
    }
}

// Function to display the summary of expenses
void showSummary() {
    std::map<std::string, double> categoryTotals;
    double totalExpense = 0.0;

    for (const auto& exp : expenses) {
        categoryTotals[exp->category] += exp->amount;
        totalExpense += exp->amount;
    }

    std::cout << "\nExpense Summary:\n";
    std::cout << "----------------------\n";
    for (const auto& pair : categoryTotals) {
        std::cout << pair.first << ": $" << std::fixed << std::setprecision(2) << pair.second << "\n";
    }
    std::cout << "Total Expenses: $" << std::fixed << std::setprecision(2) << totalExpense << "\n";
}

int main() {
    // Adding sample expenses
    addExpense("2023-10-10", 50.0, "Food", "Lunch at a restaurant");
    addExpense("2023-10-15", 30.0, "Transport", "Bus fare");
    addExpense("2023-10-20", 20.0, "Food", "Snacks");

    // Filtering expenses
    filterExpensesByCategory("Food");
    filterExpensesByDate("2023-10-10", "2023-10-15");

    // Showing summary
    showSummary();

    return 0;
}
