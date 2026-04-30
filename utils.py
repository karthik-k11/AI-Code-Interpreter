import re

##Block dangerous keywords
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

    pattern = r"```python(.*?)```"
    matches = re.findall(pattern, text, re.DOTALL)

    if matches:
        return matches[0].strip()  ##To take ONLY FIRST block

    pattern_generic = r"```(.*?)```"
    matches = re.findall(pattern_generic, text, re.DOTALL)

    if matches:
        return matches[0].strip()

    return "No Python code found."


def is_code_safe(code: str) -> bool:

    for keyword in DANGEROUS_KEYWORDS:
        if keyword in code:
            return False

    return True