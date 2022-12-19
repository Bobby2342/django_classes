# colors=["yellow","green","red","blue","yellow","orange","red"]
# to_be_removed = ["yellow","red"]
# new_colors = []

# for color in  colors:
#     if color not in to_be_removed:
#         new_colors.append(color)
# print(new_colors)

# print(list(filter(lambda color:color not in to_be_removed,colors,)))
        
 

a ="876d59e45"
total = 0
for i in a :
    if i.isdigit():
        total = total + int(i)

print(total)

print(sum(map(int,filter(str.isdigit,a))))
