from pathlib import Path


def read_log_file(file_path: str) -> list[str]:
    """
    Read a log file and return its lines.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")

    return path.read_text(encoding="utf-8").splitlines()