import sys
from tokenizer import Tokenizer

file_name = sys.argv[1]
tokenizer = Tokenizer(file_name)

while token:= tokenizer.getToken():
    print(token)
    tokenizer.skipToken()
