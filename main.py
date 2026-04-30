from llm import get_llm_response
from utils import extract_python_code, is_code_safe
from executor import execute_code


def main():
    print("=== AI Code Interpreter ===")

    while True:
        user_input = input("\nEnter your request (or type 'exit'): ")

        if user_input.lower() == "exit":
            break

        ##LLM
        response = get_llm_response(user_input)

        print("\n--- RAW LLM Response ---")
        print(response)

        ##Extract ONLY first code block
        code = extract_python_code(response)

        print("\n--- Extracted Python Code ---")
        print(code)

        ##Safety check
        if not is_code_safe(code):
            print("\n--- BLOCKED ---")
            print("Unsafe code detected. Execution stopped.")
            continue

        ##Execute
        result = execute_code(code)

        print("\n--- Execution Output ---")
        print(result)


if __name__ == "__main__":
    main()