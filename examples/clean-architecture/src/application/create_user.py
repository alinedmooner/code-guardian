"""Application use cases - Clean Architecture example."""

# This is CORRECT - application can import from domain
from domain.user import User


class CreateUserUseCase:
    """Use case for creating a new user."""

    def execute(self, name: str, email: str) -> User:
        """Execute the use case."""
        user_id = self._generate_id()
        return User(user_id, name, email)

    def _generate_id(self) -> str:
        """Generate unique user ID."""
        import uuid
        return str(uuid.uuid4())

