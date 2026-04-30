import sys
import io
import contextlib


def execute_code(code: str) -> str:

    ##Capture stdout
    output = io.StringIO()

    try:
        with contextlib.redirect_stdout(output):
            exec(code, {})  ##empty global scope

        return output.getvalue() if output.getvalue() else "Code executed successfully (no output)"

    except Exception as e:
        return f"Execution Error: {str(e)}"