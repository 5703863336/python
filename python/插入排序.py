#插入排序
def inser_sort(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j]<alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
#二分查找
def erfen(alist,item):
    if not alist:
        return False
    n = len(alist)
    mid = n // 2
    if alist[mid] ==item:
        return  True
    elif item<alist[mid]:
        return erfen(alist[:mid],item)
    else:
        return erfen(alist[mid+1:],item)



alist = [1,4,5,2,3]

inser_sort(alist)
print(alist)
a = alist
print(a)
print(erfen(a,5))
