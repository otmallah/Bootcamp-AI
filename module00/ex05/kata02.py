

from select import POLLNVAL
from tkinter import Place


kata = (2019, 9, 25, 3, 30)
string = '0{}/{}/{} 0{}:{}'
print(string.format(kata[1], kata[2], kata[0], kata[3], kata[4]))