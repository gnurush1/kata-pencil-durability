from sys import argv

def main():
	testWriteFunctionality()
	testPencilDegradationWhereWeCantFinishASentence()

def testWriteFunctionality():
	correctOutput = "She sells sea shells down by the sea shore"
	pencil = Pencil()
	currentSentenceOnPaper = "She sells sea shells"
	sentenceToWrite = " down by the sea shore"

	assert correctOutput == pencil.write(currentSentenceOnPaper, sentenceToWrite)

def testPencilDegradationWhereWeCantFinishASentence():
	correctOutput = "She sells sea shells down by the sea      "
	durability = 12
	pencil = Pencil(durability)
	currentSentenceOnPaper = "She sells sea shells"
	sentenceToWrite = " down by the sea shore"
	
	assert correctOutput == pencil.write(currentSentenceOnPaper, sentenceToWrite)

class Pencil():
	def __init__(self, durability = 200):
		self.durability = durability

	def write(self, currentSentenceOnPaper, sentenceToWrite):
		sentenceToWriteBuffer = ""
		for i in range(0, len(sentenceToWrite)):
			character = sentenceToWrite[i]
			if not character.isspace():
				if character.isupper() and self.durability >= 2:
					self.durability -= 2
				elif character.islower() and self.durability >= 1:
					self.durability -= 1
				else:
					character = " "
			sentenceToWriteBuffer += character
		return currentSentenceOnPaper + sentenceToWriteBuffer

if __name__ == '__main__':
	main()