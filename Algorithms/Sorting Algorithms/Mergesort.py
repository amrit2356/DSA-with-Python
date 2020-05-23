def mergesort(a):
    if len(a)>1:
        mid = len(a)//2
        left_list = a[:mid]
        right_list = a[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = j = k = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]<right_list[j]:
                a[k] = left_list[i]
                i += 1
                k += 1
            else:
                a[k] = right_list[j]
                j += 1
                k += 1
        
        while i<len(left_list):
            a[k] = left_list[i]
            i += 1
            k += 1
        
        while j<len(right_list):
            a[k] = right_list[j]
            j += 1
            k += 1


    return a

def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a value: ")))
        choice = input("Do you want to enter more ?")
    arr = mergesort(arr)
    print(arr)

if __name__ == "__main__":
    main()