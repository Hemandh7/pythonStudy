list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

def concatinateLists(list1, list2):
    newlist=[]
    l=min(len(list1),len(list2))
    for i in range(l):
        newlist.append(list1[i]+list2[i])
    return newlist
    
res=concatinateLists(list1, list2)
print(res)