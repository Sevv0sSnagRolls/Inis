
def explore(input):
    return input * 2


def new_clans(input):
    return input * 3

deck = [new_clans, explore]

print( [ e(2) for e in deck ])



'''


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

'''

class A():

    def __int__(self):
        self.name = ''

class B(A):
    name = 'B'
    def test(self, input):
        return input*2


class C(A):
    name = 'C2'
    def test(self, input):
        return input * 3


D = [B(), C()]


