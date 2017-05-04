# Author: Steven Bird <stevenbird1@gmail.com>
# Date: 2017-05-03

"""
Bininj Kunwok skin database and functions.
"""

from collections import defaultdict, namedtuple

# Declare all skins (to avoid typos)

NAKAMARRANG = 'nakamarrang'
NAWAMUD = 'nawamud'
NANGARRIDJ = 'nangarridj'
NABULANJ = 'nabulanj'

NAKANGILA = 'nakangila'
NAWAKADJ = 'nawakadj'
NABANGARDI = 'nabangardi'
NAKODJOK = 'nakodjok'

NGALKAMARRANG = 'ngalkamarrang'
NGALWAMUD = 'ngalwamud'
NGALNGARRIDJ = 'ngalngarridj'
NGALBULANJ = 'ngalbulanj'

NGALKANGILA = 'ngalkangila'
NGALWAKADJ = 'ngalwakadj'
NGALBANGARDI = 'ngalbangardi'
NGALKODJOK = 'ngalkodjok'

BANGARDI = 'bangardi'
KODJOK = 'kodjok'
BALANG = 'balang'
KELA = 'kela'

BULANJ = 'bulanj'
NGARRIDJ = 'ngarridj'
KAMARRANG = 'kamarrang'
WAMUD = 'wamud'

BANGARDIDJAN = 'bangardidjan'
KODJAN = 'kodjan'
BERLINJDJAN = 'berlinjdjan'
KALIDJAN = 'kalidjan'

BULANJDJAN = 'bulanjdjan'
NGARRIDJAN = 'ngarridjan'
KAMANJDJAN = 'kamanjdjan'
WAMUDDJAN = 'wamuddjan'

# Attributes (values are arbitrary, not seen externally)

GENDER = 'gender'
MALE = 'm'
FEMALE = 'f'
PATRIMOIETY = 'patrimoiety'
YIRR = 'y'
DUWA = 'd'
MATRIMOIETY = 'matrimoiety'
LEFT = 'l'
RIGHT = 'r'
LOCATION = 'location'
EAST = 'e'
WEST = 'w'

Skin = namedtuple('Skin', (GENDER, PATRIMOIETY, MATRIMOIETY, LOCATION))

flip = {
    MALE: FEMALE,
    FEMALE: MALE,
    YIRR: DUWA,
    DUWA: YIRR,
    LEFT: RIGHT,
    RIGHT: LEFT,
    EAST: WEST,
    WEST: EAST
}
    
attributes = {
    NAKAMARRANG:   Skin(MALE, YIRR, LEFT, WEST),
    NAWAMUD:       Skin(MALE, YIRR, LEFT, WEST),
    NANGARRIDJ:    Skin(MALE, DUWA, LEFT, WEST),
    NABULANJ:      Skin(MALE, DUWA, LEFT, WEST),

    NAKANGILA:     Skin(MALE, YIRR, RIGHT, WEST),
    NAWAKADJ:      Skin(MALE, YIRR, RIGHT, WEST),
    NABANGARDI:    Skin(MALE, DUWA, RIGHT, WEST),
    NAKODJOK:      Skin(MALE, DUWA, RIGHT, WEST),

    NGALKAMARRANG: Skin(FEMALE, YIRR, LEFT, WEST),
    NGALWAMUD:     Skin(FEMALE, YIRR, LEFT, WEST),
    NGALNGARRIDJ:  Skin(FEMALE, DUWA, LEFT, WEST),
    NGALBULANJ:    Skin(FEMALE, DUWA, LEFT, WEST),

    NGALKANGILA:   Skin(FEMALE, YIRR, RIGHT, WEST),
    NGALWAKADJ:    Skin(FEMALE, YIRR, RIGHT, WEST),
    NGALBANGARDI:  Skin(FEMALE, DUWA, RIGHT, WEST),
    NGALKODJOK:    Skin(FEMALE, DUWA, RIGHT, WEST),

    BANGARDI:      Skin(MALE, YIRR, LEFT, EAST),
    KODJOK:        Skin(MALE, YIRR, LEFT, EAST),
    BALANG:        Skin(MALE, DUWA, LEFT, EAST),
    KELA:          Skin(MALE, DUWA, LEFT, EAST),

    BULANJ:        Skin(MALE, YIRR, RIGHT, EAST),
    NGARRIDJ:      Skin(MALE, YIRR, RIGHT, EAST),
    KAMARRANG:     Skin(MALE, DUWA, RIGHT, EAST),
    WAMUD:         Skin(MALE, DUWA, RIGHT, EAST),

    BANGARDIDJAN:  Skin(FEMALE, YIRR, LEFT, EAST),
    KODJAN:        Skin(FEMALE, YIRR, LEFT, EAST),
    BERLINJDJAN:   Skin(FEMALE, DUWA, LEFT, EAST),
    KALIDJAN:      Skin(FEMALE, DUWA, LEFT, EAST),

    BULANJDJAN:    Skin(FEMALE, YIRR, RIGHT, EAST),
    NGARRIDJAN:    Skin(FEMALE, YIRR, RIGHT, EAST),
    KAMANJDJAN:    Skin(FEMALE, DUWA, RIGHT, EAST),
    WAMUDDJAN:     Skin(FEMALE, DUWA, RIGHT, EAST),
}

