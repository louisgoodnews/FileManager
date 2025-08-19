"""
Author: Louis Goodnews
Date: 2025-08-19
"""

from core.core import FileManager


def main() -> None:
    """ """

    # Print the current working directory
    print(FileManager.CWD)

    # Create a directory
    FileManager.create_directory(path="test_dir")

    # Delete the directory
    FileManager.delete_directory(path="test_dir")

    # Create a file
    FileManager.create_file(path="test_1.txt")

    # Create a file
    FileManager.create_file(path="test_2.txt")

    # Create a symlink
    FileManager.create_symlink(
        source="test_1.txt",
        target="test_1_link.txt",
    )

    # Write to the file
    FileManager.write_file(
        path="test_1.txt",
        content="Hello, World!",
    )

    # Read the file
    print(FileManager.read_file(path="test_1.txt"))

    # Delete the file
    FileManager.delete_file(path="test_1.txt")

    # Delete the file
    FileManager.delete_file(path="test_1_link.txt")

    # Delete the file
    FileManager.delete_file(path="test_2.txt")

    # Delete the directory
    FileManager.delete_directory(path="test_dir")


if __name__ == "__main__":
    main()
