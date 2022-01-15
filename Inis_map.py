"""
def explore(input):
    return input * 2


def new_clans(input, *f):
    return input * 3

deck = [new_clans, explore]

print( [ e(2) for e in deck ])



class inis_deck():

    def __init__(self):
        self.name = ''
        self.type = ''
        self.cards = []


class card():

    def __init__(self):
        self.name = ''
        self.type = ''



# Messenger/MessengerIdiom.py

class Messenger:
    def __init__(self, **kwargs):
        self.__dict__ = kwargs

m = Messenger(info="some information", b=['a', 'list'])
m.more = 11
print m.info, m.b, m.more

"""

class testclass:

    def add_attributes(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


if __name__ == '__main__':
    d = { 'key1': 10, 'key2': 20, 'key3': 30}
    a = testclass()
    a.add_attributes( **d )
    print(dir(a))
    print(a.key1)



