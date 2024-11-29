import numpy as np;

def UpdateMean(OldMean: float, newElement:float, n:int, A:list):
    return OldMean + (newElement - OldMean)/(n+1)

def UpdateMedian(OldMedian:float, NewDataValue:float, n:int, A:list):
    if n % 2 == 0:
        if NewDataValue < OldMedian:
            if A[n//2 - 1] <= NewDataValue:
                return NewDataValue
            else:
                return A[n//2 - 1]
        else:
            if A[n//2] >= NewDataValue:
                return NewDataValue
            else:
                return A[n//2]
    else:
        if NewDataValue < OldMedian:
            if A[n//2] <= NewDataValue:
                return (NewDataValue + A[n//2+1])/2
            else:
                return (A[n//2] + A[n//2-1])/2
        else:
            if A[n//2] >= NewDataValue:
                return (A[n//2] + NewDataValue)/2
            else:
                return (A[n//2] + A[n//2+1])/2
    

def UpdateStd(OldMean:float, OldStd:float, NewDataValue: float, n:int, A:list):
    return (((n)*(n-1) * OldStd**2) + (n-1)*(NewDataValue - OldMean)**2)**0.5 / (n)

N = input("Enter the number of elements in the array: ")
A = []

for i in range(int(N)):
    A.append(float(input()))
    
OldMean = float(input("Enter the old mean: "))
OldMedian = float(input("Enter the old median: "))
OldStd = float(input("Enter the old standard deviation: "))
NewDataValue = float(input("Enter the new data value: "))

print("New mean: ", UpdateMean(OldMean, NewDataValue, N, A))
print("New median: ", UpdateMedian(float(OldMedian), float(NewDataValue), int(N), np.array(A)))
print("New standard deviation: ", UpdateStd(float(OldMean), float(OldStd), float(NewDataValue), int(N), np.array(A)))
