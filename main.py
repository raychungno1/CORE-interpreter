import sys
from tokenizer import Tokenizer
from parsetree import Prog, Input

code = sys.argv[1]
Tokenizer(code)  # initialize tokenizer

input_file = sys.argv[2]
Input.set_input_file(input_file)  # initialize input file

prog = Prog()
prog.parse()
print(5 * "-")
prog.print(0, 4 * " ")
print(5 * "-")
prog.execute()
