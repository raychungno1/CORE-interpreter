from error import GrammarError
from tokenizer import TOKEN_MAP, Tokenizer


class Comp:
    def __init__(self):
        self.op_1 = None
        self.comp_op = None
        self.op_2 = None

    def parse(self):
        Tokenizer.check_and_skip_token("(", "Comparison")

        from .op import Op
        self.op_1 = Op()
        self.op_1.parse()

        if TOKEN_MAP[Tokenizer.get_token()] in ["!=", "==", "<", ">", "<=", ">="]:
            self.comp_op = Tokenizer.get_token()
            Tokenizer.skip_token()
        else:
            raise GrammarError("!= / == / < / > / <= / >=", "Comparison")

        self.op_2 = Op()
        self.op_2.parse()
        
        Tokenizer.check_and_skip_token(")", "Comparison")

    def print(self):
        print("(", end = "")
        self.op_1.print()
        print(f" {TOKEN_MAP[self.comp_op]} ", end = "")
        self.op_2.print()
        print(")", end = "")
        return self

    def execute(self):
        return self
