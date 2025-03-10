# 🚀 YeetCode  

**YeetCode** is a CLI tool designed for developers to easily pull LeetCode problems into their local environment, generate AI-powered test cases, and run solutions—all without leaving their setup.  

## ⚡ Features  
- Fetch LeetCode problems directly into your workspace  
- Dynamically generate high-quality test cases using AI  
- Run and validate your solutions locally  

## 🛠 Installation & Usage  

You'll need Python 3.8+ and AWS CLI configured. Install YeetCode with:  

```bash
# Install YeetCode
pip install yeetcode

# Listing all problems
yeetcode list

# Pulling Problems
yeetcode pull <problem_id>

# Testing Solutions
yeetcode test # From inside the problem directory
```

## 💡 What YeetCode Does  

1. Fetches problem data from LeetCode.  
2. Generates high-quality test cases on demand using AI.  
3. Runs tests locally using Python’s unittest or pytest framework.  
4. Caches results to minimize redundant API calls.

**Note:** The backend components are abstracted away. You don’t need to worry about them—just focus on solving problems!

## 📚 Sample Applications

### Hello World in Go

1. Navigate to the `samples` directory.
2. Run the following command in your terminal:

```bash
go run hello_world.go
```

This will compile and execute the Go program, printing "Hello, World!" to the console.

Just a generated go app, whatever, who cares. I think I'm going to rewrite this project in Go.
