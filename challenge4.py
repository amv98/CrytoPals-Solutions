import binascii

def xor(a, b):
    return bytes([i ^ b for i in a])

def find_message(s):
    messages = []
    for i in s:
        for j in range(0,255):
            messages.append(xor(i,j))
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
    space = lambda x:x == ord(' ') #ascii value for space
    return len([i for i in s if lower_case(i) or upper_case(i) or space(i)]) / len(s)

if __name__ == '__main__':
    lines = [binascii.unhexlify(i.strip()) for i in open('4.txt')]
    print(find_message(lines))
