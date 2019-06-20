import random as r
def merge(l, r):
    lst = []
    while l and r:
        if l[0] < r[0]:
            lst.append(l.pop(0))
        else:
            lst.append(r.pop(0))

    if l:
        lst.extend(l)
    if r:
        lst.extend(r)
    return lst

def mergesort(lst):
    ln = len(lst)
    if ln >= 2:
        mid = int(ln / 2)
        lst = merge(mergesort(lst[:mid]), mergesort(lst[mid:]))
    return lst


t = [r.randint(1,1000) for i in range(50)]
print('before: ', t)
res = mergesort(t)
print()
print('after: ', res)
