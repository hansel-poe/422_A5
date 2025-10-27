import random
import matplotlib.pyplot as plt
from collections import deque

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

#Formar is (left, right)
neighborsMap = {
    'A': ('F','B'),
    'B': ('A','C'),
    'C': ('B','D'),
    'D': ('C','E'),
    'E': ('D','F'),
    'F': ('E','A')
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

#compute P(var = val  | givens) over n samples
def generate_samples(n, var, val = False, givens = []):
    for i in currDict: currDict[i] = getSample(0.5,0.5) #assign randomly with uniform dist
    for given in givens: currDict[given] = givens[given] #assign given variables

    rotationVars = [i for i in currDict if i not in givens]
    de = deque(rotationVars)
    probs = []
    count_dict = {
        False:0,
        True:0
    }
    for i in range(n):
        toSample = de.popleft() #get var to sample
        left, right = neighborsMap[toSample]
        dist = getDistVar(toSample, currDict[left], currDict[right])
        sample = getSample(dist[1], dist[0])
        currDict[toSample] = sample

        count_dict[currDict[var]] += 1
        probs.append(count_dict[val] / (i + 1))
        de.append(toSample)#put back var in the back

    return probs

def graph(x, y, ve_val):
    # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
    fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
    ax.set_xscale('log')
    ax.plot(x, y, label='Gibbs Sampling')  # Plot some data on the Axes.
    ax.set_xlabel('Number of samples')  # Add an x-label to the Axes.
    ax.set_ylabel('P(E = e0 | b1, c0)')  # Add a y-label to the Axes.
    ax.set_title('P(E = e0 | b1, c0) vs Number of Samples')  # Add a title to the Axes.

    plt.axhline(y=ve_val, label='Variable Elimination', color = 'r') #plot horizontal line showing result from variable elimination

    plt.legend()
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Test
    # print(f_fa[0][1], f_ab[1][1])
    # print(getDistVar('A', True, False))
    # print(getDistVar('D', False, False))

    givens = {'B': True, 'C': False}
    probs = generate_samples(N, 'E', False, givens)
    x = range(1,100001)
    # print(len(probs))
    # print(probs[0:30])
    graph(x,probs, 0.197)
    print(probs[99995:])




