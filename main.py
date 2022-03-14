import sys
from tokenizer import TOKEN_MAP, Tokenizer
from parsetree import Prog

code = sys.argv[1]
input = sys.argv[1]
tokenizer = Tokenizer(code)

while token := tokenizer.getToken():
    print(token)

    tokenizer.skipToken()

prog = Prog()
