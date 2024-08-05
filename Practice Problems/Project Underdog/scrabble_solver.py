"""
This was a real interview question at Dropbox. Candidates who passed the interview would typically successfully implement Part 1 and then articulate an algorithm for Part 2 within 60 minutes, but they might not have time to implement Part 2.

Part 1

Write code that:

- Accepts a string (e.g. as an argument to a function, or as a command-line argument). This string represents your Scrabble “rack”.
- Prints out the words that can be made from the characters in that input string, along with their Scrabble scores, one word per line, in descending score order

Example input and output:

`$ python scrabble_cheater.py SPCQEIU  # Use any language you like.`
`17 piques`
`17 equips`
`16 quips`
`16 pique`
`16 equip`
`15 quip`
`…`

Resources:

- Word list
- Letter scores

Key points:

- Letters cannot be reused. For example, if your Scrabble rack is “ABCD”, you can make the word “CAB” but not the word “DAD”, because you only have one “D”.
- 
Part 2

Extend the script to handle blank tiles. When reading the input, the character _ can be used as a wildcard — it can represent any letter.

Wildcards do not count towards a word's score.


blanks - count how many there are
look through letters  in  rack
if yes, remove them
if blank decrement the count
keep track of tiles used to get score
"""