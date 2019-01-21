thisContext importBuiltIn: #Object.

"Lol, it's comment :)"
Object subclass: #RGBColor
    category: 'Colors'
    comment: 'Color in RGB palette'
    classContext: [
        initWithRed:andGreen:andBlue: [ :self :red :green :blue |
            ^ self new red: red; green: green; blue: blue; yourself.
        ]

        initBlack: [ :self |
            ^ self initWithRed: 0 andGreen: 0 andBlue: 0.
        ]

        initWhite: [ :self |
            ^ self initWithRed: 255 andGreen: 255 andBlue: 255
        ]
    ]
    instanceContext: [
        | red green blue |

        red [ :self | ^self.red ]
        red: [ :self :value | self.red := value ]

        green [ :self | ^self.green ]
        green: [ :self :value | self.green := value ]

        blue [ :self | ^self.blue ]
        blue: [ :self :value | self.blue := value ]

        inverted [ :self |
           ^ class initWhite - self.
        ]

        - other [ :self |
            <category: 'math'>
            ^ class initWithRed: ( red sub: other red) andGreen:
        ]

        "
        description [ :self |
            ^ '' join: { '{', 'red:', red string, 'green:', green string, 'blue:', blue string, '}' }
        ]
        "
    ].

a := 5.34.
b := $1.

c := True inverted equal: False.
c equal: True.

lol := [ :a :b |
    | test |
    test := [ :a | ^ a + 5 ].
    ^ test value: a + test value: b         "returns (test value: (a + (test value: b)))"
].

d := lol value: 5 value: 3