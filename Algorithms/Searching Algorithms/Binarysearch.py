def binarysearch(arr,num):
    low = 0
    high = len(arr) - 1
    while low <= high: 
        mid = (low + high) // 2
        if arr[mid] > num: 
            high = mid - 1
        elif arr[mid] < num: 
            low = mid + 1
        else: 
            return mid
    return -1

def binsearch_recursive(a,num, low=0, high =-1):
    if not a:
        return -1
    if high ==-1:
        high = len(a)-1
    if low == high:
        if a[low] == num:
            return low
        else:
            return -1
    mid = low + (high -low)//2
    if a[mid] > num:
        return binsearch_recursive(a,num,low,mid-1)
    elif a[mid]<num:
        return binsearch_recursive(a,num,mid+1,high)
    else:
        return mid

def main():
    arr = []
    choice = "y"
    while(choice != "n"):
        arr.append(int(input("Enter a num: ")))
        choice = input("Do you want to enter more ?")
    num = int(input("Enter a number to be searched "))
    
    print("--------Binary Search:Interative Program-----------")
    pos = binarysearch(arr,num)
    print("The number " +str(num)+" is placed at the posistion "+str(pos+1))
    
    print("--------Binary Search:Recursive Program-----------")
    pos = binsearch_recursive(arr,num)
    print("The number " +str(num)+" is placed at the posistion "+str(pos+1))


if __name__ == "__main__":
    main() 