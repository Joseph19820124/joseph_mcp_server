# server.py
from fastmcp import FastMCP
import random

magic_words = ["consistent", "honor", "attitude", "motivation", "perseverance", "integrity", "optimistic", "never giving up"]

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

@mcp.tool
def magic_word() -> str:
    """Return a random word from the list"""
    return random.choice(magic_words)

if __name__ == "__main__":
    mcp.run()
