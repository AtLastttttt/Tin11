'''
Nhập độ cao h(m) xuất vận tốc rơi tự do của vật theo công bằng v = sqrt(2*g*h), g = 9.8
'''

h = float(input("Chieu cao:"))
g = 9.8
from math import sqrt
v = sqrt(2*g*h)
print("Van toc roi tu do cua vat theo cong:", v)
