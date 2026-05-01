import io
import contextlib


def execute_code(code: str, file_path: str = None) -> str:
    """
    Executes Python code with clean output formatting
    """

    output = io.StringIO()
    exec_globals = {}

    if file_path:
        exec_globals["file_path"] = file_path

    try:
        with contextlib.redirect_stdout(output):
            exec(code, exec_globals)

        result = output.getvalue().strip()

        if not result:
            return "Code executed successfully (no output)"

        return result

    except Exception as e:
        return f"Execution Error: {str(e)}"