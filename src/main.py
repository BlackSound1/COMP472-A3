from pnt_state import PNTState
from utils import *


def read_input() -> list:
    """ Reads the given test cases in the input directory

    :return: The PNTStates
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
                    print(state)
                    print()
                    states.append(state)
    except FileNotFoundError:
        print('no input file found\n')
    finally:
        return states


def to_pnt_state(string: str) -> PNTState:
    """ Converts a given string into a PNTState

    :param string: The string to convert
    :return: The PNTState
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


def main():
    # states = [PNTState(3, 0, [], 0), PNTState(7, 1, [1], 2), PNTState(10, 3, [4, 2, 6], 4), PNTState(7, 3, [1, 4, 2], 3)]
    states = read_input()
    for state in states:
        move, value, states_visited, states_evaluated, depth_reached = state.alpha_beta_search()
        generate_output(move, value, states_visited, states_evaluated, depth_reached)

    while True:
        string = input('Enter a command input or q to quit: ')
        if string == 'q':
            break
        state = to_pnt_state(string)
        if state is not None:
            move, value, states_visited, states_evaluated, depth_reached = state.alpha_beta_search()
            generate_output(move, value, states_visited, states_evaluated, depth_reached)

    # print('---Starting the game with---\n')
    # print(state)
    # print("Static Board Eval:", state.static_board_evaluation())
    # print("Possible token(s):", state.next_possible_tokens())
    # print()
    #
    # # Interactive Testing
    # while len(state.next_possible_tokens()) != 0:
    #     print(f'---Player {state.next_player}\'s turn---\n')
    #     print("Taken:", state.taken_tokens)
    #     print("Possible token(s):", state.next_possible_tokens())
    #     print("Static Board Eval:", state.static_board_evaluation())
    #
    #     max_turn = [PNTState.taken_tokens]
    #
    #     val, best_move = state.alpha_beta_search()
    #
    #     print(f"Player {state.next_player}'s best move is: " + str(best_move))
    #
    #     print(f"Player {state.next_player}'s best move val is: " + str(val))
    #
    #     token = input(f"Player {state.next_player}: ")
    #     try:
    #         state.get_token(int(token))
    #     except Exception as err:
    #         print(err)
    #
    #     if state.winner:
    #         print(f"Player {state.winner} wins")
    #     else:
    #         print("Taken:", state.taken_tokens)
    #         print("Possible token(s):", state.next_possible_tokens())
    #         print("Static Board Eval:", state.static_board_evaluation(), '\n')


if __name__ == "__main__":
    main()
