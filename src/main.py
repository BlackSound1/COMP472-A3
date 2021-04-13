from pnt_state import PNTState


def main():
    state = PNTState(7, 3, [1, 4, 2], 3)
    state.alpha_beta_search()

    # state = PNTState(3, 0, [], 0)
    # state.alpha_beta_search()
    #
    # state = PNTState(7, 1, [1], 2)
    # state.alpha_beta_search()
    #
    # state = PNTState(10, 3, [4, 2, 6], 4)
    # state.alpha_beta_search()

    # state = PNTState(10, 3, [4, 2, 6], 4)
    #
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
