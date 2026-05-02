# AI Code Interpreter

A mini AI-powered code interpreter that converts natural language into Python code, executes it safely, and returns results.

---

## Features

- Natural language → Python code (LLM-powered)
- Code extraction from messy responses
- Safe execution engine
- Security filtering (blocks dangerous code)
- File support (CSV analysis using pandas)
- Clean and minimal output

## Architecture

User Input → LLM → Code Extraction → Safety Check → Execution → Output

---

## Tech Stack

- Python
- Groq API (LLaMA 3.1)
- Pandas
- dotenv

---

## Setup Instructions

### 1. Clone repo

```bash
git clone https://github.com/your-username/ai-code-interpreter.git
cd ai-code-interpreter
```