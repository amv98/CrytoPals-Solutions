import binascii

def xor(a, b):
    return bytes([i ^ j for i,j in zip(a,b)])

def repeating_key_xor(a,key):
    return xor(a, key * (len(a) // len(key)) + key[:len(a) % len(key)])

if __name__ == '__main__':
    a = bytes('''Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal''',"utf-8")
    key = bytes('ICE','utf-8')
    correct_answer = b'''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'''
    answer = binascii.hexlify(repeating_key_xor(a, key))
    print(answer)
    print(answer == correct_answer)
