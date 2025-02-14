# fruits = ["Apple", "Peach", "Banana"]

# for x in fruits:
#     print(x)


student_score = [2,45,34,67,33,78,45,95,74]

# x = sum(student_score)
# y = max(student_score)

high_score = 0

for x in student_score:
    if x >  high_score:
        high_score = x
print(high_score)        
        
