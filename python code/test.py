def hex_xor(hex1, hex2):
    if not all(char in "0123456789ABCDEFabcdef" for char in hex1+hex2):
        raise ValueError("hexa invalid")
hex_xor("1234567890abcdef","bcdefdg")