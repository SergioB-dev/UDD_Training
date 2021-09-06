

import Foundation

var filePth = Bundle.main.url(forResource: "test/sowpods", withExtension: ".txt")!

let sowArray = try! String(contentsOf: filePth).components(separatedBy: "\n")

let scores = [
    "a": 1,
    "b": 3,
    "c": 3,
    "d": 2,
    "e": 1,
    "f": 4,
    "g": 2,
    "h": 4,
    "i": 1,
    "j": 8,
    "k": 5,
    "l": 1,
    "m": 3,
    "n": 1,
    "o": 1,
    "p": 3,
    "q": 10,
    "r": 1,
    "s": 1,
    "t": 1,
    "u": 1,
    "v": 4,
    "w": 4,
    "x": 8,
    "y": 4,
    "z": 10
]



func createScrabbleWords(from words: [String],rack: String) -> (String, Int) {
    var possibleWords = [String]()
    var isValidWord = false
    var rackCharacters = [Character]()
    for char in rack {
        rackCharacters.append(char)
    }
    
    for word in words {
        var characterList = rackCharacters
        for char in word {
            if characterList.contains(char) {
                isValidWord = true
                let indexToRemove = characterList.firstIndex(of: char)
                characterList.remove(at: indexToRemove!)
            } else {
                isValidWord = false
                break
            }
        }
        if isValidWord {
            possibleWords.append(word)
        }
    }
    let scoreList = zip(possibleWords.map{ $0.scoreWord()}, possibleWords).map{($0, $1)}
    let highestScoringWord = scoreList.max(by: <)!
    return (highestScoringWord.1, highestScoringWord.0)
}

extension String {
    func scoreWord() -> Int {
        var chars = [Character]()
        for char in self {
            chars.append(char)
        }
        var score = 0
        for char in chars {
            score += scores[String(char).lowercased()]!
        }
        return score
    }
}

createScrabbleWords(from: sowArray, rack: "QZAAIE")

// Returns ("ZEA", 12)