skins = list(attributes.keys())

lookup = defaultdict(list)
for skin, attr in attributes.items():
    lookup[attr].append(skin)

# Relationships

# These are not modelled, just memorised
karrang = {
    NAKAMARRANG:   NGALNGARRIDJ,
    NAWAMUD:       NGALBULANJ,
    NANGARRIDJ:    NGALWAMUD,
    NABULANJ:      NGALKAMARRANG,

    NAKANGILA:     NGALBANGARDI,
    NAWAKADJ:      NGALKODJOK,
    NABANGARDI:    NGALWAKADJ,
    NAKODJOK:      NGALKANGILA,

    NGALKAMARRANG: NGALNGARRIDJ,
    NGALWAMUD:     NGALBULANJ,
    NGALNGARRIDJ:  NGALWAMUD,
    NGALBULANJ:    NGALKAMARRANG,

    NGALKANGILA:   NGALBANGARDI,
    NGALWAKADJ:    NGALKODJOK,
    NGALBANGARDI:  NGALWAKADJ,
    NGALKODJOK:    NGALKANGILA,

    BANGARDI:      BERLINJDJAN,
    KODJAN:        KALIDJAN,
    BALANG:        KODJOK,
    KELA:          BANGARDIDJAN,

    BULANJ:        KAMANJDJAN,
    NGARRIDJ:      WAMUDDJAN,
    KAMARRANG:     NGARRIDJAN,
    WAMUD:         BANGARDIDJAN,

    BANGARDIDJAN:  BERLINJDJAN,
    KODJOK:        KALIDJAN,
    BERLINJDJAN:   KODJOK,
    KALIDJAN:      BANGARDIDJAN,

    BULANJDJAN:    KAMANJDJAN,
    NGARRIDJAN:    WAMUDDJAN,
    KAMANJDJAN:    NGARRIDJAN,
    WAMUDDJAN:     BANGARDIDJAN,
}

djedje = defaultdict(list)
for child, mother in karrang.items():
    djedje[mother].append(child)
djedje = dict(djedje)

# standard kinship relationships
def f(skin): return attributes[skin][GENDER] == FEMALE
def m(skin): return attributes[skin][GENDER] == MALE

def M(skin): return karrang[skin]
def fD(skin): ...

# need sister/brother pairs
def S(skin):
def Z(skin):

ngabba = {}
kakkali = {}
travel = {}
kakkak = {}
doydoy = {}
berluh = {}
ngadjadj = {}

for skin in skins:
    gender, patrimoiety, matrimoiety, location = attributes[skin]
    ngabba[skin] = lookup[Skin(MALE, patrimoiety, flip[matrimoiety], location)]
    berluh[skin] = lookup[Skin(FEMALE, patrimoiety, flip[matrimoiety], location)]
    kakkali[skin] = lookup[Skin(flip[gender], flip[patrimoiety], flip[matrimoiety], location)]
    travel[skin] = lookup[Skin(gender, patrimoiety, matrimoiety, flip[location])]
    ngadjadj[skin] = lookup[Skin(MALE, flip[patrimoiety], matrimoiety, location)]
    kakkak[skin] = karrang[karrang[skin]]
    doydoy[skin] = karrang[karrang[karrang[skin]]]

    siblings = djedje[karrang[skin]]

    if gender == MALE:
        kankinj[skin] = 
