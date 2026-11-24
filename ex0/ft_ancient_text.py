import sys
import typing


def report_error(message: str) -> None:
    print(message)


def read_archive(filename: str) -> str | None:
    print(f"Accessing file '{filename}'")
    try:
        archive: typing.IO[str] = open(filename, "r", encoding="utf-8")
    except (OSError, ValueError) as error:
        report_error(f"Error opening file '{filename}': {error}")
        return None
    content: str | None = None
    try:
        content = archive.read()
    except (OSError, UnicodeError) as error:
        report_error(f"Error reading file '{filename}': {error}")
    finally:
        try:
            archive.close()
        except OSError as error:
            report_error(f"Error closing file '{filename}': {error}")
            content = None
    if content is not None:
        display_content(content)
        print(f"File '{filename}' closed.")
    return content


def display_content(content: str) -> None:
    print("---\n")
    print(content, end="")
    print("\n---")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    read_archive(sys.argv[1])


if __name__ == "__main__":
    main()
