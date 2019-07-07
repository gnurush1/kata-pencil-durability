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
	replacingStartIndex = 3
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

def testEditWhereWeInsertArtichokeInTheWhiteSpaceGap():
	originalText = "An       a day keeps the doctor away"
	replacingWord = "artichoke"
	correctOutput = "An artich@k@ay keeps the doctor away"
	replacingStartIndex = 3
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

def testEditWhereTheWhiteSpaceGapIsAtTheEndButTheReplacingWordIsTooLongForTheSentence():
	originalText = "The doctor fears the      ."
	replacingWord = "artichoke"
	correctOutput = "The doctor fears the artic@"
	replacingStartIndex = 21
	pencil = Pencil()
	assert correctOutput == pencil.edit(originalText, replacingWord, replacingStartIndex)

# Start of extended testing
def testDurabilityExtendedComplete():
	pencil = Pencil()
	assert pencil.durability == 200
	assert pencil.length == 5
	exampleText1 = "temp"
	exampleText2 = "temp2"
	exampleText3 = "temp3"
	out = pencil.write(exampleText1, exampleText2)
	assert pencil.durability == 195
	out = pencil.write(out, exampleText3)
	assert pencil.durability == 190
	pencil.sharpen()
	assert pencil.durability == 200
	assert pencil.length == 4

def testDurabilityExtendedCompleteAfterSharpen():
	pencil = Pencil(durability=8)
	assert pencil.durability == 8
	assert pencil.length == 5
	exampleText1 = "temp"
	exampleText2 = "temp2"
	exampleText3 = "temp3"
	out = pencil.write(exampleText1, exampleText2)
	assert pencil.durability == 3
	assert out == "temptemp2"
	out = pencil.write(out, exampleText3)
	assert pencil.durability == 0
	assert out == "temptemp2tem  "
	pencil.sharpen()
	assert pencil.durability == 8
	assert pencil.length == 4

def testDurabilityIncompleteAndCantSharpenAnymore():
	pencil = Pencil(durability=4, length=0)
	assert pencil.durability == 4
	assert pencil.length == 0
	exampleText1 = "temp"
	exampleText2 = "temp2"
	exampleText3 = "temp3"
	out = pencil.write(exampleText1, exampleText2)
	assert pencil.durability == 0
	assert out == "temptemp "
	pencil.sharpen()
	assert pencil.durability == 0
	out = pencil.write(out, exampleText3)
	assert out == "temptemp      "
	pencil.sharpen()
	assert pencil.durability == 0
	assert pencil.length == 0

def testWriteExtendedWithNewlineCharacters():
	exampleText1 = "I met a traveller from an antique land\n"
	exampleText2 = "Who said: Two vast and trunkless legs of stone\n"
	exampleText3 = "Stand in the desert..."
	correct = """I met a traveller from an antique land
Who said: Two vast and trunkless legs of stone
Stand in the desert..."""
	pencil = Pencil(durability=1000)
	out = pencil.write(exampleText1, exampleText2)
	out = pencil.write(out, exampleText3)
	assert correct == out

def testEraseExtendedComplete():
	exampleText1 = "The quick brown fox jumps over a lazy dog"
	correctOutput1 = "The quick brown     jumps over a lazy dog"
	exampleText2 = "Jived fox nymph grabs quick waltz."
	correctOutput2 = "Jived fox       grabs quick waltz."
	exampleText3 = "Cwm fjord bank glyphs vext quiz"
	correctOutput3 = "    fjord bank glyphs vext quiz"
	exampleText4 = "WHY WHy WhY Why wHY wHy whY why"
	correctOutput4 = "WHY WHy     Why wHY wHy whY why"
	exampleText5 = "no no no yes yes yes no no no yes yes yes"
	correctOutput5 = "no no no yes yes yes no no        yes yes"
	pencil = Pencil(eraserDurability=100)
	out1 = pencil.erase(exampleText1, "fox")
	out2 = pencil.erase(exampleText2, "nymph")
	out3 = pencil.erase(exampleText3, "Cwm")
	out4 = pencil.erase(exampleText4, "WhY")
	out5 = pencil.erase(exampleText5, "no yes")
	assert pencil.eraserDurability == 81
	assert correctOutput1 == out1
	assert correctOutput2 == out2
	assert correctOutput3 == out3
	assert correctOutput4 == out4
	assert correctOutput5 == out5

def testEditExtendedCompleteAndReplaceEntireSentanceWithSpaces():
	exampleText1 = "An       a day keeps the doctor away."
	correctOutput1 = "An apple a day keeps the doctor away."
	exampleText2 = exampleText1
	correctOutput2 = "An apples@u@@y keeps the doctor away."
	exampleText3 = correctOutput1
	correctOutput3 = "@@ @@@@@ @ @@@ @@@@@ @@@ @@@@@@ @@@@@"
	pencil = Pencil(durability=1000)
	out1 = pencil.edit(exampleText1, "apple", 3)
	out2 = pencil.edit(exampleText2, "applesauce", 3)
	out3 = pencil.edit(exampleText3, ' ' * len(exampleText1), 0)
	assert pencil.durability == 988
	assert correctOutput1 == out1
	assert correctOutput2 == out2
	assert correctOutput3 == out3


if __name__ == '__main__':
	main()