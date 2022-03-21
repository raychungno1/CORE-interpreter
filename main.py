import sys
from tokenizer import TOKEN_MAP, Tokenizer
from parsetree import prog
from error import GrammarError

code = sys.argv[1]
input_file = sys.argv[2]
Tokenizer(code, input_file)  # initialize tokenizer

# while token := Tokenizer.get_token():
#     print(token, end=" ")
#     Tokenizer.skip_token()
# print()
# prog = Prog()
# prog.parse().print().execute()
