List =['math','che','phy']

List.append(20544)
print(List)

List.insert(2,10075)
print(List)

List1 = [1,2,3]
List2 = [2,3,4,5]

#add list2 to list1
List1.extend(List2)
print(List1)

# add List1 to list2
List2.extend(List1)
print(List2)

List = [1,2,3,4,5]
print(sum(List))

List = [1,2,3,1,2,1,2,3,2,1]
print(List.count(1))

List = [1,2,3,1,2,1,2,3,2,1]
print(len(List))

List = [1,2,3,1,2,1,2,3,2,1]
print(List.index(2))

List = [5.4,2.1,3.2,4.5,6.7]
print(min(List))

List = [5.4,5.1,2.3,6.1,2.8]
print(max(List))

List = [2.4,5.6,3.2,4.2]
print(List.pop())

List = [2.5,1.4,2.3,1.5]
print(List.pop(0))

List = [2.3,5.4,3.6,5.8]
del List[0]
print(List)

List = [2.5,1.5,7.3,9.3]
List.remove(1.5)
print(List)
print(List.copy())
print(List.clear())