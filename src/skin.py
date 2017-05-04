# Author: Steven Bird <stevenbird1@gmail.com>
# Date: 2017-05-03

"""
Bininj Kunwok skin database.
"""

# Skins are encoded as matrimoiety (left, right), gender, and generation number.

MALE = 'm'
FEMALE = 'f'

LEFT = 'l'
RIGHT = 'r'

west = {
    'lm1': 'nabulanj',         'lf1': 'ngalbulanj',
    'lm2': 'nawamud',          'lf2': 'ngalwamud',
    'lm3': 'nangarridj',       'lf3': 'ngalngarridj',
    'lm4': 'nakamarrang',      'lf4': 'ngalkamarrang',
    'rm1': 'nawakadj',         'rf1': 'ngalwakadj',
    'rm2': 'nabangardi',       'rf2': 'ngalbangardi',
    'rm3': 'nakangila',        'rf3': 'ngalkangila',
    'rm4': 'nakodjok',         'rf4': 'ngalkodjok'
}

east = {
    'lm1': 'kela',             'lf1': 'kalidjan',
    'lm2': 'kodjok',           'lf2': 'kodjdjan',
    'lm3': 'balang',           'lf3': 'belinj',
    'lm4': 'bangardi',         'lf4': 'bangardidjan',
    'rm1': 'ngarridj',         'rf1': 'ngarridjdjan',
    'rm2': 'kamarrang',        'rf2': 'kamanj',
    'rm3': 'bulanj',           'rf3': 'bulanjdjan',
    'rm4': 'wamud',            'rf4': 'wamuddjan'
}

increase = {'1': '2', '2': '3', '3': '4', '4': '1'}
decrease = {'1': '4', '2': '1', '3': '2', '4': '3'}

# utility function
def p(skin, f):
    return f(*tuple(skin))

# gender tests
def f(skin):
    return p(skin, lambda m, g, n: g == FEMALE)

# gender tests
def m(skin):
    return p(skin, lambda m, g, n: g == MALE)

# duwa?
def duwa(skin):
    return p(skin, lambda m, g, n: n in '13')

# find the mother
def M(skin):
    return p(skin, lambda m, _, n: m + FEMALE + decrease[n])

# find a woman's daughter
def fD(skin):
    assert f(skin)
    return p(skin, lambda m, _, n: m + FEMALE + increase[n])

# brother
def B1(skin):
    return p(skin, lambda m, _, n: m + MALE + n)
def B2(skin):
    return p(skin, lambda m, _, n: m + MALE + increase[increase[n]])

# sister
def Z1(skin):
    return p(skin, lambda m, _, n: m + FEMALE + n)
def Z2(skin):
    return p(skin, lambda m, _, n: m + FEMALE + increase[increase[n]])

# spouse
# NB we're not modelling first and second choices here
def SP1(skin):
    return p(skin,
             lambda m, g, n: (
                 {LEFT: RIGHT, RIGHT: LEFT}[m] +
                 {MALE: FEMALE, FEMALE: MALE}[g] +
                 n))

def SP2(skin):
    skin = SP1(skin)
    return p(skin,
             lambda m, g, n: m + g + increase[increase[n]])

def F1(skin):
    return P1(M(skin))

def F2(skin):
    return P2(M(skin))

def mD1(skin):
    assert m(skin)
    return fD(SP1(skin))

def mD2(skin):
    assert m(skin)
    return fD(SP2(skin))
