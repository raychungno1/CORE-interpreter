class GrammarError(Exception):
    """Error raised for an invalid token"""

    def __init__(self, token, stmt_type):
        self.token = token
        self.stmt_type = stmt_type

    def __str__(self):
        return f"Expected \"{self.token}\" in statement \"{self.stmt_type}\""

class IdDuplicateError(Exception):
    """Error raised for a duplicate id during declaration"""

    def __init__(self, id_name):
        self.id_name = id_name

    def __str__(self):
        return f"Identifier \"{self.id_name}\"  already declared"

class IdMissingError(Exception):
    """Error raised for a missing id"""

    def __init__(self, id_name):
        self.id_name = id_name

    def __str__(self):
        return f"Identifier \"{self.id_name}\" was not declared"