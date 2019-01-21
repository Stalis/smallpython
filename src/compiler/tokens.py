class Token:
    def __init__(self, name: str, regex: str):
        self.name = name
        self.regex = regex


r_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
r_KW = r_ID + r':'

r_CHAR = r'\S'
r_OPCHAR = r'[\!\@\#\$\%\^\&\*\-\+\=\~\/\?\<\>\,\;\|\‘\\]'

r_SQ_STRING = r"\'(\\\'|[^\'])*\'"
r_DQ_STRING = r'\"(\\\"|[^\"])*\"'
r_BQ_STRING = r'\`(\\\`|[^\`])*\`'

r_BIN_DIGIT = r'[0-1]'
r_OCT_DIGIT = r'[0-7]'
r_DEC_DIGIT = r'[0-9]'
r_HEX_DIGIT = r'[0-9A-Za-z]'

r_INTEGER = r'\-?' + r_DEC_DIGIT + r'+'
r_FLOAT = r'\-?' + r_DEC_DIGIT + r'*\.' + r_INTEGER

tokens = [
    Token('KEYWORD_SELF', 'self'),
    Token('KEYWORD_SUPER', 'super'),
    Token('KEYWORD_NIL', 'nil'),
    Token('KEYWORD_THIS_CONTEXT', 'thisContext'),
    Token('KEYWORD_TRUE', 'True'),
    Token('KEYWORD_FALSE', 'False'),

    Token('LITERAL_HEX', r'0[xX]' + r_HEX_DIGIT + r'+'),
    Token('LITERAL_OCT', r'0[oO]' + r_OCT_DIGIT + r'+'),
    Token('LITERAL_BIN', r'0[bB]' + r_BIN_DIGIT + r'+'),
    Token('LITERAL_FLOAT', r_FLOAT),
    Token('LITERAL_INTEGER', r_INTEGER),
    Token('LITERAL_STRING', r_SQ_STRING),
    Token('LITERAL_COMMENT', r_DQ_STRING),
    Token('LITERAL_CHAR', r'\$' + r_CHAR),

    Token('IDENT_SYMBOL_KW_SELECTOR', r'#(' + r_KW + r')+'),
    Token('IDENT_SYMBOL_OP_SELECTOR', r'#(' + r_OPCHAR + r')+'),
    Token('IDENT_SYMBOL_UN_SELECTOR', r'#' + r_ID),
    Token('IDENT_KEYWORD', r_ID + r':'),
    Token('IDENT_INPUT_ARG', r':' + r_ID),
    Token('IDENT_NAME', r_ID),

    Token('OP_RETURN', r'\^'),
    Token('OP_ASSIGNMENT', r':='),

    Token('PARENT_OPEN', r'\('),
    Token('PARENT_CLOSE', r'\)'),

    Token('BLOCK_OPEN', r'\['),
    Token('BLOCK_CLOSE', r'\]'),

    Token('DICT_OPEN', r'\#\{'),
    Token('ARRAY_OPEN', r'\{'),
    Token('ARRAY_CLOSE', r'\}'),

    Token('DELIM_LESS', r'\<'),
    Token('DELIM_GREATER', r'\>'),

    Token('DELIM_COLON', r'\:'),
    Token('DELIM_SEMICOLON', r'\;'),
    Token('DELIM_PIPE', r'\|'),
    Token('DELIM_COMMA', r'\.'),
    Token('DELIM_PERIOD', r'\,'),
    Token('DELIM_NEWLINE', r'\n+'),

    Token('OP_CUSTOM', r_OPCHAR + r'+'),
]

ignore_regex = r'[^\S\n]+'
