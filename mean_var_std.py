import numpy as np
def calculate(list):
    if (len(list)< 9):
        raise ValueError("List must contain nine numbers.")
    arr1 = np.array(list)
    arr = arr1.reshape(3,3)
    cols=np.column_stack(arr)
    var = [[np.var(x) for x in cols],[np.var(x) for x in arr],np.var(arr)]
    mean = [[np.mean(x) for x in cols],[np.mean(x) for x in arr],np.mean(arr)]
    std = [[np.std(x) for x in cols],[np.std(x) for x in arr],np.std(arr)]
    max = [np.max(arr, axis=0),np.max(arr, axis=1),np.max(arr)]
    min = [np.min(arr, axis=0),np.min(arr, axis=1),np.min(arr)]
    sum = [arr.sum(axis=0),arr.sum(axis=1),arr.sum()]
  
    calculations={"mean":mean, "variance":var, "standard deviation": std, "max":max, "min":min, "sum":sum}
    
    return calculations
print(calculate([2,6,2,8,4,0,1,5,7]))
