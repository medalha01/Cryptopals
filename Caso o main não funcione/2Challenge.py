import base64
import binascii

hex_String1 = "1c0111001f010100061a024b53535009181c"
hex_String2 = "686974207468652062756c6c277320657965"
expected_Result = "746865206b696420646f6e277420706c6179"


class HexBin:
    def __init__(self):
        self.init = True

    def binXor(self, bitsOne, bitsTwo):
        result = ""
        for iterator in range(0, len(bitsOne)):
            result += chr(bitsOne[iterator] ^ bitsTwo[iterator])
        return result.encode("ascii")

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


hex_Worker = HexBin()
string_One = HexSolver(hex_String1)
string_Two = HexSolver(hex_String2)
decodeOne = string_One.decoder()
decodeTwo = string_Two.decoder()
result = hex_Worker.binXor(decodeOne, decodeTwo)
end_Result = hex_Worker.toHex(result)
print(end_Result)
