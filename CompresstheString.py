import itertools

def main():
    S = input()
    
    print(*(itertools.starmap(lambda key, group: (len(list(group)), int(key)), itertools.groupby(S))))

if __name__ == '__main__':
    main()
