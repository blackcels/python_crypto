from heapq import heapify, heappush, heappop
class Node:
	def __init__(self, char, freq):
		self.freq = 0
		self.char = "a"
		self.char = char
		self.freq = freq
		self.left = None
		self.right = None

	def __lt__(self, other):
		if(other == None):
			return -1
		if(not isinstance(other, Node)):
			return -1
		return self.freq > other.freq

	def __str__(self):
		txt = str(self.freq)
		txt = str(self.char) + txt
		return str(txt)

class HuffmanCode:
	def __init__(self):
		self.myList = []
		self.huffcode = {}
		self.revHuffcode = {}
	
	def create_list(self, str):
		dico = {}
		for char in str:
			if char in dico:
				dico[char] += 1
			else:
				dico[char] = 1

		for (char, count) in dico.items():
			leaf = (Node(char, count))
			self.myList.append(leaf)
		self.myList = sorted(self.myList, key=lambda leaf: leaf.freq)
	
	def huffman_tree(self):
		while len(self.myList) >= 2:
			nod1 = heappop(self.myList)
			self.myList = sorted(self.myList, key=lambda leaf: leaf.freq)
			nod2 = heappop(self.myList)
			i = nod1.freq + nod2.freq
			mergedNod = Node(None, i)
			mergedNod.left = nod1
			mergedNod.right = nod2
			heappush(self.myList, mergedNod)
			self.myList = sorted(self.myList, key=lambda leaf: leaf.freq)
			

	def huffman_req(self, nod, code):
		if nod == None:
			return None

		if nod.char != None:
			self.huffcode[code] = nod.char
			self.revHuffcode[nod.char] = code
			

		self.huffman_req(nod.left, (code + "1"))
		self.huffman_req(nod.right, (code + "0"))

	def huffman_code(self):
		self.huffman_req(self.myList[0], "")
		print(self.huffcode)
	
	def encode(self, txt):
		codedText = ""
		for char in txt:
			codedText += self.revHuffcode[char]
		return codedText

	def decode(self, bit):
		decodedText = ""
		buff = ""
		for char in bit:
			buff += char
			if buff in self.huffcode:
				decodedText += self.huffcode[buff]
				buff = ''
		return decodedText

code = HuffmanCode()
code.create_list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
code.huffman_tree()
code.huffman_code()
print(code.encode("UARERHUM"))
print(code.decode(code.encode("UARERHUM")))