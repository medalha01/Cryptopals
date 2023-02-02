import base64
import binascii

hex_String = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"


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


ChallengeOne = HexSolver(hex_String)
base64 = ChallengeOne.hexToB64()
print(
    ChallengeOne.check_Equal(
        base64, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
    )
)
