from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mypykit",
    version="0.0.3",
    author="haninam",
    author_email="2050love@naver.com",
    description="my sample lib",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/schooldevops/python-tutorials",
    # project_urls={
    #     "Bug Tracker": "https://github.com/schooldevops/python-tutorials/issues",
    # },
    install_requires=['pykrx', 'pandas'],
    packages=find_packages(exclude=[]),
    classifiers=[
        "Programming Language :: Python :: 3",
        # "License :: OSI Approved :: MIT License",
        # "Operating System :: OS Independent",
    ],
    # package_dir={"": "src"},
    # keywords=['teddynote', 'teddylee777', 'python datasets', 'python tutorial', 'pypi'],
    # packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)