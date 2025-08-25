"""FastAPI Generator - Un générateur d'applications FastAPI"""

__version__ = "1.0.0"
__author__ = "Votre Nom"
__email__ = "votre.email@example.com"

from .generator import FastAPIGenerator
from .cli import main

__all__ = ["FastAPIGenerator", "main"]