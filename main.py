import sys
from tokenizer import Tokenizer

file_name = sys.argv[1]
tokenizer = Tokenizer(file_name)

token = tokenizer.getToken()
while token:
    print(" ", token, end = "")
    tokenizer.skipToken()
    token = tokenizer.getToken()
print()

# f = open(FILENAME, "r")
# line = f.readline()
