from sys import argv

def main():
    test1()


def testWriteFunctionality():
    correctOutput = "She sells sea shells down by the sea shore"
    pencilDurability = PencilDurability()
    currentSentenceOnPaper = "She sells sea shells"
    sentenceToWrite = " down by the sea shore"

    assert correctOutput == pencilDurability.write(currentSentenceOnPaper, sentenceToWrite)

class PencilDurability():
    def write(self, currentSentenceOnPaper, sentenceToWrite):
        return currentSentenceOnPaper + sentenceToWrite

if __name__ == '__main__':
	main()