import binascii
import base64

def hamming_distance(a, b):
	a = bin(int(binascii.hexlify(a),16))
	b = bin(int(binascii.hexlify(b),16))
	return sum(i != j for i, j in zip(a, b))

def xor(a, b):
    return bytes([i ^ b for i in a])

def find_key(s):
	messages = []
	for i in range(0, 255):
		messages.append((xor(s, i), i))
	max_value = 0
	for i in messages:
		print(i)
		temp = score(i[0])
		if temp > max_value:
			max_value = temp
			message = i
	return message[1]

def score(s):
    lower_case = lambda x:x in range(ord('a'), ord('a') + 26)
    upper_case = lambda x:x in range(ord('A'), ord('A') + 26)
    return len([i for i in s if lower_case(i) or upper_case(i)]) / len(s)

if __name__ == '__main__':
	a = bytes('this is a test','utf-8')
	b = bytes('wokka wokka!!!','utf-8')  
	#print(hamming_distance(a, b))
	lines = base64.b64decode(bytes(''.join(i for i in open('6.txt')),'utf-8'))
	#print(lines)
	min_value = 1000 
	for keysize in range(2, 41):
		value = 0
		for i in range(1,5):
			value += hamming_distance(lines[:i * keysize], lines[i * keysize:(i + 1) * keysize]) / keysize
		value /= 4
		if value < min_value:
			key_size = keysize
			min_value = value 
	#print(key_size)
	blocks = [lines[i: i + key_size] for i in range(0, len(lines), key_size)]
	key = ''
	for i in range(key_size):
		transposed_block = [block[i] for block in blocks if len(block) > i]
		key += chr(find_key(transposed_block))
		print(key)

	print(key)
