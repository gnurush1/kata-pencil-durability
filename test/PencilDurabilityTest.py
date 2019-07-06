from sys import argv

def main():
	testWriteFunctionality()
	testPencilDegradationWhereWeCantFinishASentence()
	testSharpenPencilAfterRunningOutOfDurabilityAndThenFinishingTheSentence()
	testSharpenPencilWithZeroLength()
	testEraseFunctionality()
	testEraserDurabilityWhereWeCantFinishErasingTheWord()

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

def testEraserDurabilityWhereWeCanEraseTheEntireWord():
	correctOutput = "She sells sea shells down by the     shore"
	pencil = Pencil()
	originalText = "She sells sea shells down by the sea shore"
	textToErase = "sea"
	assert correctOutput == pencil.erase(originalText, textToErase)
	assert pencil.eraserDurability == 97

def testEraserDurabilityWhereWeCantFinishErasingTheWord():
	correctOutput = "She sells sea shells down by the s   shore"
	leadDurability = 0
	pencilLength = 0
	eraserDurability = 2
	pencil = Pencil(leadDurability, pencilLength, eraserDurability)
	originalText = "She sells sea shells down by the sea shore"
	textToErase = "sea"
	assert correctOutput == pencil.erase(originalText, textToErase)
	assert pencil.eraserDurability == 0

def testEditWhereWeInsertOnionInTheWhiteSpaceGap():
	originalText = "An       a day keeps the doctor away"
	replacingWord = "onion"
	correctOutput = "An onion a day keeps the doctor away"
	replacingStartIndex = 4
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

def testEditWhereWeInsertArtichokeInTheWhiteSpaceGap():
	originalText = "An       a day keeps the doctor away"
	replacingWord = "artichoke"
	correctOutput = "An artich@k@ay keeps the doctor away"
	replacingStartIndex = 4
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

def testEditWhereTheWhiteSpaceGapIsAtTheEndButTheReplacingWordIsTooLongForTheSentence():
	originalText = "The doctor fears the      ."
	replacingWord = "artichoke"
	correctOutput = "The doctor fears the artic@"
	replacingStartIndex = 21
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

class Pencil():
	def __init__(self, durability = 200, length = 5, eraserDurability = 100):
		self.maxDurability = durability
		self.durability = durability
		self.length = length
		self.eraserDurability = eraserDurability

	def write(self, currentSentenceOnPaper, sentenceToWrite):
		sentenceToWriteBuffer = ""
		for i in range(0, len(sentenceToWrite)):
			character = self.decreaseLeadDurability(sentenceToWrite[i])
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
			for i in range(startingIndexOfTextToErase + len(textToErase) - 1, startingIndexOfTextToErase - 1, -1):
				if not listEquivalentOfOriginalText[i].isspace():
					if self.eraserDurability > 0:
						listEquivalentOfOriginalText[i] = " "
						self.eraserDurability -= 1
		return "".join(listEquivalentOfOriginalText)

	def edit(self, originalText, replacingWord, replacingStartIndex):
		listEquivalentOfReplacingWord = list(replacingWord)
		listEquivalentOfOriginalText = list(originalText)
		if (replacingStartIndex + len(replacingWord)) > len(originalText):
			endIndex = len(originalText)
		else:
			endIndex = replacingStartIndex + len(replacingWord)
		for i in range(replacingStartIndex, endIndex):
			if listEquivalentOfOriginalText[i].isspace():
				character = self.decreaseLeadDurability(listEquivalentOfReplacingWord[i - replacingStartIndex])
				listEquivalentOfOriginalText[i] = character
			else:
				listEquivalentOfOriginalText[i] = "@"
		return "".join(listEquivalentOfOriginalText)

	def decreaseLeadDurability(self, character):
		if not character.isspace():
			if character.isupper() and self.durability >= 2:
				self.durability -= 2
			elif character.islower() and self.durability >= 1:
				self.durability -= 1
			else:
				character = " "
		return character

if __name__ == '__main__':
	main()