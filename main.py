from pep_tokenizer import tokenizer
from pep_parser import mini_parser
print("Pep Interpreter\n")

while(True):
    try:

        inp = input(">>> ")

        # tokenize
        tokens = tokenizer(inp)

        # parser
        print(tokens)
        output = mini_parser(tokens)

        if output:
            print(output)
       
    except KeyboardInterrupt:
        exit()
 

# # Symbol Table Tests:


# from pep_parser.symbol_table import SymbolTable
# SymbolTable.add_symbol("b",20)
# SymbolTable.add_symbol("c",30)
# SymbolTable.add_symbol("c",60)

# print(SymbolTable.find_symbol("c"))
# print(SymbolTable.symbols)
    

