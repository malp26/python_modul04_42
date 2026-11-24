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


def transform_content(content: str) -> str:
    transformed: list[str] = []
    for line in content.splitlines(keepends=True):
        if line.endswith("\n"):
            transformed.append(line[:-1] + "#\n")
        else:
            transformed.append(line + "#")
    return "".join(transformed)


def save_archive(filename: str, content: str) -> bool:
    print(f"Saving data to '{filename}'")
    try:
        archive: typing.IO[str] = open(filename, "w", encoding="utf-8")
    except (OSError, ValueError) as error:
        report_error(f"Error opening file '{filename}': {error}")
        return False
    success = True
    try:
        archive.write(content)
    except (OSError, UnicodeError) as error:
        report_error(f"Error writing file '{filename}': {error}")
        success = False
    finally:
        try:
            archive.close()
        except OSError as error:
            report_error(f"Error closing file '{filename}': {error}")
            success = False
    return success


def get_destination() -> str:
    return input("Enter new file name (or empty): ")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    content = read_archive(sys.argv[1])
    if content is None:
        return
    transformed = transform_content(content)
    print("\nTransform data:")
    display_content(transformed)
    try:
        filename = get_destination()
    except (EOFError, KeyboardInterrupt, OSError, UnicodeError) as error:
        report_error(f"Destination input interrupted: {error}")
        print("Not saving data.")
        return
    if not filename:
        print("Not saving data.")
    elif save_archive(filename, transformed):
        print(f"Data saved in file '{filename}'.")
    else:
        print("Data not saved.")


if __name__ == "__main__":
    main()
