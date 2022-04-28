import numpy as np

array_random = [1,4,0,2,2,2,-3,4]
#array_final = []

for x in range(len(array_random)):

    for y in range(len(array_random) - 1, -1, -1):
        if (y < x):
          if(y>0):
            if (array_random[x] < array_random[y] and array_random[x] >= array_random[y - 1]):
                array_random = np.insert(array_random, y, array_random[x])
                #print(array_random)
                array_random = np.delete(array_random, x + 1)
                #print(array_random)
                break

          else:
            if (array_random[x] < array_random[y]):
                array_random = np.insert(array_random, y, array_random[x])
                #print(array_random)
                array_random = np.delete(array_random, x + 1)
                #print(array_random)
                break

print(array_random)