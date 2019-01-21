from compiler.splexer import SPLexer

if __name__ == '__main__':
    lexer = SPLexer()

    with open('/Users/stalis/Develop/Projects/smallpython/src/examples/RGBColor.spy', 'r') as example:
        source = example.read()

    for token in lexer.tokenize(source):
        print(token)
