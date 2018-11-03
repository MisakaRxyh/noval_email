import getnoval
from numpy import *
import time
set_printoptions(threshold=NaN)
if __name__ == '__main__':
    novalhtml = ""
    url = "https://www.37zw.net/0/761/390284.html"
    novalhtml = getnoval.Noval_Html_Code(url)
    print(novalhtml)
