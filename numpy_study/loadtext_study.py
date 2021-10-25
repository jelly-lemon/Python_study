from io import StringIO

import numpy as np

def test_0():
    d = StringIO(u"M 21 72\\nF 35 58")
    d = np.loadtxt(d, dtype={'names': ('gender', 'age', 'weight'), 'formats': ('S1', 'i4', 'f4')})
    print(d)

if __name__ == '__main__':
    test_0()