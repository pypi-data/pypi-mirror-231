from pathlib import Path

import setuptools

__version__ = "0.6.1"
__author__ = "Michał Skibiński"

this_directory = Path(__file__).parent

with open(this_directory / "requirements.txt") as f:
    requirements = f.read().splitlines()


setuptools.setup(
    name="chess-insight",
    install_requires=requirements,
    version=__version__,
    author=__author__,
    author_email="mskibinski109@gmail.com",
    description="""
        Modern package for analyzing chess games. 
        """.replace(
        "\n", " "
    ).strip(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="GPL-3.0+",
    # keywords=" draughts, checkers, AI mini-max, game, board",
    url="https://github.com/michalskibinski109/chess-insight",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Board Games",
        "Topic :: Games/Entertainment :: Turn Based Strategy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Typing :: Typed",
    ],
    python_requires=">=3.7",
)
