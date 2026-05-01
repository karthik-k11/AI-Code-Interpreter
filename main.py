from llm import get_llm_response
from utils import extract_python_code, is_code_safe
from executor import execute_code


def main():
    print("=== AI Code Interpreter ===")

    while True:
        user_input = input("\nEnter your request (or type 'exit'): ")

        if user_input.lower() == "exit":
            break

        file_path = input("Enter file path (or press Enter to skip): ").strip()

        if file_path == "":
            file_path = None

        ##LLM
        response = get_llm_response(user_input, file_path)

        print("\n--- RAW LLM Response ---")
        print(response)

        ##Extract
        code = extract_python_code(response)

        print("\n--- Extracted Python Code ---")
        print(code)

        ##Safety
        if not is_code_safe(code):
            print("\n--- BLOCKED ---")
            print("Unsafe code detected.")
            continue

        ##Execute
        result = execute_code(code)

        print("\n=== RESULT ===")
        print(result)


if __name__ == "__main__":
    main()