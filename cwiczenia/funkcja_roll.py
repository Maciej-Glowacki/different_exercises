import random


def roll(dices, dice_type=6, mod=0):
    '''
    Roll dice simulation

    :param: nums of dices, type of dices and dice modificator
    :return: score of dice
    '''
    if dice_type not in (3, 4, 6, 8, 10, 12, 100):
        raise Exception("No such dice!")

    return sum(random.randint(1, dice_type) for i in range(dices)) + mod


if __name__ == '__main__':

    print(roll(2))

    print(roll(4, 10, 7))

    print(roll(1, 2))
