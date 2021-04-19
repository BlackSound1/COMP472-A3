import os

output_counter = 1


def is_factor_or_multiple(value, compared_value) -> bool:
    """ Checks if one given value is a factor or multiple of another given value

    :param value: One of the values to check
    :param compared_value: The other value
    :return: True or False
    """
    if value <= compared_value:
        return not bool(compared_value % value)
    else:
        return not bool(value % compared_value)


def is_prime(value) -> bool:
    """ Checks if a given value is prime

    :param value: The value to check
    :return: True or False
    """
    if value > 1:
        for i in range(2, value):
            if value % i == 0:
                break
        else:
            return True
    return False


def to_int_list(string: str):
    str_list = string.split()
    return list(map(int, str_list))


def generate_output(move: int, value: float, states_visited: [], states_evaluated: [],
                    depth_reached: int, random: bool):
    global output_counter

    # Nb of children nodes visited / Nb of parent nodes
    # Nb of nodes visited excluding root / Nb of nodes visited - Nb of leaf nodes
    if len(states_visited) == len(states_evaluated):
        branching_factor = len(states_visited) - 1
    else:
        branching_factor = (len(states_visited) - 1) / (len(states_visited) - len(states_evaluated))

    output_string = f'Move: {move}\n' \
                    f'Value: {value}\n' \
                    f'Number of Nodes Visited: {len(states_visited)}\n' \
                    f'Number of Nodes Evaluated: {len(states_evaluated)}\n' \
                    f'Max Depth Reached: {depth_reached}\n' \
                    f'Avg Effective Branching Factor: {branching_factor}\n'
    print(output_string)

    if random:
        directory = f'../output/random'
    else:
        directory = f'../output'

    if not os.path.isdir(directory):
        os.makedirs(directory)

    with open(f'{directory}/output{output_counter}.txt', 'wt') as file:
        file.write(output_string)
        file.close()
    output_counter += 1
