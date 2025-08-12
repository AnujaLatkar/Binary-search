list = []
n =int(input("Enter The Number : "))
for i in range (0,n):
    ele= int (input("Enter Element"))
    list.append(ele)
print(list)
AC_id=int(input("Enter AC_id to be searched"))
list.sort()
print(list)
left=0
right=len(list)-1

while left<=right:
    mid=(left+right)//2
    if list[mid]==AC_id:
        print(AC_id," is found at index ",mid)
        break 
    if list[mid]<AC_id:
        left=mid+1
    if list[mid]>AC_id:
        right=mid-1
