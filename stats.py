def mean(arr):
    summ = 0
    n = len(arr)
    for num in arr:
        summ += num
    
    return summ / n

def median(arr):
    n = len(arr)
    d = int(n/2)
    if n % 2 == 0:
        return (arr[d] + arr[d-1]) / 2
    else:
        return arr[d]
        
def mode(arr):
    d = {}
    maxx = 0
    for num in arr:
        d[num] = d.get(num, 0) + 1
        maxx = max(maxx, d[num])
    
    ans = []
    
    for n, freq in d.items():
        if freq == maxx:
            ans.append(n)
    
    return ans
     

def variance(arr):
    m = mean(arr)
    sol = 0 
    for num in arr:
        sol += (num - m) ** 2
    
    return sol / (len(arr))

def std(arr):
    return variance(arr) ** 0.5

def correlation(arr1, arr2):
    std1 = std(arr1)
    std2 = std(arr2)
    cov = covariance(arr1, arr2)
    
    return cov / (std1 * std2)

def covariance(arr1, arr2):
    mean1 = mean(arr1)
    mean2 = mean(arr2)
    
    sol = 0 
    for i in range(len(arr1)):
        sol += (arr1[i] - mean1) * (arr2[i] - mean2)
    
    return sol / (len(arr1))

def min_max(arr1):
    min = float('inf')
    max = float('-inf')
    
    for num in arr1:
        if num < min:
            min = num
            
        if num > max:
            max = num
        
    for i in range(len(arr1)):
        arr1[i] = round((arr1[i] - min) / (max - min), 5)
    
    return arr1
