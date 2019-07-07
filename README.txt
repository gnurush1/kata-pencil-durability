Pencil Durability Kata

A few notes on the implementation of the Pencil object:
	Due to there being some ambiguity caused by the project specifications, the following assuptions have been made:
		- All non-alphabetic characters will be treated as using up 1 point of durability of the pencil
		- All characters erased will remove 1 durability point from the eraser
		- You can sharpen a pencil at any point and restore lead durability to full, but will always lose 1 length in the process
		- When editing text, the user will give the function an index to start at for the word to replace. This index can be anywhere within the sentence, even where there is a non-whitespace character.
		- When editing text, the pencil lead degridation will still apply. However, collisions that result in the "@" character will not use up any durability points, since we have not written in anything until the user defines which character they want in it's place.

Language used to implement the Kata: Python 2.7

How to run the tests:
	Simply run "python <path to tests>" in the command line (without the quotes). Note that "python" is the name of the command I used for my machine, so it might be different depending on what name you gave the command to execute python files.