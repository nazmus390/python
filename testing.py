# num =[1,2,3,4,5]
# for x in num:
#     if x == 3:
#         print("found!")
#         continue
#     print(x)
#

num =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for x in num:
    for letter in '0123456789':
        print(x,letter)
        count+=1
print(count)


x = 1
while x < 11:
    print(x)
    x += 1

print(x)
