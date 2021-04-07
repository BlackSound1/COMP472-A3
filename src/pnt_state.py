from inspect import cleandoc
from utils import *


class PNTState():
    """Represents a pick numbered-tokens state"""

    def __init__(self, total_tokens, num_taken_tokens, taken_tokens, depth):
        self._total_tokens = total_tokens
        self._num_taken_tokens = num_taken_tokens
        self._taken_tokens = taken_tokens
        self._depth = depth

    def __str__(self):
        return cleandoc(f"""
        PNT State
        Total tokens: {self._total_tokens}
        Num taken token: {self._num_taken_tokens}
        Tokens taken: {self._taken_tokens}
        Depth: {self._depth}
        """)

    @property
    def total_tokens(self):
        return self._total_tokens

    @property
    def num_taken_tokens(self):
        return self._num_taken_tokens

    @property
    def taken_tokens(self):
        return self._taken_tokens

    @property
    def winner(self) -> int:
        if len(self.next_possible_tokens()) == 0 and self._num_taken_tokens > 0:
            return 2 - self._num_taken_tokens % 2
        return 0

    @property
    def next_player(self) -> int:
        if self._num_taken_tokens % 2 == 0:
            return 1
        return 2

    @property
    def last_taken_token(self) -> int:
        return self._taken_tokens[-1]

    def _take_token(self, token) -> int:
        self._num_taken_tokens += 1
        self._taken_tokens.append(token)
        return token

    def get_token(self, token) -> int:
        if token in self.next_possible_tokens():
            return self._take_token(token)
        raise ValueError("Invalid token.")

    def next_possible_tokens(self) -> list:
        # First move
        if self._num_taken_tokens == 0:
            return [token for token in range(1, (self._total_tokens + 1) // 2) 
            if token not in self._taken_tokens and 
            token % 2 == 1]
        # Not first move
        else:
            return [token for token in range(1, (self._total_tokens + 1)) 
            if token not in self._taken_tokens and 
            is_factor_or_multiple(token, self.last_taken_token)]

    def static_board_evaluation(self) -> float:
        if self.winner == 1:
            return 1.0
        elif self.winner == 2:
            return -1.0
        
        evaluation_value = 0
        if 1 not in self.taken_tokens:
            evaluation_value = 0
        elif self.last_taken_token == 1:
            if len(self.next_possible_tokens()) % 2 == 1:
                evaluation_value = 0.5
            else:
                evaluation_value = -0.5
        elif is_prime(self.last_taken_token):
            last_move = self.last_taken_token
            multiples_of_last_token = [token for token in self.next_possible_tokens() if token % last_move == 0]
            
            if len(multiples_of_last_token) % 2 == 0:
                evaluation_value = -0.7
            else:
                evaluation_value = 0.7
        else:
            last_move = self.last_taken_token
            possible_prime_factors = [token for token in self.next_possible_tokens() if last_move % token == 0 and is_prime(token)]
            largest_prime = max(possible_prime_factors)
            multiples_of_largest_prime = [token for token in self.next_possible_tokens() if token % largest_prime == 0]
            
            if len(multiples_of_largest_prime) % 2 == 0:
                evaluation_value = -0.6
            else:
                evaluation_value = 0.6
        
        return evaluation_value if self.next_player == 1 else -evaluation_value
