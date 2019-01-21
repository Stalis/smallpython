from compiler.lexer import Lexer
from compiler.parser import Parser


if __name__ == '__main__':
    lex = Lexer()
    par = Parser()

    # source = ''
    with open('examples/RGBColor.sp', 'r') as example:
        source = example.read()
    lexer = lex.get_lexer()
    # print([rule.re for rule in lexer.rules if rule.name is 'IDENT_KEYWORD'])

    tokens = lexer.lex(source)
    # tokens = lexer.lex("<category: 'math'>")
    for token in tokens:
        print(token)

    ast = par.parse(tokens)
    print(ast)
