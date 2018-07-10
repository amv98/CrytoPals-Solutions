import binascii

def xor(a, b):
    return binascii.hexlify(bytes([i ^ j for i, j in zip(a, b)]))

if __name__ == '__main__':
    a = '1c0111001f010100061a024b53535009181c'
    b= '686974207468652062756c6c277320657965'
    correct_answer = b'746865206b696420646f6e277420706c6179'
    a, b = binascii.unhexlify(a), binascii.unhexlify(b)
    answer = xor(a, b)
    print(answer)
    print(answer == correct_answer)
