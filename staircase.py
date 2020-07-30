def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
        print(a, b)
    return a

if __name__ == "__main__":
    n = int(input())
    staircase(n)