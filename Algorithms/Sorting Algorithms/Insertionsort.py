def insertionsort(a):
    for i in range(1,len(a)):
        tmp = a[i]
        k = i
        while k>0 and tmp <a[k -1]:
            a[k] = a[k-1]
            k-=1
        a[k] = tmp
    
    return a


def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    arr = insertionsort(arr)
    print(arr)

if __name__ == "__main__":
    main()