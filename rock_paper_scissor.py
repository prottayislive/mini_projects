import random


def play():
    """ Making initial choice for user and pc"""
    print("Enter 'r' for rock, 'p' for paper, 's' for scissor")
    user = input("Choose your move: ").lower().strip()
    computer = random.choice(['r', 'p', 's'])
    print(f"You played {user} and computer played {computer}")

    # conditionals to determine winner or loser
    if user == computer:
        return 'tie'
    if is_win(user, computer):
        winner = "Congrats! You won!"
        return winner
    loser = "You Lost!"
    return loser


def is_win(player, opponent):
    """Finding winner through logic --> r>s, s>p , p>r"""
    # game mechanics to decide who wins
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (
            player == 'p' and opponent == 'r'):
        return True


print(play())
