def partition():
    pass

def quicksort(a):
    return a









def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    arr = quicksort(arr)
    print(arr)

if __name__ == "__main__":
    main()