def febonacci(n,arr):
    if n==0:
        return 0
    if n ==1:
        return 1
    if arr[n] != -1:
        return arr[n]
    arr[n] = febonacci(n-1,arr) + febonacci(n-2,arr)
    return arr[n]
if __name__ == "__main__":
    n =6
    arr = [-1] * (n+1)
    for i in range(n+1):
        print(febonacci(i,arr))