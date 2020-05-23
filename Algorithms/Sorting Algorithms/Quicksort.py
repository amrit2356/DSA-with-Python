import random
def partition(a, low, high):
    pivot = low + random.randrange(high-low+1)
    swap(a,pivot, high)
    for i in range(low, high):
        if a[i]<=a[high]:
            swap(a,i,low)
            low+=1

    swap(a, low,high)
    return low        

def swap(a,x,y):
    tmp = a[x]
    a[x] = a[y]
    a[y] = tmp

def quicksort(a, low, high):
    if low<high:
        pivot = partition(a,low,high)
        quicksort(a,low,pivot-1)
        quicksort(a,pivot+1,high)
    return a

def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    arr = quicksort(arr ,0, len(arr)-1)
    print(arr)

if __name__ == "__main__":
    main()