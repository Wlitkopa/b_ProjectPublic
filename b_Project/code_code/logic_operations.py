

# Logic operations on bit strings

def XOR(bits1, bits2):
    xor_result = ""
    for index in range(len(bits1)):
        if bits1[index] == bits2[index]:
            xor_result += '0'
        else:
            xor_result += '1'
    return xor_result


def AND(bits1, bits2):
    and_result = ""
    for index in range(len(bits1)):
        if (bits1[index] == '1') and (bits2[index] == '1'):
            and_result += '1'
        else:
            and_result += '0'
    return and_result


def OR(bits1, bits2):
    or_result = ""
    for index in range(len(bits1)):
        if (bits1[index] == '0') and (bits2[index] == '0'):
            or_result += '0'
        else:
            or_result += '1'
    return or_result


def NEG(bits):
    neg_result = ""
    for index in range(len(bits)):
        if bits[index] == '0':
            neg_result += '1'
        else:
            neg_result += '0'
    return neg_result

