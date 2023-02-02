from CryptoFunc import HexBin, HexCodec, Cryptography, FileCryptoParser


def challengeOne():
    hex_String = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
    ChallengeOne = HexCodec(hex_String)
    base64 = ChallengeOne.hexToB64()
    print("Primeiro desafio:")
    print(base64)
    print(
        ChallengeOne.check_Equal(
            base64, "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
        )
    )


def challengeTwo():
    print("\nSegundo desafio")
    hex_String1 = "1c0111001f010100061a024b53535009181c"
    hex_String2 = "686974207468652062756c6c277320657965"
    expected_Result = "746865206b696420646f6e277420706c6179"
    hex_Worker = HexBin()
    string_One = HexCodec(hex_String1)
    string_Two = HexCodec(hex_String2)
    decodeOne = string_One.decoder()
    decodeTwo = string_Two.decoder()
    result = hex_Worker.binXor(decodeOne, decodeTwo)
    end_Result = hex_Worker.toHex(result)
    print(end_Result)


def challengeThree():
    print("\nTerceiro desafio")
    crypto_Text = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    Decypher = Cryptography(crypto_Text)
    Hexer = HexBin()
    candidates = Decypher.brute_Force(Hexer)
    print("Score:", candidates[0])
    print("Text:", candidates[1].decode().strip())
    print("Key:", candidates[2])


def challengeFour():
    print("\nQuarto desafio")
    filename = "4.txt"
    CypherText = FileCryptoParser(filename)
    candidate = CypherText.lineParsing()
    print("Score:", candidate[0])
    print("Text:", candidate[1].decode().strip())
    print("Key:", candidate[2])
