from sys import argv
from Pencil import Pencil

def main():
	print("Starting write test:")
	testWriteFunctionality()
	testWriteExtendedWithNewlineCharacters()
	print("Passed! Starting durability tests:")
	testPencilDegradationWhereWeCantFinishASentence()
	testDurabilityExtendedComplete()
	testDurabilityExtendedCompleteAfterSharpen()
	testDurabilityIncompleteAndCantSharpenAnymore()
	testSharpenPencilAfterRunningOutOfDurabilityAndThenFinishingTheSentence()
	testSharpenPencilWithZeroLength()
	print("Passed! Starting erase tests:")
	testEraseFunctionality()
	testEraserDurabilityWhereWeCantFinishErasingTheWord()
	testEraseExtendedComplete()
	print("Passed! Starting edit tests:")
	testEditWhereWeInsertOnionInTheWhiteSpaceGap()
	testEditWhereWeInsertArtichokeInTheWhiteSpaceGap()
	testEditWhereTheWhiteSpaceGapIsAtTheEndButTheReplacingWordIsTooLongForTheSentence()
	testEditExtendedCompleteAndReplaceEntireSentanceWithSpaces()
	print("All tests passed!")

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


if __name__ == '__main__':
	main()