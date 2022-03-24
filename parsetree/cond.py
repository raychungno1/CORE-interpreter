from error import GrammarError
from tokenizer import TOKEN_MAP, Tokenizer


class Cond:
    def __init__(self):
        self.alt_no = 1
        self.comp = None
        self.cond_1 = None
        self.cond_2 = None

    def parse(self):
        first_token = Tokenizer.get_token()
        if first_token == TOKEN_MAP["!"]:
            self.alt_no = 2
            Tokenizer.skip_token()
            self.cond_1 = Cond()
            self.cond_1.parse()

        elif first_token == TOKEN_MAP["["]:
            Tokenizer.skip_token()
            self.cond_1 = Cond()
            self.cond_1.parse()

            cond_token = Tokenizer.get_token()
            if cond_token == TOKEN_MAP["&&"]:
                self.alt_no = 3
            elif cond_token == TOKEN_MAP["||"]:
                self.alt_no = 4
            else:
                raise GrammarError("&& / ||", "Condition")
            
            Tokenizer.skip_token()
            self.cond_2 = Cond()
            self.cond_2.parse()

            Tokenizer.check_and_skip_token("]", "Condition")

        else:
            self.alt_no = 1
            from .comp import Comp
            self.comp = Comp()
            self.comp.parse()

    def print(self):
        if self.alt_no == 1:
            self.comp.print()

        elif self.alt_no == 2:
            print("!", end = "")
            self.cond_1.print()

        else:
            print("[", end = "")
            self.cond_1.print()
            
            if self.alt_no == 3:
                print(" && ", end = "")
            else:
                print(" || ", end = "")

            self.cond_2.print()
            print("]", end = "")

    def execute(self):
        return self
