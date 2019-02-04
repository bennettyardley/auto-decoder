
def caesar(text, shift):
    atoz = string.ascii_lowercase
    shiftatoz = atoz[shift:] + atoz[:shift]
    table = str.maketrans(alphabet, shifted_alphabet)
    return text.translate(table)

def ASCIItoBin(text):
    return binascii.a2b_uu(text)

def BintoASCII(text):
    return binascii.b2a_uu(text)

def BintoBase(text):
    return binascii.b2a_base64(text)

def BasetoBin(text):
    return binascii.a2b_base64(text)

def BintoHex(text):
    return binascii.b2a_hex(text)

def Hextobin(text):
    return binascii.a2b_hex(text)

def main():
    dictionary = enchant.Dict("en_US")
    text = input("Enter Text: ")
    decodelist = []
    decodelist.append(text)
    for i in range(1,26):
        decodelist.append(caesar(text,i))
        i = i+1
    binText = ASCIItoBin(text)
    decodelist.append(BintoASCII(text))
    decodelist.append(BintoBase(binText))
    decodelist.append(BintoHex(binText))
    j = 0
    correct = []
    for decoded in decodelist:
        wordList = re.sub("[^\w]", " ",  decoded).split()
        if dictionary.check(random.choice(wordList)):
            correct.append(j)
        j = j + 1
    for correctOnes in correct:
        print(decodelist[correctOnes])
main()
