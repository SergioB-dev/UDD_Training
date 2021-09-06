# Word Solver

## Part 1

Write some code that:
Takes a 7-character string (either as a command-line argument or as an argument to a function)
Prints out the words that can be made from those characters, along with their Scrabble scores, one word per line, in descending score order

## Example input and output:

$ python scrabble_cheater.py 

SPCQEIU  

- 17 piques
- 17 equips
- 16 quips
- 16 pique
- 16 equip
- 15 quip


**Resources:**
[Word list](https://www.dropbox.com/s/qkg62nkh483g635/sowpods.txt?dl=0)
[Letter scores](https://www.dropbox.com/s/talrnaxaftbb1rz/letter_scores.txt?dl=0)
Part 2

Extend the script to handle blank tiles. When reading the input, the character _ can be used as a wildcard — it can represent any letter.

Wildcards do not count towards a word's score.
