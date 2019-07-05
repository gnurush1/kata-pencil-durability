from sys import argv

def main():
	testWriteFunctionality()
	testPencilDegradationWhereWeCantFinishASentence()
	testSharpenPencilAfterRunningOutOfDurabilityAndThenFinishingTheSentence()
	testSharpenPencilWithZeroLength()
	testEraseFunctionality()

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

def testSharpenPencilAfterRunningOutOfDurabilityAndThenFinishingTheSentence():
	correctOutput = "She sells sea shells down by the sea "
	durability = 12
	length = 2
	pencil = Pencil(durability, length)
	currentSentenceOnPaper = "She sells sea shells"
	sentenceToWrite = " down by the sea "

	writingOutput = pencil.write(currentSentenceOnPaper, sentenceToWrite)
	assert correctOutput == writingOutput
	assert pencil.durability == 0

	pencil.sharpen()
	assert pencil.durability == 12

	correctOutput = "She sells sea shells down by the sea shore"
	wordToFinishSentence = "shore"
	assert correctOutput == pencil.write(writingOutput, wordToFinishSentence)

def testSharpenPencilWithZeroLength():
	correctOutput = "She sells sea shells down by the sea "
	durability = 12
	length = 0
	pencil = Pencil(durability, length)
	currentSentenceOnPaper = "She sells sea shells"
	sentenceToWrite = " down by the sea "

	writingOutput = pencil.write(currentSentenceOnPaper, sentenceToWrite)
	assert correctOutput == writingOutput
	assert pencil.durability == 0

	pencil.sharpen()
	assert pencil.durability == 0

def testEraseFunctionality():
	correctOutput = "She sells sea shells down by the     shore"
	pencil = Pencil()
	originalText = "She sells sea shells down by the sea shore"
	textToErase = "sea"
	assert correctOutput == pencil.erase(originalText, textToErase)

class Pencil():
	def __init__(self, durability = 200, length = 5):
		self.maxDurability = durability
		self.durability = durability
		self.length = length

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

	def sharpen(self):
		if self.length != 0:
			self.durability = self.maxDurability
			self.length -= 1

	def erase(self, originalText, textToErase):
		startingIndexOfTextToErase = originalText.rfind(textToErase)
		listEquivalentOfOriginalText = list(originalText)
		if startingIndexOfTextToErase != -1:
			for i in range(startingIndexOfTextToErase, startingIndexOfTextToErase + len(textToErase)):
				listEquivalentOfOriginalText[i] = " "
		return "".join(listEquivalentOfOriginalText)

if __name__ == '__main__':
	main()