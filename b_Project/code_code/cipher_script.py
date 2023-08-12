
from abc import ABC, abstractmethod
import platform
import sys
import os

# File containing ChaCha20 algorithm with its special operations and functions specified in documentation

system = platform.system()
path = os.getcwd()
if system == 'Linux':
    sys.path.append(f"{path}/code_code")
elif system == 'Windows':
    sys.path.append(f"{path}\\code_code")
else:
    print("Unknown operating system")
    exit(1)

from cipher_operations import *
from logic_operations import XOR


class Cipher_plan(ABC):

    @abstractmethod
    def crypt(self, message, key: str) -> str:
        pass

# Class of ChaCha20 stream cipher
class Cipher(Cipher_plan):

    nonce_len = (2**96) - 1
    const = get_bin(904202222022003, 64)
    nonce_dict = ctAndNonce("code_code/ct_and_nonce.txt")

    # Encryption/Decryption method
    def crypt(self, user_input: str, key: str) -> str:

        dict_oper = Cipher.nonce_dict.get(user_input)

        if dict_oper is None: # Message as an input
            random.seed(f"{user_input}")
            nonce = get_bin(random.randint(0, Cipher.nonce_len), 96)
            input_bin_stream = CreateStream(user_input, 10)
        else: # Ciphertext as an input
            input_bin_stream = base64_decode(user_input)
            nonce = dict_oper

        key_bin_stream = ModifyToDefaultLen(CreateStream(key, 8))

        counter = 1
        block = Cipher.CreateBlock(key_bin_stream, nonce, counter)
        block = Cipher.ScrambleBlock(block)
        output_stream = ""
        while True:
            msg_stream_len = len(input_bin_stream)
            cur_block = ASCIIToBinStream(functools.reduce(operator.concat, block))
            if msg_stream_len <= len(cur_block):
                block_part = cur_block[:msg_stream_len]
                output_stream += XOR(input_bin_stream, block_part)
                break
            else:
                input_part = input_bin_stream[:512]
                input_bin_stream = input_bin_stream[512:]
                output_stream += XOR(input_part, cur_block)
                counter += 1
                block[3][0] = get_bin(counter, 32)
                block = Cipher.ScrambleBlock(block)

        if dict_oper is None: # Message as an input
            output = base64_encode(output_stream)
            print(f'Encrypting:\n\n{output}\n')

        else: # input is a ct
            output = MessageStreamToString(output_stream)
            print(f'Decrypting:\n\n{output}\n')


        if dict_oper is None:
            ct_nonce_file = open("code_code/ct_and_nonce.txt", "a")
            ct_nonce_file.write(f"\n{output}:{nonce}")
            ct_nonce_file.close()
            Cipher.nonce_dict[output] = nonce
        else:
            pass

        return


    # QR function, which is specified in Salsa20 algorithm structure (not in use but implemented because of similarity of ChaCha20 and Salsa20)
    @staticmethod
    def QRfunctionSalsa20(a: str, b: str, c: str, d: str):
        b = XOR(b, bit_move(AddTwoBinary(a, d), 7))
        c = XOR(c, bit_move(AddTwoBinary(b, a), 9))
        d = XOR(d, bit_move(AddTwoBinary(c, b), 13))
        a = XOR(a, bit_move(AddTwoBinary(d, c), 18))

        return a, b, c, d


    # QR Function, which is specified in ChaCha20 algorithm structure
    @staticmethod
    def QRfunctionChacha20(a: str, b: str, c: str, d: str):

        a, b = AddTwoBinary(a, b)
        d = XOR(d, a)
        d = bit_move(d, 16)

        c, d = AddTwoBinary(c, d)
        b = XOR(b, c)
        b = bit_move(b, 12)

        a, b = AddTwoBinary(a, b)
        d = XOR(d, a)
        d = bit_move(d, 8)

        c, d = AddTwoBinary(c, d)
        b = XOR(b, c)
        b = bit_move(b, 7)

        return a, b, c, d


    # Block of data scrambling ChaCha20 method 
    @staticmethod
    def ScrambleBlock(block: list):

        for i in range(10):
            for j in range(4):
                block[0][j], block[1][j], block[2][j], block[3][j] = Cipher.QRfunctionChacha20(block[0][j], block[1][j], block[2][j], block[3][j])
            for j in range(4):
                block[0][(j % 4)], block[1][((1 + j) % 4)], block[2][((2 + j) % 4)], block[3][((3 + j) % 4)] = Cipher.QRfunctionChacha20(block[0][(j % 4)], block[1][((1 + j) % 4)], block[2][((2 + j) % 4)], block[3][((3 + j) % 4)])
        return block


    # Method creating special ChaCha20 block
    @staticmethod
    def CreateBlock(key_bin: str, nonce: str, counter: int):
        const = Cipher.const
        counter_bin = get_bin(counter, 32)
        block = [[const[:32], const[32:], const[:32], const[32:]],
                 [key_bin[:32], key_bin[32:64], key_bin[64:96], key_bin[96:128]],
                 [key_bin[128:160], key_bin[160:192], key_bin[192:224], key_bin[224:256]],
                 [counter_bin, nonce[:32], nonce[32:64], nonce[64:96]]]
        return block

