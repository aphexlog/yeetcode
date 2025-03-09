# 🚀 YeetCode  

**YeetCode** is a CLI tool designed for developers to easily pull LeetCode problems into their local environment, generate AI-powered test cases, and run solutions—all without leaving their setup.  

## ⚡ Features  
- Fetch LeetCode problems directly into your workspace  
- Dynamically generate test cases using AI  
- Run and validate your solutions locally  
- Optimized for AWS, keeping costs minimal  
- No passive costs—compute only when needed  

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
2. Generates test cases on demand.  
3. Runs tests locally using Python’s unittest or pytest framework.  
4. Caches results to minimize redundant API calls.

**Note:** The backend components like AWS Lambda, Bedrock/SageMaker, DynamoDB/S3 are abstracted away. You don’t need to worry about them—just focus on solving problems!
