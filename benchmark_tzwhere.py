from tzwhere import tzwhere

tz = tzwhere.tzwhere(input_kind='csv')

def benchmark():
    for i in range(10000):
        tz.tzNameAt(35.29, -89.66)


import cProfile
cProfile.run('benchmark()')


