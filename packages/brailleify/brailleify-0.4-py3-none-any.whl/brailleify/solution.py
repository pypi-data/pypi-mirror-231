# Local Constants
BrailleAlphabet = [
    '100000', '110000', '100100', '100110', '100010',
    '110100', '110110', '110010', '010100', '010110',
    '101000', '111000', '101100', '101110', '101010',
    '111100', '111110', '111010', '011100', '011110',
    '100011', '111001', '010111', '101101', '101111', '101011'
]
Capitalize = '000001'
Space = '000000'

# Function definition
def solution(s):
    BrailleOutput = ''
    for char in s:
        if char == ' ':
            BrailleOutput += Space
        elif char.isupper():
            BrailleOutput += Capitalize
            BrailleOutput += BrailleAlphabet[ord(char.lower()) - ord('a')]
        else:
            BrailleOutput += BrailleAlphabet[ord(char) - ord('a')]
    return BrailleOutput