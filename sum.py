a = "876d59e45"
total = 0
for i in a :
    if i.isdigit():
        total = total + int(i)

print(total)

# print(sum(map(int,filter(str.isdigit,a))))

output = filter(str.isdigit,a)
o = map(int,output)
print(sum(o))