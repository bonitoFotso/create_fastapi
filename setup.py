"""
Configuration du package pour l'installation
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("fastapi_generator/__init__.py", "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"').strip("'")
            break

setup(
    name="fastapi-generator",
    version=version,
    author="Votre Nom",
    author_email="votre.email@example.com",
    description="Un générateur d'applications FastAPI avec structure complète",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votrenom/fastapi-generator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.0.0",
        "jinja2>=3.0.0",
        "colorama>=0.4.0",
    ],
    entry_points={
        "console_scripts": [
            "fastapi-gen=fastapi_generator.cli:main",
            "fastapi-generator=fastapi_generator.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "fastapi_generator": ["templates/**/*"],
    },
)