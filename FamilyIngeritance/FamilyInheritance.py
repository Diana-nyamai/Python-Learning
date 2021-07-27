class Family:
    def __init__(self, name, complexion):
        self.name = name
        self.complexion = complexion
       

        if self.name == 'mwende':
            print('your name is same as your granny')
        else:
            print('welcome ')


class GrandKid(Family):
    def height(self):
        print('taller')

nem = input('enter your name: ')
complexs = input('enter your complexion: ')
g1 = GrandKid(nem, complexs)
print('your are: ' + g1.name + ' and your complexion is ' + g1.complexion + ' same as your grandmother but you are ')
g1.height()
       