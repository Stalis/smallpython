Object subclass: #Token
    classContext: [
        | :self |

        initWithName: name andRegex: regex [
            ^ self new name: name; regex: regex; yourself
        ]

        #initWithName:andRegex: := [
            | :name :regex |
            ^ self new name: name; regex: regex; yourself
        ]

        initDefault [
            ^ initWithName: '' andRegex: ''
        ]
    ]
    instanceContext: [ | :self name regex | ]


| tokens tokenDict |
tokens = {
    Token new name: 'KEYWORD_SELF'; regex: 'self'; yourself,
    Token new name: 'KEYWORD_NIL'; regex: 'nil'; yourself,
}

tokenDict = #{
    'KEYWORD_SELF' -> 'self',
    'KEYWORD_NIL' -> 'nil',
}

getTokenNames [
    ^tokens map: [ :tok | ^tok name ]
]