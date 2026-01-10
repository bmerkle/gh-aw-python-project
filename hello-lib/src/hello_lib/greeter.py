"""Greeter module containing the main functionality."""


class Greeter:
    """A simple greeter class that generates greeting messages."""

    def __init__(self, name: str = "World") -> None:
        """Initialize the Greeter with a name.

        Args:
            name: The name to greet. Defaults to "World".
        """
        self.name = name

    def greet(self) -> str:
        """Generate a greeting message.

        Returns:
            A greeting string.
        """
        return f"Hello, {self.name}!"

    def greet_formal(self) -> str:
        """Generate a formal greeting message.

        Returns:
            A formal greeting string.
        """
        return f"Good day, {self.name}. It is a pleasure to meet you."


def greet(name: str = "World") -> str:
    """Convenience function to generate a greeting.

    Args:
        name: The name to greet. Defaults to "World".

    Returns:
        A greeting string.
    """
    return Greeter(name).greet()
