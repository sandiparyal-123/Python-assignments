#1. create the list
list1 = ["x", "y", "z", 1, 2, 3]
print(list1)

#2. adding element to list using append
list1.append(76)
print ("after adding new item:  ", list1)

#3. adding using insert
list1.insert(4 , "apple")
print ("adding using insert:   ", list1)

#4. deleting using remove: 
list1.remove(3)
print ("after using remove():   ", list1)

#5. deleting using pop:
list1.pop()
print ("after using pop():   ", list1)

#6. sorting - increasing order: 
list2 = [1,3,6,2,56,73,24]
list2.sort()
print ("increasing order:   ", list2)

#7. sorting  -decreasing order:
list2.sort(reverse =True)
print ("decreasing order:   ", list2)

#8. simple reversing:
list1.reverse()
print("reversed list:   ", list1)

#9. clear fucntion :
list2.clear()
print (list2)

#10. del function for removing
del list1[2] #index used
print (list1)