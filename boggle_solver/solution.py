class Trie:
    def __init__(self, letter = None):
        self.letter = letter
        self.children = {}
        self.leaf = False

    def add(self, word):
        if len(word):
            letter = word[0]
            word = word[1:]
            if letter not in self.children:
                self.children[letter] = Trie(letter)
            return self.children[letter].add(word)
        else:
            self.leaf = True
            return self

    def search(self, letter):
        if letter not in self.children:
            return None
        return self.children[letter]

def findWord(board, trie, validated, row, col, count, path = None, currLetter = None, word = None):
    letter = board[row][col]
    if path is None or currLetter is None or word is None:
        currLetter = trie.search(letter)
        path = [(row, col)]
        word = letter
    else:
        currLetter = currLetter.search(letter)
        path.append((row, col))
        word = word + letter
    
    if currLetter is None:
        return

    if currLetter.leaf:
        validated.add(word)

    for r in range(row-1, row+2):
        for c in range(col-1, col+2):
            if (r >= 0 and r< count and c>=0 and c<count and r != row and c != col and (r,c) not in path):
                findWord(board, trie, validated, r, c, count, path[:], currLetter, word[:])

def solve_boggle(count):
    board = []
    for i in range(0, count):
        board.append([])
        for _ in range(0, count):
            board[i].append(input().strip().upper())

    for row in board:
        print(row)

    trie = Trie()

    with open('dictionary-yawl.txt', 'r') as file:
        for line in file.readlines():
            word = line.rstrip().upper()
            trie.add(word)

    
    

    # set to store strings that match valid words
    validated = set()

    for row in range(0, count):
        for col in range(0, count):
            findWord(board, trie, validated, row, col, count)

    for word in sorted(validated):
        print(word)

solve_boggle(3)
