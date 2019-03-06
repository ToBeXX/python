#杨辉三角
#方法一
def triangles():
    L = [1]
    while True:
        L = [1]+[L[i] + L[i+1] for i in range(len(L)-1)]+[1]
        yield L
#方法二
import operator
def triangles():
    L = [1]
    while True:
        L = list(map(operator.add,[0]+L,L+[0]))
        yield L
#方法三
def triangles():
    L = [1]
    while True:
        L = [x+y for k,x in enumerate([0]+L) for j,y in enumerate(L+[0]) if k==j]
        yield L
