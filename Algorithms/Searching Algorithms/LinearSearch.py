def linearsearch(a,num):
    flag = False
    for i in range(len(a)):
        if(a[i] == num):
            flag = True
            print(a)
            print("The number "+str(num)+" is available at the position "+str(i+1))
            break
        else:
            continue
    if(flag == False):
        print("The number does not exist in the list")


def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    num = int(input("Enter a number to be searched "))
    linearsearch(arr,num)

if __name__ == "__main__":
    main()


