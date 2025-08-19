# FileManager

A robust and intuitive file management utility for Python that simplifies common file and directory operations with a clean, object-oriented interface.

## Features

- **File Operations**: Create, read, write, move, copy, rename, and delete files
- **Directory Management**: Create, check existence, and delete directories
- **Symlink Handling**: Create and manage symbolic links
- **Archive Support**: Extract various archive formats
- **Platform Independent**: Works across different operating systems
- **Type Annotated**: Full type hints for better IDE support and code clarity
- **Asynchronous Support**: Built with `aiofiles` for non-blocking I/O operations

## Installation

```bash
pip install file-manager-louisgoodnews
```

## Quick Start

```python
import FileManager

# Create a new file
FileManager.create_file("example.txt", "Hello, World!")

# Read file content
content = FileManager.read_file("example.txt")
print(content)  # Output: Hello, World!

# Check if file exists
if FileManager.does_file_exist("example.txt"):
    print("File exists!")
```

## Available Methods

### File Operations
- `create_file(path: str, content: str = "") -> bool`
- `read_file(path: str) -> str`
- `write_file(path: str, content: str, mode: str = "w") -> bool`
- `delete_file(path: str) -> bool`
- `move_file(source: str, destination: str) -> bool`
- `copy_file(source: str, destination: str) -> bool`
- `rename_file(path: str, new_name: str) -> bool`

### Directory Operations
- `create_directory(path: str) -> bool`
- `delete_directory(path: str) -> bool`
- `is_directory_empty(path: str) -> bool`
- `move_directory(source: str, destination: str) -> bool`
- `rename_directory(path: str, new_name: str) -> bool`

### Symlink Operations
- `create_symlink(source: str, destination: str) -> bool`
- `delete_symlink(path: str) -> bool`

### Archive Operations
- `unpack_archive(archive_path: str, extract_dir: str = None) -> bool`

## Error Handling

All methods return boolean values indicating success/failure and raise appropriate exceptions with descriptive messages when operations fail.

## Dependencies

- Python 3.7+
- aiofiles
- pyunpack
- patool

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Louis Goodnews - [@louisgoodnews](https://github.com/louisgoodnews)
