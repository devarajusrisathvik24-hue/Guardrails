
import re

PYTHON_TERMS = {
    "python", "python3", "pip", "pypi",
    "def", "lambda", "decorator", "decorators",
    "list", "tuple", "dictionary", "dict", "set",
    "function", "functions", "class", "classes",
    "object", "objects", "module", "modules",
    "package", "packages", "import", "exception",
    "exceptions", "iterator", "iterators", "generator",
    "generators", "list comprehension", "pandas",
    "numpy", "django", "flask", "pytest", "virtualenv",
    "venv", "f-string", "self", "none", "asyncio"
}

def check_python_topic(user_message: str) -> bool:
    """Return True when a message appears related to Python."""
    text = user_message.lower()
    words = set(re.findall(r"[a-zA-Z_][a-zA-Z_0-9]*", text))

    # Explicit Python references are strong indicators.
    if "python" in words or "python3" in words:
        return True

    # Recognize common Python concepts and libraries.
    if words.intersection(PYTHON_TERMS):
        return True

    return False
