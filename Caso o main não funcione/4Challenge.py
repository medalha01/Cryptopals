import base64
import binascii

### 1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
class Cryptography:
    def __init__(self, passphrase):
        self.passphrase = bytes.fromhex(passphrase)
        ### https://en.wikipedia.org/wiki/Letter_frequency
        self.char_Frequency_Dictionary = {
            "a": 0.082,
            "b": 0.015,
            "c": 0.029,
            "d": 0.043,
            "e": 0.13,
            "f": 0.022,
            "g": 0.02,
            "h": 0.06,
            "i": 0.07,
            "j": 0.00015,
            "k": 0.00077,
            "l": 0.04,
            "m": 0.023,
            "n": 0.067,
            "o": 0.075,
            "p": 0.02,
            "q": 0.0001,
            "r": 0.06,
            "s": 0.063,
            "t": 0.091,
            "u": 0.028,
            "v": 0.01,
            "w": 0.02,
            "x": 0.0015,
            "y": 0.02,
            "z": 0.00074,
            " ": 0.13,
        }
        self.first_Char_Frequency = {
            "a": 0.117,
            "b": 0.04,
            "c": 0.05,
            "d": 0.03,
            "e": 0.028,
            "f": 0.05,
            "g": 0.016,
            "h": 0.042,
            "i": 0.073,
            "j": 0.0051,
            "k": 0.0085,
            "l": 0.024,
            "m": 0.038,
            "n": 0.023,
            "o": 0.076,
            "p": 0.043,
            "q": 0.0022,
            "r": 0.028,
            "s": 0.067,
            "t": 0.16,
            "u": 0.012,
            "v": 0.082,
            "w": 0.00045,
            "x": 0.055,
            "y": 0.076,
            "z": 0.00045,
            " ": 0.005,
        }
        ###### https://math.wvu.edu/~hdiamond/Math222F17/Sigurd_et_al-2004-Studia_Linguistica.pdf
        self.words_Lenght_Frequency = {
            1: 0.0316,
            2: 0.16,
            3: 0.22,
            4: 0.15,
            5: 0.10,
            6: 0.08,
            7: 0.07,
            8: 0.05,
            9: 0.03,
            10: 0.03,
        }

    def score_Tool(self, text):
        score = 0
        switch = True
        lenghtCounter = 0
        for byte in text:
            character = chr(byte).lower()
            if switch == False:
                score += self.char_Frequency_Dictionary.get(character, 0)
            else:
                score += self.first_Char_Frequency.get(character, 0)
                switch = False
            if character == " ":
                score += self.words_Lenght_Frequency.get(lenghtCounter, 0)
                lenghtCounter = 0
            else:
                lenghtCounter += 1
        return score

    def brute_Force(self, HexBin):
        possible_canditates = []
        actual_Score = 0

        for candidate in range(256):
            text = HexBin.binXorSingleChar(self.passphrase, candidate)
            score = self.score_Tool(text)
            if score > actual_Score:
                possible_canditates = list([score, text, candidate])
                actual_Score = score

        return possible_canditates


class HexBin:
    def __init__(self):
        self.init = True

    def binXor(self, bitsOne, bitsTwo):
        result = ""
        for iterator in range(0, len(bitsOne)):
            result += chr(bitsOne[iterator] ^ bitsTwo[iterator])
        return result.encode("ascii")

    def binXorSingleChar(self, bitsOne, char):
        result = b""
        for cher in bitsOne:
            result += bytes([cher ^ char])
        return result

    def toHex(self, value):
        valuePos = binascii.hexlify(value)
        return valuePos


class HexSolver:
    def __init__(self, hex_str):
        self.hex_str = hex_str

    def decoder(self):
        decode_String = binascii.unhexlify(self.hex_str)
        return decode_String

    def encoder(self, decode_String):
        Encoded64 = base64.b64encode(decode_String).decode("ascii")
        return Encoded64

    def hexToB64(self):
        decode_String = self.decoder()
        Encoded64 = self.encoder(decode_String)
        return Encoded64

    def check_Equal(self, Encoded64, Objetivo):
        return Encoded64 == Objetivo


class FileCryptoParser:
    def __init__(self, filename):
        self.filename = filename

    def lineParsing(self):
        highscore = 0
        candidate = 0
        for line in open(self.filename):
            text = line.strip()
            Decypher = Cryptography(text)
            Hexer = HexBin()
            candidates = Decypher.brute_Force(Hexer)
            if candidates[0] > highscore:
                candidate = candidates
                highscore = candidate[0]
        return candidate


CypherText = FileCryptoParser("4.txt")
candidate = CypherText.lineParsing()
print(candidate[0])
print(candidate[1])
print(candidate[2])
