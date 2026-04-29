from llm import get_llm_response


def main():
    print("=== AI Code Interpreter (Day 1 - HuggingFace) ===")

    while True:
        user_input = input("\nEnter your request (or type 'exit'): ")

        if user_input.lower() == "exit":
            break

        response = get_llm_response(user_input)

        print("\n--- LLM Response ---")
        print(response)


if __name__ == "__main__":
    main()