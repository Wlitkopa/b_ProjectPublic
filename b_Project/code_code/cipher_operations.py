import functools
import operator
import platform
import random
import sys
import os

system = platform.system()
path = os.getcwd()
if system == 'Linux':
    sys.path.append(f"{path}/code_code")
elif system == 'Windows':
    sys.path.append(f"{path}\\code_code")
else:
    print("Unknown operating system")
    exit(1)

from logic_operations import XOR



# Variables
key_default_len = 256
base64_encoding_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                         'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                         'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']


# Function returnig n 8-bit random values - not mine
def randomBytes(n: int):
    return bytes(random.getrandbits(8) for i in range(n))


# Function returning random number between 0-255 - not mine
def randomInt():
    return random.randint(0, 255)


# Function returning random number between 0-255, coded in binary system and padded to 8-bit num - not mine
def randomByteBin():
    return get_bin(random.randint(0, 255), 8)


# Function performing bit rotation
def bit_move(bit: str, n: int) -> str:
    bit = bit[n:] + bit[:n]
    return bit


# Chars array into ascii code array - not mine
def intoASCIIArray(message: str) -> list:
    int_array = []
    mesg_array = list(message)
    for i in mesg_array:
        int_array.append(ord(i))
    return int_array


# Ascii code array into chars array - not mine
def intoCharArray(message: list) -> list:
    mesg_char = []
    for i in message:
        mesg_char.append(chr(i))
    return mesg_char


# Function returning binary representation padded to n-bit - not mine
def get_bin(x, n):
    return format(x, 'b').zfill(n)


# Function converting binary string num into decimal value
def binaryToDecimal(binary: str) -> int:
    decimal = 0
    for i in range(len(binary)):
        cur_bit = binary[-(i + 1)]
        cur_bit = int(cur_bit)
        decimal += cur_bit * pow(2, i)
    return decimal


# Function converting ascii string into 8-bit portions - not mine
def ASCIIToBinChunks(message_list: list) -> list:
    binary = []
    for x in message_list:
        binary.append(get_bin(x, 8))
    return binary


# Function converting unicode string into 10-bit portions
def UnicodeToBinChunks(message_list: list) -> list:
    binary = []
    for x in message_list:
        binary.append(get_bin(x, 10))
    return binary


# Function converting ascii decimal values array (message) into binary string array of specified element binary length
def ToBinChunks(message_list: list, extention: int) -> list:
    binary = []
    for x in message_list:
        binary.append(get_bin(x, extention))
    return binary


# Function concatenating ASCII nums in binary string code array into one string - not mine
def ASCIIToBinStream(binary: list) -> str:
    binary_str = ""
    for x in binary:
        binary_str += x
    return binary_str


# Function converting bit stream into an array of blocks of specified length. If it is keystream that needs to be "chunked", then the third 
# argument needs to be set as "True". Moreover stream length needs to be multiplication of chunk length because of need to freely converting
# bit stream into chars
def StreamToChunks(bin_str: str, chunk_len: int, key_bool=False) -> list:
    key_chunks = []
    cur_index = 0

    if key_bool:
        stream_len = key_default_len
    else:
        stream_len = len(bin_str)

    if stream_len % chunk_len != 0:
        raise TypeError("Type proper chunk_len and key_bool")
    else:
        pass

    chunks_amount = int(stream_len / chunk_len)
    for i in range(chunks_amount):
        next_index = chunk_len * (i + 1)
        key_chunks.append(bin_str[cur_index:next_index])
        cur_index = next_index

    return key_chunks


# zmodyfikowanie klucza do długości 256 bitów - Przemek
# Function modyfying length of key to exactly 256 bits. In case of too little length, key is padded with 0s. In case of length that
# exeeds 256 bits key is decreased using 256 bit set using XOR and random function on each additional set of bits which helps in
# maintaing originality of key (collision prevention)
def ModifyToDefaultLen(bin_key_stream: str) -> str:
    random.seed("key")

    key_length = len(bin_key_stream)
    if key_length == key_default_len:
        return bin_key_stream
    elif key_length < key_default_len:
        diff = key_default_len - key_length
        for i in range(diff):
            bin_key_stream += "0"
        return bin_key_stream
    else:
        over_bits_len = key_length - key_default_len
        bin_properpart_stream = bin_key_stream[:key_default_len]
        key_chunks = StreamToChunks(bin_properpart_stream, 8, True)

        for i in range(over_bits_len):
            rand_bin = randomByteBin()
            cur_chunk_index = (i % 32)
            key_chunks[cur_chunk_index] = XOR(key_chunks[cur_chunk_index], rand_bin)

        bin_key_stream = ASCIIToBinStream(key_chunks)

        return bin_key_stream


