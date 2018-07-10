import binascii
import base64

def hex_to_base64(s):
    return base64.b64encode(binascii.unhexlify(s))

if __name__ == '__main__':
    s = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    correct_answer = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    answer = hex_to_base64(s)
    print(answer)
    print(answer == correct_answer)