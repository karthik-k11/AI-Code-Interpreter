import re

##Block DANGEROUS KEYWORDS
DANGEROUS_KEYWORDS = [
    "import os",
    "import sys",
    "subprocess",
    "shutil",
    "open(",
    "__import__",
    "eval(",
    "exec("
]


def extract_python_code(text: str) -> str:

    ##Case 1: ```python blocks
    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)

    if matches:
        return matches[0].strip()

    ##Case 2: ``` generic blocks
    pattern_generic = r"```(.*?)```"
    matches = re.findall(pattern_generic, text, re.DOTALL)

    if matches:
        return matches[0].strip()

    ##Case 3: Plain code (no markdown)
    return text.strip()


def is_code_safe(code: str) -> bool:
    for keyword in DANGEROUS_KEYWORDS:
        if keyword in code:
            return False
    return True