from setuptools import find_packages, setup

with open("app/README.md") as f:
    long_description = f.read()

setup(
    name = "scian_ciiu",
    version = "0.0.13",
    description = "A library to search the corresponding mexican scian or ciiu given an input parameter",
    package_dir = {"":"app"},
    packages = find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dimitrj89/scian_ciiu",
    author="Dimitrj Bonansea",
    author_email="dimitrj22@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)