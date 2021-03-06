from discord.ext import commands


class ShuffleState():
    def __init__(self):
        self.array = []

    def shuffle(self):
        self.array = list(zip(*[group[i:] + group[:i] for i, group in enumerate(zip(*self.array))]))


def init_globals():
    global bot, shuffleState
    bot = commands.Bot(command_prefix=commands.when_mentioned)
    shuffleState = ShuffleState()
