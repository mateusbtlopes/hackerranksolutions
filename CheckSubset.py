def main():
    for i in range(int(input())):
        a = int(input()); A = set(input().split())
        b = int(input()); B = set(input().split())
        print('True' if A.union(B) == B else 'False')

if __name__ == '__main__':
    main()
