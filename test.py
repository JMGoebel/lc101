'''Testing Grounds'''

class Clothing:
    '''This class represents wearable clothing'''
    def __init__(self, location, color, part):
        self.color = color
        self.location = location
        self.part = part
        self.wearing = False

    def put_on(self):
        '''Used to put on clothing'''
        if not self.wearing:
            print('You on put on the {} {}'.format(self.color, self.part))
            self.wearing = True
        else:
            print('You are already wearing the {} shirt'.format(self.color))

    def take_off(self):
        '''Used to remove clothing'''
        if self.wearing:
            print('You take off the {} shirt'.format(self.color))
            self.wearing = False
        else:
            print('You are are not wearing the {} shirt'.format(self.color))

shirt = Clothing('Torso', 'red', 'shirt')

shirt.put_on()
shirt.put_on()
shirt.take_off()
shirt.take_off()
