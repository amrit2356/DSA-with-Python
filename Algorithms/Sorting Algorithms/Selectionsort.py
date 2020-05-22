def selectionsort(a):
    for i in range(len(a)):
        least = i
        for k in range(i+1,len(a)):
            if(a[k]<a[least]):
                least = k
        swap(a,least,i)
    return a

def swap(a,x,y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp


def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    arr = selectionsort(arr)
    print(arr)


if __name__ == "__main__":
    main()

