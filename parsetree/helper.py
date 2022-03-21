from tokenizer import Tokenizer, TOKEN_MAP
from error import GrammarError

def check_and_skip_token(token, stmt_type):
    """Checks if the next token matches a given token type, raising an error otherwise."""

    if (Tokenizer.get_token() == TOKEN_MAP[token]):
            Tokenizer.skip_token()
    else:
        raise GrammarError(token, stmt_type)
