import re


def extract_python_code(text: str) -> str:

    ##Pattern to match ```python ... ```
    pattern = r"```python(.*?)```"

    matches = re.findall(pattern, text, re.DOTALL)

    if matches:
        ##Join all code blocks if multiple exist
        return "\n\n".join(match.strip() for match in matches)

    ##Fallback: try generic ```
    pattern_generic = r"```(.*?)```"
    matches = re.findall(pattern_generic, text, re.DOTALL)

    if matches:
        return "\n\n".join(match.strip() for match in matches)

    return "No Python code found."