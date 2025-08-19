"""
Author: Louis Goodnews
Date: 2025-08-19
"""

import aiofiles
import os
import shutil
import sys
import traceback

from datetime import datetime
from enum import Enum
from pathlib import Path
from pyunpack import Archive
from tkinter import filedialog
from typing import Final, List, Optional, Tuple, Union


__all__: Final[List[str]] = ["FileManager"]


class FileTask(Enum):
    """
    The FileTask enum is an enum that represents the different file operations.

    Attributes:
    ----------
    COPY: Copy a file
    CREATE: Create a file
    DELETE: Delete a file
    EXISTS: Check if a file or directory exists
    LINK: Create a symlink
    MOVE: Move a file
    READ: Read a file
    RENAME: Rename a file
    UNPACK: Unpack an archive
    WRITE: Write to a file
    """

    COPY = "copy"
    CREATE = "create"
    DELETE = "delete"
    EXISTS = "exists"
    LINK = "link"
    MOVE = "move"
    READ = "read"
    RENAME = "rename"
    UNPACK = "unpack"
    WRITE = "write"

    def __str__(self) -> str:
        """
        Returns the string representation of the enum member.

        :return: The string representation of the enum member
        :rtype: str
        """

        # Return the string representation of the enum member
        return self.value


class FileManager:
    """
    The FileManager class is a utility class that provides methods for file and directory operations.

    Attributes:
    ----------
    CWD: The current working directory

    Methods:
    -------
    ask_and_open_file: Asks the user to open a file
    ask_and_open_files: Asks the user to open files
    ask_and_open_file_name: Asks the user to open a file name
    ask_and_open_file_names: Asks the user to open file names
    ask_and_save_file: Asks the user to save a file
    create_directory: Creates a directory at the given path
    create_file: Creates a file at the given path
    create_symlink: Creates a symlink at the given path
    delete_directory: Deletes a directory at the given path
    delete_file: Deletes a file at the given path
    delete_symlink: Deletes a symlink at the given path
    does_directory_exist: Checks if a directory exists at the given path
    does_file_exist: Checks if a file exists at the given path
    does_symlink_exist: Checks if a symlink exists at the given path
    is_directory_empty: Checks if a directory is empty
    move_directory: Moves a directory to the given destination
    move_file: Moves a file to the given destination
    rename_directory: Renames a directory at the given path
    rename_file: Renames a file at the given path
    rename_symlink: Renames a symlink at the given path
    read_file: Reads a file at the given path
    unpack_archive: Unpacks an archive at the given path
    write_file: Writes content to a file at the given path
    """

    # Initialize the current working directory
    CWD: Final[Path] = Path(os.getcwd())

    # Initialize the OS
    OS: Final[str] = sys.platform

    @classmethod
    def _convert_to_path(
        cls,
        path: Union[str, Path],
    ) -> Path:
        """
        Converts the given path to a Path object

        :param path: The path to convert
        :type path: Union[str, Path]

        :return: The converted path
        :rtype: Path
        """

        # Check if the path is a Path object
        if not isinstance(
            path,
            Path,
        ):
            # Convert the path to a Path object
            path = Path(path=path)

        # Return the path
        return path

    @classmethod
    def ask_and_open_directory(
        cls,
        title: str,
        initialdir: Optional[Union[str, Path]] = None,
    ) -> Optional[str]:
        """
        Asks the user to open a directory

        :param title: The title of the directory dialog
        :type title: str
        :param initialdir: The initial directory to open the directory dialog at
        :type initialdir: Optional[Union[str, Path]]

        :return: The path to the directory if the user opened it, None otherwise
        :rtype: Optional[str]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening directory at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        try:
            # Ask the user to open a directory
            return filedialog.askdirectory(
                initialdir=initialdir,
                title=title,
            )
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to open directory at '{initialdir.resolve()}':\n{traceback.format_exc()}"
            )

            # Return None
            return None

    @classmethod
    def ask_and_open_file(
        cls,
        title: str,
        filetypes: List[Tuple[str, str]],
        initialdir: Optional[Union[str, Path]] = None,
        initialfile: Optional[Union[str, Path]] = None,
    ) -> Optional[str]:
        """
        Asks the user to open a file

        :param title: The title of the file dialog
        :type title: str
        :param filetypes: The file types to filter by
        :type filetypes: List[Tuple[str, str]]
        :param initialdir: The initial directory to open the file dialog at
        :type initialdir: Optional[Union[str, Path]]
        :param initialfile: The initial file to open the file dialog at
        :type initialfile: Optional[Union[str, Path]]

        :return: The path to the file if the user opened it, None otherwise
        :rtype: Optional[str]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        # Check if the initial file has been passed
        if initialfile:
            # Convert the initial file to a Path object
            initialfile = cls._convert_to_path(path=initialfile)

            # Check if the initial file exists
            if not cls.does_file_exist(path=initialfile):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file at '{initialfile.resolve()}' impossible: file does not exist. Aborting..."
                )

                # Return None
                return None

        try:
            # Ask the user to open a file
            return filedialog.askopenfilename(
                filetypes=filetypes,
                initialdir=initialdir,
                initialfile=initialfile,
                title=title,
            )
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to open file at '{initialfile.resolve()}':\n{traceback.format_exc()}"
            )

            # Return None
            return None

    @classmethod
    def ask_and_open_files(
        cls,
        title: str,
        filetypes: List[Tuple[str, str]],
        initialdir: Optional[Union[str, Path]] = None,
        initialfile: Optional[Union[str, Path]] = None,
    ) -> Optional[Union[Tuple[str, ...], str]]:
        """
        Asks the user to open files

        :param title: The title of the file dialog
        :type title: str
        :param filetypes: The file types to filter by
        :type filetypes: List[Tuple[str, str]]
        :param initialdir: The initial directory to open the file dialog at
        :type initialdir: Optional[Union[str, Path]]
        :param initialfile: The initial file to open the file dialog at
        :type initialfile: Optional[Union[str, Path]]

        :return: The paths to the files if the user opened them, None otherwise
        :rtype: Optional[Union[Tuple[str, ...], str]]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening files at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        # Check if the initial file has been passed
        if initialfile:
            # Convert the initial file to a Path object
            initialfile = cls._convert_to_path(path=initialfile)

            # Check if the initial file exists
            if not cls.does_file_exist(path=initialfile):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening files at '{initialfile.resolve()}' impossible: file does not exist. Aborting..."
                )

                # Return None
                return None

        try:
            # Ask the user to open files
            return filedialog.askopenfilenames(
                filetypes=filetypes,
                initialdir=initialdir,
                initialfile=initialfile,
                title=title,
            )
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to open files at '{initialfile.resolve()}':\n{traceback.format_exc()}"
            )

            # Return None
            return None

    @classmethod
    def ask_and_open_file_name(
        cls,
        title: str,
        filetypes: List[Tuple[str, str]],
        initialdir: Optional[Union[str, Path]] = None,
        initialfile: Optional[Union[str, Path]] = None,
    ) -> Optional[str]:
        """
        Asks the user to open a file name

        :param title: The title of the file dialog
        :type title: str
        :param filetypes: The file types to filter by
        :type filetypes: List[Tuple[str, str]]
        :param initialdir: The initial directory to open the file dialog at
        :type initialdir: Optional[Union[str, Path]]
        :param initialfile: The initial file to open the file dialog at
        :type initialfile: Optional[Union[str, Path]]

        :return: The path to the file if the user opened it, None otherwise
        :rtype: Optional[str]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file name at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        # Check if the initial file has been passed
        if initialfile:
            # Convert the initial file to a Path object
            initialfile = cls._convert_to_path(path=initialfile)

            # Check if the initial file exists
            if not cls.does_file_exist(path=initialfile):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file name at '{initialfile.resolve()}' impossible: file does not exist. Aborting..."
                )

                # Return None
                return None

        try:
            # Ask the user to open a file name
            return filedialog.askopenfilename(
                filetypes=filetypes,
                initialdir=initialdir,
                initialfile=initialfile,
                title=title,
            )
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to open file name at '{initialfile.resolve()}':\n{traceback.format_exc()}"
            )

            # Return None
            return None

    @classmethod
    def ask_and_open_file_names(
        cls,
        title: str,
        filetypes: List[Tuple[str, str]],
        initialdir: Optional[Union[str, Path]] = None,
        initialfile: Optional[Union[str, Path]] = None,
    ) -> Optional[Union[Tuple[str, ...], str]]:
        """
        Asks the user to open file names

        :param title: The title of the file dialog
        :type title: str
        :param filetypes: The file types to filter by
        :type filetypes: List[Tuple[str, str]]
        :param initialdir: The initial directory to open the file dialog at
        :type initialdir: Optional[Union[str, Path]]
        :param initialfile: The initial file to open the file dialog at
        :type initialfile: Optional[Union[str, Path]]

        :return: The paths to the files if the user opened them, None otherwise
        :rtype: Optional[Union[Tuple[str, ...], str]]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file names at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        # Check if the initial file has been passed
        if initialfile:
            # Convert the initial file to a Path object
            initialfile = cls._convert_to_path(path=initialfile)

            # Check if the initial file exists
            if not cls.does_file_exist(path=initialfile):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Opening file names at '{initialfile.resolve()}' impossible: file does not exist. Aborting..."
                )

                # Return None
                return None

        try:
            # Ask the user to open file names
            return filedialog.askopenfilenames(
                filetypes=filetypes,
                initialdir=initialdir,
                initialfile=initialfile,
                title=title,
            )
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to open file names at '{initialfile.resolve()}':\n{traceback.format_exc()}"
            )

            # Return None
            return None

    @classmethod
    def ask_and_save_file(
        cls,
        title: str,
        filetypes: List[Tuple[str, str]],
        initialdir: Optional[Union[str, Path]] = None,
        initialfile: Optional[Union[str, Path]] = None,
    ) -> Optional[str]:
        """
        Asks the user to save a file

        :param title: The title of the file dialog
        :type title: str
        :param filetypes: The file types to filter by
        :type filetypes: List[Tuple[str, str]]
        :param initialdir: The initial directory to open the file dialog at
        :type initialdir: Optional[Union[str, Path]]
        :param initialfile: The initial file to open the file dialog at
        :type initialfile: Optional[Union[str, Path]]

        :return: The path to the file if the user saved it, None otherwise
        :rtype: Optional[str]
        """

        # Check if the initial directory has been passed
        if initialdir:
            # Convert the initial directory to a Path object
            initialdir = cls._convert_to_path(path=initialdir)

            # Check if the initial directory exists
            if not cls.does_directory_exist(path=initialdir):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Saving file at '{initialdir.resolve()}' impossible: directory does not exist. Aborting..."
                )

                # Return None
                return None

        # Check if the initial file has been passed
        if initialfile:
            # Convert the initial file to a Path object
            initialfile = cls._convert_to_path(path=initialfile)

            # Check if the initial file exists
            if not cls.does_file_exist(path=initialfile):
                # Log the warning
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Saving file at '{initialfile.resolve()}' impossible: file does not exist. Aborting..."
                )

                # Return None
                return None

        # Ask the user to save a file
        return filedialog.asksaveasfilename(
            filetypes=filetypes,
            initialdir=initialdir,
            initialfile=initialfile,
            title=title,
        )

    @classmethod
    def copy_directory(
        cls,
        source: Union[str, Path],
        destination: Union[str, Path],
    ) -> bool:
        """
        Copies a directory to the given destination

        :param source: The source directory to copy
        :type source: Union[str, Path]
        :param destination: The destination directory to copy to
        :type destination: Union[str, Path]

        :return: True if the directory was copied, False otherwise
        :rtype: bool
        """

        # Convert the source to a Path object
        source = cls._convert_to_path(path=source)

        # Check if the source directory exists
        if not cls.does_directory_exist(path=source):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Copying directory at '{source.resolve()}' impossible: source directory does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the destination to a Path object
        destination = cls._convert_to_path(path=destination)

        # Check if the destination directory exists
        if cls.does_directory_exist(path=destination):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Copying directory at '{source.resolve()}' to '{destination.resolve()}' impossible: destination directory already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Copy the directory
            shutil.copytree(
                src=source,
                dst=destination,
            )

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to copy directory at '{source.resolve()}' to '{destination.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def copy_file(
        cls,
        source: Union[str, Path],
        destination: Union[str, Path],
    ) -> bool:
        """
        Copies a file to the given destination

        :param source: The source file to copy
        :type source: Union[str, Path]
        :param destination: The destination file to copy to
        :type destination: Union[str, Path]

        :return: True if the file was copied, False otherwise
        :rtype: bool
        """

        # Convert the source to a Path object
        source = cls._convert_to_path(path=source)

        # Check if the source file exists
        if not cls.does_file_exist(path=source):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Copying file at '{source.resolve()}' impossible: source file does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the destination to a Path object
        destination = cls._convert_to_path(path=destination)

        # Check if the destination file exists
        if cls.does_file_exist(path=destination):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Copying file at '{source.resolve()}' to '{destination.resolve()}' impossible: destination file already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Copy the file
            shutil.copyfile(
                src=source,
                dst=destination,
            )

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to copy file at '{source.resolve()}' to '{destination.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def create_directory(
        cls,
        path: Union[str, Path],
        create_parents: bool = False,
    ) -> bool:
        """
        Creates a directory at the given path

        :param path: The path to create the directory at
        :type path: Union[str, Path]
        :param create_parents: Whether to create the parent directories if they do not exist
        :type create_parents: bool

        :return: True if the directory was created, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the directory exists
        if cls.does_directory_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Directory at '{path.resolve()}' already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Create the directory
            path.mkdir(parents=create_parents)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to create directory at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def create_file(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Creates a file at the given path

        :param path: The path to create the file at
        :type path: Union[str, Path]

        :return: True if the file was created, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | File at '{path.resolve()}' already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Create the file
            path.touch()

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to create file at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def create_symlink(
        cls,
        source: Union[str, Path],
        target: Union[str, Path],
    ) -> bool:
        """
        Creates a symlink at the given path

        :param source: The source path
        :type source: Union[str, Path]
        :param target: The target path
        :type target: Union[str, Path]

        :return: True if the symlink was created, False otherwise
        :rtype: bool
        """

        # Convert the source to a Path object
        source = cls._convert_to_path(path=source)

        # Check if the source exists
        if not cls.does_exist(path=source):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Creating symlink at '{source.resolve()}' impossible: source file does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the target to a Path object
        target = cls._convert_to_path(path=target)

        # Check if the target exists
        if cls.does_exist(path=target):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Creating symlink at '{source.resolve()}' to '{target.resolve()}' impossible: target file already exists. Aborting..."
            )

            # Return False
            return False

        try:
            if OS == "Windows":
                # Create the symlink
                os.symlink(
                    src=source,
                    dst=target,
                )
            else:
                # Create the symlink
                source.symlink_to(
                    target=target,
                    target_is_directory=target.is_dir(),
                )

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to create symlink at '{source.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def delete_directory(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Deletes a directory at the given path

        :param path: The path to delete the directory at
        :type path: Union[str, Path]

        :return: True if the directory was deleted, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the directory exists
        if not cls.does_directory_exist(path=path):
            # Print the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Deleting directory at '{path.resolve()}' impossible: directory does not exist. Aborting..."
            )

            # Return False
            return False

        # Check if the directory is empty
        if not cls.is_directory_empty(path=path):
            # Print the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Deleting directory at '{path.resolve()}' impossible: directory is not empty. Aborting..."
            )

            # Return False
            return False

        try:
            # Delete the directory
            path.rmdir()

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to delete directory at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def delete_file(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Deletes a file at the given path

        :param path: The path to delete the file at
        :type path: Union[str, Path]

        :return: True if the file was deleted, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if not cls.does_file_exist(path=path):
            # Print the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Deleting file at '{path.resolve()}' impossible: file does not exist. Aborting..."
            )

            # Return False
            return False

        try:
            # Delete the file
            path.unlink()

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to delete file at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def delete_symlink(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Deletes a symlink at the given path

        :param path: The path to delete the symlink at
        :type path: Union[str, Path]

        :return: True if the symlink was deleted, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the symlink exists
        if not cls.does_exist(path=path):
            # Print the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Deleting symlink at '{path.resolve()}' impossible: symlink does not exist. Aborting..."
            )

            # Return False
            return False

        try:
            # Delete the symlink
            path.unlink()

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to delete symlink at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def does_exist(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Checks if a path exists at the given path

        :param path: The path to check
        :type path: Union[str, Path]

        :return: True if the path exists, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Return whether the path exists
        return path.exists()

    @classmethod
    def does_directory_exist(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Checks if a directory exists at the given path

        :param path: The path to check
        :type path: Union[str, Path]

        :return: True if the directory exists, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the path is a directory
        if not path.is_dir():
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Directory at '{path.resolve()}' does not exist or is not a directory. Aborting..."
            )

            # Return False
            return False

        # Return whether the directory exists
        return path.exists()

    @classmethod
    def does_file_exist(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Checks if a file exists at the given path

        :param path: The path to check
        :type path: Union[str, Path]

        :return: True if the file exists, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the path is a file
        if not path.is_file():
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | File at '{path.resolve()}' does not exist or is not a file. Aborting..."
            )

            # Return False
            return False

        # Return whether the file exists
        return path.exists()

    @classmethod
    def is_directory_empty(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Checks if a directory is empty

        :param path: The path to check
        :type path: Union[str, Path]

        :return: True if the directory is empty, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Return whether the directory is empty
        return not any(path.iterdir())

    @classmethod
    def is_file_empty(
        cls,
        path: Union[str, Path],
    ) -> bool:
        """
        Checks if a file is empty

        :param path: The path to check
        :type path: Union[str, Path]

        :return: True if the file is empty, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if not cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | File at '{path.resolve()}' does not exist or is not a file. Aborting..."
            )

            # Return False
            return False

        # Return whether the file is empty
        return not path.stat().st_size

    @classmethod
    def move_directory(
        cls,
        path: Union[str, Path],
        destination: Union[str, Path],
    ) -> bool:
        """
        Moves a directory to the given destination

        :param path: The path to move the directory to
        :type path: Union[str, Path]
        :param destination: The destination to move the directory to
        :type destination: Union[str, Path]

        :return: True if the directory was moved, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the directory exists
        if not cls.does_directory_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Moving directory at '{path.resolve()}' impossible: directory does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the destination to a Path object
        destination = cls._convert_to_path(destination)

        # Check if the destination exists
        if cls.does_directory_exist(destination):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Moving directory at '{path.resolve()}' impossible: destination directory already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Move the directory
            path.rename(target=destination)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to move directory at '{path.resolve()}' to '{destination.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def move_file(
        cls,
        path: Union[str, Path],
        destination: Union[str, Path],
    ) -> bool:
        """
        Moves a file to the given destination

        :param path: The path to move the file to
        :type path: Union[str, Path]
        :param destination: The destination to move the file to
        :type destination: Union[str, Path]

        :return: True if the file was moved, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if not cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Moving file at '{path.resolve()}' impossible: file does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the destination to a Path object
        destination = cls._convert_to_path(destination)

        # Check if the destination exists
        if cls.does_file_exist(destination):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Moving file at '{path.resolve()}' impossible: destination file already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Move the file
            path.rename(target=destination)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to move file at '{path.resolve()}' to '{destination.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def open(
        cls,
        source: Union[str, Path],
        file_task: FileTask,
        target: Optional[Union[str, Path]] = None,
        new_name: Optional[str] = None,
    ) -> Union[bool, str]:
        """
        Opens a file at the given path

        :param source: The source file to open
        :type source: Union[str, Path]
        :param file_task: The file task to perform
        :type file_task: FileTask
        :param target: The target file to open to
        :type target: Optional[Union[str, Path]]
        :param new_name: The new name of the file
        :type new_name: Optional[str]

        :return: True if the file was opened, False otherwise
        :rtype: Union[bool, str]
        """

        if file_task == "copy":
            return (
                cls.copy_directory(
                    source=source,
                    destination=target,
                )
                if cls.does_directory_exist(path=source)
                else cls.copy_file(
                    source=source,
                    destination=target,
                )
            )

        if file_task == "create":
            return (
                cls.create_directory(path=source)
                if cls.does_directory_exist(path=source)
                else (
                    cls.create_file(path=source)
                    if cls.does_file_exist(path=source)
                    else cls.create_symlink(path=source)
                )
            )

        if file_task == "delete":
            return (
                cls.delete_directory(path=source)
                if cls.does_directory_exist(path=source)
                else (
                    cls.delete_file(path=source)
                    if cls.does_file_exist(path=source)
                    else cls.delete_symlink(path=source)
                )
            )

        if file_task == "exists":
            return (
                cls.does_directory_exist(path=source)
                if cls.does_directory_exist(path=source)
                else (
                    cls.does_file_exist(path=source)
                    if cls.does_file_exist(path=source)
                    else cls.does_symlink_exist(path=source)
                )
            )

        if file_task == "empty":
            return (
                cls.is_directory_empty(path=source)
                if cls.does_directory_exist(path=source)
                else cls.is_file_empty(path=source)
            )

        if file_task == "link":
            return cls.create_symlink(
                source=source,
                target=target,
            )

        if file_task == "move":
            return (
                cls.move_directory(
                    path=source,
                    destination=target,
                )
                if cls.does_directory_exist(path=source)
                else cls.move_file(
                    path=source,
                    destination=target,
                )
            )

        if file_task == "read":
            return cls.read_file(path=source)

        if file_task == "rename":
            return (
                cls.rename_directory(
                    path=source,
                    new_name=new_name,
                )
                if cls.does_directory_exist(path=source)
                else (
                    cls.rename_file(
                        path=source,
                        new_name=new_name,
                    )
                    if cls.does_file_exist(path=source)
                    else cls.rename_symlink(
                        path=source,
                        new_name=new_name,
                    )
                )
            )

        if file_task == "unpack":
            return cls.unpack_archive(
                path=source,
                extract_to=target,
            )

        if file_task == "write":
            return cls.write_file(
                path=source,
                content=target,
            )

    @classmethod
    def read_file(
        cls,
        path: Union[str, Path],
    ) -> Optional[str]:
        """
        Reads a file at the given path

        :param path: The path to read the file at
        :type path: Union[str, Path]

        :return: The content of the file if it was read, None otherwise
        :rtype: Optional[str]
        """

        async def _read_file(path: Path) -> Optional[str]:
            """
            Reads a file at the given path

            :param path: The path to read the file at
            :type path: Path

            :return: The content of the file if it was read, None otherwise
            :rtype: Optional[str]
            """

            try:
                # Read the file
                async with aiofiles.open(
                    encoding="utf-8",
                    file=path,
                    mode="r",
                ) as file:
                    # Return the content of the file
                    return await file.read()
            except Exception:
                # Print the error
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to read file at '{path.resolve()}':\n{traceback.format_exc()}"
                )

                # Return None
                return None

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if not cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Reading file at '{path.resolve()}' impossible: file does not exist. Aborting..."
            )

            # Return None
            return None

        # Run the async function and return the result
        return asyncio.run(_read_file(path=path))

    @classmethod
    def rename_directory(
        cls,
        path: Union[str, Path],
        new_name: str,
    ) -> bool:
        """
        Renames a directory at the given path

        :param path: The path to rename the directory at
        :type path: Union[str, Path]
        :param new_name: The new name of the directory
        :type new_name: str

        :return: True if the directory was renamed, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the directory exists
        if not cls.does_directory_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming directory at '{path.resolve()}' impossible: directory does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the new name to a Path object
        new_name = cls._convert_to_path(
            path=Path(
                path.parent,
                new_name,
            )
        )

        # Check if the new name exists
        if cls.does_directory_exist(path=new_name):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming directory at '{path.resolve()}' impossible: new name already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Rename the directory
            path.rename(target=new_name)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to rename directory at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def rename_file(
        cls,
        path: Union[str, Path],
        new_name: str,
    ) -> bool:
        """
        Renames a file at the given path

        :param path: The path to rename the file at
        :type path: Union[str, Path]
        :param new_name: The new name of the file
        :type new_name: str

        :return: True if the file was renamed, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if not cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming file at '{path.resolve()}' impossible: file does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the new name to a Path object
        new_name = cls._convert_to_path(
            path=Path(
                path.parent,
                new_name,
            )
        )

        # Check if the new name exists
        if cls.does_file_exist(path=new_name):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming file at '{path.resolve()}' impossible: new name already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Rename the file
            path.rename(target=new_name)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to rename file at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def rename_symlink(
        cls,
        path: Union[str, Path],
        new_name: str,
    ) -> bool:
        """
        Renames a symlink at the given path

        :param path: The path to rename the symlink at
        :type path: Union[str, Path]
        :param new_name: The new name of the symlink
        :type new_name: str

        :return: True if the symlink was renamed, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the symlink exists
        if not cls.does_symlink_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming symlink at '{path.resolve()}' impossible: symlink does not exist. Aborting..."
            )

            # Return False
            return False

        # Convert the new name to a Path object
        new_name = cls._convert_to_path(
            path=Path(
                path.parent,
                new_name,
            )
        )

        # Check if the new name exists
        if cls.does_symlink_exist(path=new_name):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Renaming symlink at '{path.resolve()}' impossible: new name already exists. Aborting..."
            )

            # Return False
            return False

        try:
            # Rename the symlink
            path.rename(target=new_name)

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to rename symlink at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def unpack_archive(
        cls,
        path: Union[str, Path],
        extract_to: Union[str, Path],
    ) -> bool:
        """
        Unpacks an archive at the given path to the given destination

        :param path: The path to unpack the archive at
        :type path: Union[str, Path]
        :param extract_to: The path to extract the archive to
        :type extract_to: Union[str, Path]

        :return: True if the archive was unpacked, False otherwise
        :rtype: bool
        """

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Convert the extract to to a Path object
        extract_to = cls._convert_to_path(path=extract_to)

        try:
            # Unpack the archive
            Archive(filename=path).extractall(
                auto_create_dir=True,
                directory=extract_to,
            )

            # Return True
            return True
        except Exception:
            # Print the error
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to unpack archive at '{path.resolve()}':\n{traceback.format_exc()}"
            )

            # Return False
            return False

    @classmethod
    def write_file(
        cls,
        path: Union[str, Path],
        content: str,
    ) -> bool:
        """
        Writes content to a file at the given path

        :param path: The path to write the content to
        :type path: Union[str, Path]
        :param content: The content to write to the file
        :type content: str

        :return: True if the content was written, False otherwise
        :rtype: bool
        """

        async def _write_file(path: Path, content: str) -> bool:
            """
            Writes content to a file at the given path

            :param path: The path to write the content to
            :type path: Path
            :param content: The content to write to the file
            :type content: str

            :return: True if the content was written, False otherwise
            :rtype: bool
            """

            try:
                async with aiofiles.open(
                    encoding="utf-8",
                    file=path,
                    mode="w",
                ) as file:
                    await file.write(content)

                # Return True
                return True
            except Exception:
                # Print the error
                print(
                    f"{datetime.now().isoformat()} | {cls.__name__} | ERROR | Caught an exception while attempting to write content to file at '{path.resolve()}':\n{traceback.format_exc()}"
                )

                # Return False
                return False

        # Convert the path to a Path object
        path = cls._convert_to_path(path=path)

        # Check if the file exists
        if cls.does_file_exist(path=path):
            # Log the warning
            print(
                f"{datetime.now().isoformat()} | {cls.__name__} | WARNING | Writing content to file at '{path.resolve()}' impossible: file already exists. Aborting..."
            )

            # Return False
            return False

        # Run the async function and return the result
        return asyncio.run(
            _write_file(
                path=path,
                content=content,
            )
        )
