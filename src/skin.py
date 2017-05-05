# Author: Steven Bird <stevenbird1@gmail.com>
# Date: 2017-05-04

"""
Bininj Kunwok skin database.
"""

# Skins are encoded as matrimoiety (left, right), gender, and generation number.

MALE = 'm'
FEMALE = 'f'

LEFT = 'l'
RIGHT = 'r'

flip = {
    LEFT: RIGHT,
    RIGHT: LEFT,
    MALE: FEMALE,
    FEMALE: MALE,
    '1': '3',
    '2': '4',
    '3': '1',
    '4': '2'
}

increase = {'1': '2', '2': '3', '3': '4', '4': '1'}
decrease = {'1': '4', '2': '1', '3': '2', '4': '3'}


class Skin:
    def __init__(self, code):
        self.code = code
        self.matrimoiety, self.gender, self.number = tuple(code)

    def __repr__(self):
        return self.__class__.__name__ + "('" + self.matrimoiety + self.gender + self.number + "')"

    def __str__(self):
        raise NotImplementedError

    # gender tests
    def f(self):
        return self.gender == FEMALE
    def m(self):
        return self.gender == MALE

    # patrimoiety tests
    def duwa(self):
        return self.number in "13"
    def yirridjdja(self):
        return self.number in "24"

    # find the mother
    def M(self):
        return self.__class__(self.matrimoiety + FEMALE + decrease[self.number])

    # woman's daughter
    def fD(self):
        assert self.f()
        return self.__class__(self.matrimoiety + FEMALE + increase[self.number])

    # brother
    def B1(self):
        return self.__class__(self.matrimoiety + MALE + self.number)
    def B2(self):
        return self.__class__(self.matrimoiety + MALE + increase[increase[self.number]])

    # sister
    def Z1(self):
        return self.__class__(self.matrimoiety + FEMALE + self.number)
    def Z2(self):
        return self.__class__(self.matrimoiety + FEMALE + increase[increase[self.number]])

    # spouse
    # NB we're not modelling first and second choices here
    def SP1(self):
        return self.__class__(flip[self.matrimoiety] +
                              flip[self.gender] +
                              self.number)
    def SP2(self):
        return self.__class__(flip[self.matrimoiety] +
                              flip[self.gender] +
                              flip[self.number])

    # father
    def F1(self):
        return self.M().SP1()
    def F2(self):
        return self.M().SP2()

    # male daughter
    def mD1(self):
        assert self.m()
        return self.SP1().fD()
    def mD2(self):
        assert self.m()
        return self.SP2().fD()



class WesternSkin(Skin):
    NAME = {
        'lm1': 'nabulanj',         'lf1': 'ngalbulanj',
        'lm2': 'nawamud',          'lf2': 'ngalwamud',
        'lm3': 'nangarridj',       'lf3': 'ngalngarridj',
        'lm4': 'nakamarrang',      'lf4': 'ngalkamarrang',
        'rm1': 'nawakadj',         'rf1': 'ngalwakadj',
        'rm2': 'nabangardi',       'rf2': 'ngalbangardi',
        'rm3': 'nakangila',        'rf3': 'ngalkangila',
        'rm4': 'nakodjok',         'rf4': 'ngalkodjok'
    }

    def __str__(self):
        return self.NAME[self.code]
       
class EasternSkin(Skin):
    NAME = {
        'lm1': 'kela',             'lf1': 'kalidjan',
        'lm2': 'kodjok',           'lf2': 'kodjan',
        'lm3': 'balang',           'lf3': 'belinj',
        'lm4': 'bangardi',         'lf4': 'bangardidjan',
        'rm1': 'ngarridj',         'rf1': 'ngarridjdjan',
        'rm2': 'kamarrang',        'rf2': 'kamanj',
        'rm3': 'bulanj',           'rf3': 'bulanjdjan',
        'rm4': 'wamud',            'rf4': 'wamuddjan'
    }

    def __str__(self):
        return self.NAME[self.code]



nabulanj = WesternSkin('lm1');       ngalbulanj = WesternSkin('lf1')
nawamud = WesternSkin('lm2');        ngalwamud = WesternSkin('lf2')
nangarridj = WesternSkin('lm3');     ngalngarridj = WesternSkin('lf3')
nakamarrang = WesternSkin('lm4');    ngalkamarrang = WesternSkin('lf4')
nawakadj = WesternSkin('rm1');       ngalwakadj = WesternSkin('rf1')
nabangardi = WesternSkin('rm2');     ngalbangardi = WesternSkin('rf2')
nakangila = WesternSkin('rm3');      ngalkangila = WesternSkin('rf3')
nakodjok = WesternSkin('rm4');       ngalkodjok = WesternSkin('rf4')

kela = EasternSkin('lm1');           kalidjan = EasternSkin('lf1')
kodjok = EasternSkin('lm2');         kodjdjan = EasternSkin('lf2')
balang = EasternSkin('lm3');         belinj = EasternSkin('lf3')
bangardi = EasternSkin('lm4');       bangardidjan = EasternSkin('lf4')
ngarridj = EasternSkin('rm1');       ngarridjdjan = EasternSkin('rf1')
kamarrang = EasternSkin('rm2');      kamanj = EasternSkin('rf2')
bulanj = EasternSkin('rm3');         bulanjdjan = EasternSkin('rf3')
wamud = EasternSkin('rm4');          wamuddjan = EasternSkin('rf4')
