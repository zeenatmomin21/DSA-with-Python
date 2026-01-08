def sum_of_n(n):
    if n == 0:
        return 0
    return n + sum_of_n(n-1)
if __name__ == "__main__":
    n = 5
    print(sum_of_n(n))  