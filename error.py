class GrammarError(Exception):
    """Error raised for an invalid token"""

    def __init__(self, token, stmt_type):
        self.token = token
        self.stmt_type = stmt_type

    def __str__(self):
        return f"Expected \"{self.token}\" in statement \"{self.stmt_type}\""
