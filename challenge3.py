import binascii

def xor(a, b):
    return bytes([i ^ b for i in a])

def find_message(s):
    messages = []
    for i in range(0,255):
        messages.append(xor(s,i))
    max_value = 0
    for i in messages:
        #print(i)
        if score(i) > max_value:
            max_value = score(i)
            message = i
    return message

def score(s):
    lower_case = lambda x:x in range(ord('a'), ord('a') + 26)
    upper_case = lambda x:x in range(ord('A'), ord('A') + 26)
    return len([i for i in s if lower_case(i) or upper_case(i)]) / len(s)

if __name__ == '__main__':
    s = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    s = binascii.unhexlify(s)
    print(find_message(s))
