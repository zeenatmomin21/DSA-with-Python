def power(x,n):
    if n ==0:
        return 1
    return x * power (x,n-1)
if __name__ == "__main__":
    x =2
    n = 5
    print(power(x,n))
    