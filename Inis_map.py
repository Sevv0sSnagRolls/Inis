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

    qty_sanctuaries = 12

    def __init__(self, name, style):
        self.name = name
        self.style = style

    def add_attributes(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def testcard(cls):
        return cls('john', 15)

    @classmethod
    def testcard2(cls):
        return cls('jSam', 35)

    @classmethod
    def sanctuaries(cls):
        if cls.qty_sanctuaries > 0:
            cls.qty_sanctuaries -= 1
        return

if __name__ == '__main__':
    a = testclass.testcard()
    print(a.name)
    b = testclass.testcard2()
    print(a.qty_sanctuaries)
    print(b.qty_sanctuaries)
    testclass.sanctuaries()
    print(a.qty_sanctuaries)
    print(b.qty_sanctuaries)



