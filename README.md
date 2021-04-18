# COMP472-A3

## Link to repository: https://github.com/BlackSound1/COMP472-A3

There are 3 main ways to use this program. In the `main()` function, there are 3 functions. 
Each of these represents a different 'mode' the software can run in. To use each mode, make sure that
relevant function is uncommented. Comment-out the rest. It is also possible to have more than 1 function 
uncommented, but that can lead to messy output in the console. It is recommended to only use 1 mode at a time.

1. `run_given_test_cases()` Uncomment this function to initiate a game of PNT using each of the 3 test cases 
given in the assignment (or any test cases provided in the `input/testcase.txt` file). Each of these games will run 
automatically. From there, the user will be prompted to 'Enter a command input or q to quit'. the user may input 'q' 
to exit the program, or input a PNT State in the following format: `TakeTokens  7  3  1  4  2  3` or
`PNT Player 7 2 3 6 0`. Both of these options are available because the instructions, at various times, use 
both notations for valid inputs.

2. `run_random_test_cases()` Uncomment this function to create and run 10 random test cases, as specified in the 
assignment. This is simpler as it does not run full games on these test cases, but rather, just applies the alpha-beta 
algorithm on them. These test cases are not truly random, they are created in such a way as to be states that are
actually possible to reach in the game. In other words, the function is 'random' in a way that still obeys the rules.
However, other than that, at every point a choice can be made, the computer makes 
a random choice.

3. `play_the_game_with_a_test_state()` Uncomment this function to play a full game of PNT starting from the default 
beginning state. This state has 7 possible tokens, with none taken yet and a maximum depth of infinity 
(represented by 0, as specified in the assignment).
   
Special Note: This software makes use of the `os.makedirs()` method. According to official Python 3 documentation 
(found here: https://docs.python.org/3/library/os.html):
> `makedirs()` will become confused if the path elements to create include `pardir` (eg. “..” on UNIX systems).

This software does indeed use the `..` character sequence to shorten path names. If this is a problem on your system,
it is advisable to replace these relative path names with absolute path names.
Of special importance is the `directory` variable in the `generate_output()` function definition in `utils.py`,
as it is this `directory` variable which directly interacts with `os.makedirs()`.
