import random

#Num of samples
N = 100000

#factor tables
#for any table f_xy, the layout is:
#       y0      y1
# x0 (x0,y0)  (x0,y1)
# x1 (x1,y0)  (x1,y1)
f_ab =[[14, 10],
       [12, 5]]

f_bc = [[11, 6],
        [1, 13]]

f_cd = [[1, 11],
        [9, 4]]

f_de = [[2, 5],
        [7, 11]]

f_ef = [[6, 3],
        [12, 15]]

f_fa = [[5, 19],
        [5, 3]]

#values of current variables
#For any variable x, False = x0 and True = x1
currDict={
    'A':None,
    'B':None,
    'C':None,
    'D':None,
    'E':None,
    'F':None
}

#maps each variables with factors involving that variable
factorsMap = {
    'A': (f_fa,f_ab),
    'B': (f_ab,f_bc),
    'C': (f_bc, f_cd),
    'D': (f_cd, f_de),
    'E': (f_de,f_ef),
    'F': (f_ef,f_fa)
}

#Generates sample given the probability distribution
def getSample(pTrue,pFalse):
    if random.uniform(0,1) <= pTrue:
        return True
    else:
        return False

#given the distVar
def getDistVar(varName, varLeftValue, varRightValue):
    f1, f2 = factorsMap[varName]
    t1 = (f1[varLeftValue][0],f1[varLeftValue][1])
    t2 = (f2[0][varRightValue],f2[1][varRightValue])

    dist = [a * b for a,b in zip(t1, t2)]
    norm = [float(i)/sum(dist) for i in dist]
    return norm

def generate_samples(n):
    return


someList = [121,345,556]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f_fa[0][1], f_ab[1][1])
    print(getDistVar('A', True, False))
    print(getDistVar('D', False, False))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
