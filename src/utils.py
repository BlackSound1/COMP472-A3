
def is_factor_or_multiple(value, compared_value) -> bool:
    if value <= compared_value:
        return not bool(compared_value % value)
    else:
        return not bool(value % compared_value)

def is_prime(value) -> bool:
    if value > 1:
        for i in range(2, value):
            if value % i == 0:
                break
        else:
            return True
    return False