from utils import *
import random
import re
from pnt_state import PNTState
from typing import List


def main():
    run_given_test_cases()

    # run_random_test_cases()

    # play_the_game_with_a_test_state()


def run_algorithm_on_10_random_test_cases(states: List[PNTState]) -> None:
    """ Runs the alpha-beta algorithm on all 10 random test cases. Prints relevant data.

    :param states: The list of PNTStates
    :return: None
    """
    for i, state in enumerate(states):
        print(f"--- Test Case {i + 1} ---\n")
        generate_output(state, *state.alpha_beta_search(), True)


def create_random_test_cases() -> list:
    """ Creates 10 random test cases.

    For each potential test case, it randomly chooses how many tokens there are and creates a new default PNTState
    based on that. Then it chooses how many turns are to have passed. A small random number of turns is chosen to make
    sure it doesn't take too long. Then it essentially 'plays' a game lasting those number of turns. Each turn,
    if there's a winner already, just add the state to the list of states to return and continue.
    Then it randomly chooses a token to take obeying the game's rules. It will try to take that token if possible.
    After all turns have happened, it will add the PNTState to the list to return. Finally, as long as there are 10
    valid test cases, it will return them. If not, it will return [], which will cause this function to be called again.

    :return: The list of 10 test cases, which are each PNTStates
    """
    test_cases = []

    for i in range(10):
        n = random.randint(7, 10)  # Decide between 7 and 10 tokens

        state = PNTState(n, 0, [], 0)

        number_of_turns_taken = random.randint(1, 3)  # Decide a number of turns between 1 and 3 that have happened

        for turn in range(1, number_of_turns_taken + 1):
            if state.winner != 0:
                test_cases.append(state)
                continue

            choices = state.next_possible_tokens()

            choice = random.choice(choices)

            try:
                state.get_token(int(choice))
            except Exception as err:
                print(err)

            state.current_depth += 1

        test_cases.append(state)

    return test_cases if len(test_cases) == 10 else []


def read_input() -> list:
    """ Reads the given test cases from the relevant input file

    :return: The list of PNTStates that were read
    """
    directory = f'../input'
    states = []
    try:
        with open(f'{directory}/testcase.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.lstrip().rstrip('\n')
                state = to_pnt_state(line)
                if state:
                    states.append(state)
    except FileNotFoundError:
        print('no input file found\n')
    finally:
        return states


def to_pnt_state(string: str) -> PNTState:
    """ Converts a textual representation of a state into an actual PNTState

    :param string: The string version of a PNTState to convert into an actual PNTState
    :return: The PNTState that was converted from text
    """
    state = None
    match = re.search(r'(?:PNT Player|TakeTokens) (\d+) (\d+)( \d+(?: \d+)*)? (\d+)',
                      string)
    if match:
        taken_tokens = []
        if match.group(3) is not None:
            taken_tokens = to_int_list(match.group(3))
        state = PNTState(int(match.group(1)), int(match.group(2)), taken_tokens, int(match.group(4)))
    return state


def run_given_test_cases() -> None:
    """ Runs the test cases that were given in the assignment, or any test cases present in the input directory

    :return: None
    """
    states = read_input()

    for state in states:
        generate_output(state, *state.alpha_beta_search(), False)

    while True:
        string = input('Enter a command input or q to quit: ')

        if string == 'q':
            break

        state = to_pnt_state(string)

        if state is not None:
            generate_output(state, *state.alpha_beta_search(), False)


def play_the_game_with_a_test_state() -> None:
    """ Actually plays the PNT game with an initial state (7 total tokens, none taken, maximum depth)

    :return: None
    """
    state = PNTState(7, 0, [], 0)

    print('---Starting the game with---\n')
    print(state)
    print("Static Board Eval:", state.static_board_evaluation())
    print("Possible token(s):", state.next_possible_tokens())
    print()

    # Interactive Testing
    while len(state.next_possible_tokens()) != 0:
        print(f'---Player {state.next_player}\'s turn---\n')
        print("Taken:", state.taken_tokens)
        print("Possible token(s):", state.next_possible_tokens())
        print("Static Board Eval:", state.static_board_evaluation())

        best_move, val, _, _, _, _ = state.alpha_beta_search()

        print(f"Player {state.next_player}'s best move is: " + str(best_move))

        print(f"Player {state.next_player}'s best move val is: " + str(val))

        token = input(f"Player {state.next_player}: ")

        try:
            state.get_token(int(token))
        except Exception as err:
            print(err)

        if state.winner:
            print(f"Player {state.winner} wins")
        else:
            print("Taken:", state.taken_tokens)
            print("Possible token(s):", state.next_possible_tokens())
            print("Static Board Eval:", state.static_board_evaluation(), '\n')


def run_random_test_cases() -> None:
    """ Runs all 10 random test cases

    :return: None
    """
    print("--- CREATING RANDOM TEST CASES ---\n")

    states = None

    while states is None:
        states = create_random_test_cases()

        if len(states) != 10:
            states = None

    print("--- RUNNING ALPHA-BETA ON THOSE TEST CASES ---\n")

    run_algorithm_on_10_random_test_cases(states)


if __name__ == "__main__":
    main()
