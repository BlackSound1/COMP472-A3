from pnt_state import PNTState


def main():
    state = PNTState(7, 0, [], 4)
    print(state)
    print("Static Board Eval:", state.static_board_evaluation())
    print("Possible token(s):", state.next_possible_tokens())
    print()

    # Interactive Testing
    while len(state.next_possible_tokens()) != 0:
        max_turn = [PNTState.taken_tokens]

        best_move = state.alpha_beta_search()

        print("Your best move is: " + str(best_move))

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
            print("Static Board Eval:", state.static_board_evaluation())
        print()


if __name__ == "__main__":
    main()
