def bubblesort(a):
    for i in range(len(a)):
        for k in range(len(a)-1,i,-1):
            if(a[k]<a[k-1]):
                swap(a,k,k-1) 
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
    arr = bubblesort(arr)
    print(arr)

if __name__ == "__main__":
    main()









