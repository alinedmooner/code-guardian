"""Domain entities - Clean Architecture example."""


class User:
    """User entity in the domain layer."""

    def __init__(self, user_id: str, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    def change_email(self, new_email: str) -> None:
        """Change user's email address."""
        # Domain logic here
        if "@" not in new_email:
            raise ValueError("Invalid email")
        self.email = new_email

