my_list=[10,20,30,40]
print(my_list)
#2
my_list[1]=15
print(my_list)
my_list1=[50,60,70]
#3
my_list.extend(my_list1)
print (my_list)
my_list.remove(70)

print(my_list)
#4
my_list.sort()
print(my_list)
#5
element = 30
found = False

for index, value in enumerate(my_list):
    if value == element:
        print(f"index of 30 is  {index}.")
        found = True
        break

if not found:
    print(f"{element} is not found in the list.")