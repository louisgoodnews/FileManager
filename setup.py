"""
FileManager - A robust and intuitive file management utility for Python
"""

from pathlib import Path

from setuptools import find_packages, setup

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# This is a minimal setup.py that defers to pyproject.toml
# It's maintained for compatibility with tools that haven't adopted PEP 621 yet

if __name__ == "__main__":
    # Use setuptools.setup with minimal configuration
    # Most configuration should be in pyproject.toml
    setup(
        # These will be overridden by pyproject.toml when using a PEP 517 build backend
        name="filemanager-louisgoodnews",
        version="0.1.0",
        description="A robust and intuitive file management utility for Python",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="Louis Goodnews",
        author_email="louisgoodnews95@gmail.com",
        url="https://github.com/louisgoodnews/FileManager",
        packages=find_packages(where="src"),
        package_dir={"": "src"},
        python_requires=">=3.7",
        # Dependencies are specified in pyproject.toml
        # This is here for backward compatibility
        install_requires=[
            "aiofiles>=23.1.0",
            "pyunpack>=0.3.1",
            "patool>=1.12",
        ],
        # Additional metadata
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: Filesystems",
        ],
        # Include package data files (non-Python files)
        include_package_data=True,
        # Entry points for command-line tools (if any)
        # entry_points={
        #     'console_scripts': [
        #         'filemanager=FileManager.cli:main',
        #     ],
        # },
    )
