"""Tests for the greeter module."""

import pytest

from hello_lib import Greeter, greet


class TestGreeter:
    """Tests for the Greeter class."""

    def test_greet_default_name(self) -> None:
        """Test greeting with default name."""
        greeter = Greeter()
        assert greeter.greet() == "Hello, World!"

    def test_greet_custom_name(self) -> None:
        """Test greeting with custom name."""
        greeter = Greeter("Alice")
        assert greeter.greet() == "Hello, Alice!"

    def test_greet_formal(self) -> None:
        """Test formal greeting."""
        greeter = Greeter("Bob")
        assert greeter.greet_formal() == "Good day, Bob. It is a pleasure to meet you."

    def test_name_attribute(self) -> None:
        """Test that name attribute is set correctly."""
        greeter = Greeter("Charlie")
        assert greeter.name == "Charlie"


class TestGreetFunction:
    """Tests for the greet convenience function."""

    def test_greet_default(self) -> None:
        """Test greet function with default name."""
        assert greet() == "Hello, World!"

    def test_greet_with_name(self) -> None:
        """Test greet function with custom name."""
        assert greet("Python") == "Hello, Python!"


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Bob", "Hello, Bob!"),
        ("", "Hello, !"),
        ("World", "Hello, World!"),
    ],
)
def test_greet_parametrized(name: str, expected: str) -> None:
    """Test greet function with various inputs."""
    assert greet(name) == expected
