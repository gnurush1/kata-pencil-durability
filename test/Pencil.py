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
		if self.length > 0:
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
			elif not character.isspace() and self.durability >= 1:
				self.durability -= 1
			else:
				character = " "
		return character