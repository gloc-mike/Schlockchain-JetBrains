class Message:
    """Response returned by hello."""

    def __init__(self, response: str):
        self.response = response


class MyDemo:
    """A *great* demo"""

    def __init__(self, name):
        self.name = name

    def hello(self, greeting: str) -> Message:
        """The canonical hello world example.

        A *longer* description with some **RST**.

        It uses :py:meth:`pauls_demo.Message` as a response.

        Args:
            name: The person to say hello to.
        Returns:
            Message: The greeting
        """
        message = Message(f"{greeting} {self.name}")
        return message
