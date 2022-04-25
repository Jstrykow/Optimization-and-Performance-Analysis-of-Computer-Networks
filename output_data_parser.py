# outputa data
"""
<solution > ::= <link part><EOL><demand part>
<link part> ::= <number of links><EOL><link load list>
<number of links> ::= <integer>
<link load list> ::= <link load>[<EOL><link load>]*
<link load> ::= <link id> <number of signals> <number of fibers>
<link id> ::= <integer>
<number of signals> ::= <integer>
<number of fibers> ::= <integer>
<demand part> ::= <number of demands><EOL><demand flow list>
<number of demands> ::= <integer>
<demand flow list> ::= <demand flow>[<EOL><demand flow>]*
<demand flow> ::= <demand id> <number of demand paths><EOL><demand path flow 
list>
<demand id> ::= <integer>
<number of demand paths> ::= <integer>
<demand path flow list> ::= <demand path flow>[<EOL><demand path flow>]*
<demand path flow> ::= <path id> <path signals count>
<path id> ::= <integer>
<path signals count> ::= <integer>
"""