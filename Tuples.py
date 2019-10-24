if __name__ == '__main__':
    n = int(input())
    li = [int(x) for x in input().split()]
    tp = tuple(li)
    print(hash(tp))
