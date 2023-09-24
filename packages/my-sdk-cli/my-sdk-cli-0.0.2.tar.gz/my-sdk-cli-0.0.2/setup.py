import sys
from setuptools import setup, find_packages

setup(
    name="my-sdk-cli",
    version="0.2",
    packages=find_packages(),
    author="Vivek-Yadav",
    author_email="vy.code92@gmail.com",
    entry_points={
        "console_scripts": [
            "my-sdk-cli = __main__:main"
        ],
    },
    python_requires='>=3.7',
    install_requires=[
        # Add any dependencies here
    ],
    project_urls={
        'GitHub': 'https://github.com/Code-Xg9/code-wave-cli'
    },
)
