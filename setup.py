import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="fib-example-pkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    license="MIT",
    description="Compute Fibonacci numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AdamChristiansen/python-virtual-env-template",
    packages=setuptools.find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
