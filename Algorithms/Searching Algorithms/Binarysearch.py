def binarysearch(arr,num):
    pass

def binsearch_recursive():
    pass




def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    num = int(input("Enter a number to be searched "))
    binarysearch(arr,num)

if __name__ == "__main__":
    main() 