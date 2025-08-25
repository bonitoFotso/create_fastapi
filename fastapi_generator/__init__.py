"""FastAPI Generator - Un générateur d'applications FastAPI"""

__version__ = "1.0.0"
__author__ = "Votre Nom"
__email__ = "votre.email@example.com"

from .cli import main
from .generator import FastAPIGenerator

__all__ = ["FastAPIGenerator", "main"]
