items = [1,2,3,4,5,6,7,8,9,10]
item = int(input("Enter search item"))

found = False
first = 0
last = len(items)-1


while first <= last and found == False:
    mid = (first+last)//2
    if items[mid] == item:
        print("item found at index",mid)
        found = True
    
    else:
        if item < items[mid]:
            last = mid-1
        
        elif item > mid:
            first = mid+1

if found == False:
    print("itme not in list")

