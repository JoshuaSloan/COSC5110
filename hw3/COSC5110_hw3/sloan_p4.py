# import libraries
import numpy as np
import math

# load data files
t500 = np.loadtxt("test500",delimiter='\t',dtype=str)
t1000 = np.loadtxt("test1000",delimiter='\t',dtype=str)
t2000 = np.loadtxt("test2000",delimiter='\t',dtype=str)

# get the minimum array partition from the input array: O(n^3) run-time
def minArrayPartition(arr):
    n = len(arr) 
    k = n
    sumArr = [0]*(n+1)
    
    # O(n)
    for i in range(1,n+1):
        sumArr[i] = sumArr[i-1] + arr[i-1]
        
	# initialize the matrix O(n^2)
    mapMatrix = [[0 for i in range(n + 1)] 
			for j in range(k + 1)] 

    # O(n)
    for i in range(1, n+1): 
        mapMatrix [1][i] = sumArr[i]
        
    # O(n)
    for i in range(1, k + 1): 
        mapMatrix [i][1] = arr[0] 
        
    # O(nk) where k = n S.T. O(n^2) with inner O(n) loop = O(n^3)
    for i in range(2, k + 1): 
        for j in range(2, n + 1): 
			
            best = math.inf
            
			#O(n) internal loop
            for p in range(1, j + 1):
                best = min(best, max(mapMatrix [i-1][p], 
					sumArr[j]-sumArr[p]))

            mapMatrix [i][j] = best #O(1)

    return mapMatrix[-1][-1]

# Driver Code 
t500 = t500[1].split()
for i in range(0, len(t500)): 
    t500[i] = int(t500[i]) 
    
t1000 = t1000[1].split()
for i in range(0, len(t1000)): 
    t1000[i] = int(t1000[i]) 
    
t2000 = t2000[1].split()
for i in range(0, len(t2000)): 
    t2000[i] = int(t2000[i]) 


#arr = [24,0,88,-59,-54,13,20,-11,22] 
#arr = [-20,100,-50,4,120,5] 
#arr = [7,0,-3,23,-6,10] 
arr = t500
#arr = t1000
#arr = t2000
    
MaP = minArrayPartition(arr)
#for row in new: print(' '.join('{0:.0f}'.format(new) for new in row))
print("The score of the maximum subset is:",MaP)