# Function presenting key as bitstream, not in use
def CreateKeyStream(key: str) -> str:
    key_list_ascii = intoASCIIArray(key)
    key_bin_chunks = ASCIIToBinChunks(key_list_ascii)
    key_bin_stream = ASCIIToBinStream(key_bin_chunks)
    key_256_bit = ModifyToDefaultLen(key_bin_stream)
    return key_256_bit


# Function presenting message as bitstream, not in use
def CreateMessageStream(message: str) -> str:
    message_list_ascii = intoASCIIArray(message)
    message_bin_chunks = UnicodeToBinChunks(message_list_ascii)
    message_bin_stream = ASCIIToBinStream(message_bin_chunks)
    return message_bin_stream


# Function presenting any string as bitstream - Przemek
def CreateStream(string: str, extention: int) -> str:
    string_list_ascii = intoASCIIArray(string)
    string_bin_chunks = ToBinChunks(string_list_ascii, extention)
    string_bin_stream = ASCIIToBinStream(string_bin_chunks)
    return string_bin_stream


# Function converting message to array of binary string chunks, not in use
def MessageToBinChunk(message_bin_stream: str) -> list:
    message_bin_chunk = StreamToChunks(message_bin_stream, 10)
    return message_bin_chunk


# Function converting message to array of decimal unicode values, not in use
def MessageToUnicodeChunk(message_bin_chunk: list) -> list:
    message_unicode_chunk = []
    for x in message_bin_chunk:
        message_unicode_chunk.append(binaryToDecimal(x))
    return message_unicode_chunk


# # Function converting message to binary stream, not in use
def MessageBinToString(message_unicode_chunk: list) -> str:
    message_string = ""
    for letter in message_unicode_chunk:
        message_string += chr(letter)
    return message_string


# Function converting bitstream to message
def MessageStreamToString(message_bin_stream: str) -> str:
    message_bin_chunk = StreamToChunks(message_bin_stream, 10)
    message_string = ""
    for x in message_bin_chunk:
        message_string += chr(binaryToDecimal(x))
    return message_string


# Function coding in base64, using an base64_encoding_table array that is specified at the beggining of this file
def base64_encode(ct_bin_stream: str) -> str:
    len_ct_stream = len(ct_bin_stream)
    rest = len_ct_stream % 6
    if rest != 0:
        core = ct_bin_stream[:-rest]
        core_rest = ct_bin_stream[-rest:]
    else:
        core = ct_bin_stream
        core_rest = ''
    core_bin_chunk = StreamToChunks(core, 6)
    ct_string = ""
    for x in core_bin_chunk:
        ct_string += base64_encoding_table[binaryToDecimal(x)]
    ct_string += f"={core_rest}"
    return ct_string


# Function decoding from base64, using base64_encoding_table array
def base64_decode(ct_string: str) -> str:
    ct_parts = ct_string.split("=")
    ct_to_decode = ct_parts[0]
    ct_bin_stream = ""

    for letter in ct_to_decode:
        ct_bin_stream += get_bin(int(base64_encoding_table.index(letter)), 6)
    ct_bin_stream += ct_parts[1]

    return ct_bin_stream


# Function adding two binary string numbers, necessary in ChaCha20 algorithm
def AddTwoBinary(x, y):
    x = binaryToDecimal(x)
    y = binaryToDecimal(y)
    x = (x + y) / 2
    x = get_bin(int(x), 32)
    y = get_bin(int(y), 32)

    return x, y


# Function returning a dictionary object of ciphertextes and their noneces
def ctAndNonce(file: str) -> dict:
    ct_nonce_file = open(f"{file}", "r")
    lines = ct_nonce_file.read()
    if len(lines) == 0:
        dictionary = {}
        return dictionary

    ct_nonce_file.seek(0)
    dictionary = dict((pair.split(':') for pair in functools.reduce(operator.concat,
                                                                    (line.split('\n') for line in
                                                                     ct_nonce_file)) if len(pair) != 0))
    ct_nonce_file.close()

    return dictionary
