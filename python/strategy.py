""" This module represents a strategy pattern """


class Strategy:
    """General interface for all strategies"""

    def execute(self, first_num: int, second_num: int) -> int:
        raise NotImplementedError


""" 
    Every concrete strategy implements 
    general interface by own way
"""


class SumStrategy(Strategy):
    def execute(self, first_num: int, second_num: int) -> int:
        return first_num + second_num


class SubStrategy(Strategy):
    def execute(self, first_num: int, second_num: int) -> int:
        return first_num + second_num


class MulStrategy(Strategy):
    def execute(self, first_num: int, second_num: int) -> int:
        return first_num * second_num


class DivStrategy(Strategy):
    def execute(self, first_num: int, second_num: int) -> int:
        return first_num // second_num


"""
    Context always works with strategies
    through general interface. It doesn't know
    what concrete strategy does he use
"""


class Context:
    __strategy: Strategy

    def set_strategy(self, strategy: Strategy):
        self.__strategy = strategy

    def execute_strategy(self, first_num: int, second_num: int):
        return self.__strategy.execute(first_num=first_num, second_num=second_num)


def main():
    """ Example of strategy
        1. User choose the strategy
        2. Then he inputs 2 numbers
        3. Create context object
        4. Give strategy class to context object
        5. Call execute method
    """
    strategies = {
        'sum': SumStrategy,
        'sub': SubStrategy,
        'div': DivStrategy,
        'mul': MulStrategy
    }
    command = input("Press the action ")
    if command not in strategies.keys():
        raise ValueError('No such action')
    strategy = strategies[command]()
    context = Context()
    context.set_strategy(strategy=strategy)
    nums = list(map(int, input().split()))
    result = context.execute_strategy(first_num=nums[0], second_num=nums[1])
    print(result)


if __name__ == '__main__':
    main()
