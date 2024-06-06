items = [1,2,3,4,5,6,7,8]
item = int(input("Enter search item"))
found = False

for i in range(len(items)):
    if items[i] == item:
        print("item found at index:",i)
        found = True
    
if found == False:
    print("item not in list")