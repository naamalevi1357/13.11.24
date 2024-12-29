# # start
import random
# 1:
# A:

city:list[str]=["Tokyo","New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

# a:
print(sorted(city,key= lambda c:len(c)))

# b:
print(sorted(city, key= lambda city: len(city.split())))

# c:
print(sorted(city,key=lambda a:city[-1]))

# d:
print(sorted(city,key=lambda n:city[::-1]))

# e: bonos
print(sorted(city,key=lambda e:city.count("a")))

# f:
contr=[["Tokyo", 5760, "Asia"], ["New York", 5690, "North America"], ["Paris", 2050,
"Europe"], ["London", 2240, "Europe"], ["Sydney", 8780, "Australia"],
["Dubai", 1300, "Asia"], ["Shanghai", 4920, "Asia"]]
# a:
print(sorted(contr, key=lambda i : i[1]))
# b:
print(sorted(contr, key=lambda i : i[1],reverse= True))

# c:
print(sorted(contr, key=lambda i:i [2]))

# e:
print(sorted(contr, key=lambda i:i [2][1]))


# b:
# 1:
list1:list[int]=[]
for i in range(50):
    x=random.randint(1,100+1)
    list1.append(x)
print(list1)
x=list1.sort()
# print(x)
print(sorted(list1,key= lambda a:[list1.sort()]))

# 2:

y=sum(list1)
print(y)
# print(sorted(list1, key= lambda s:(sum(list1)/2, s)))
print(sorted(list1, key= lambda s:(sum(list1), s)))




# 2
stori:str= ("This chocolate cake is rich moist and full of delicious chocolate flavor"
            "To make the cake you will need chocolate  flour sugar eggs and butter"
            "After baking the chocolate cake let the cake cool before adding the chocolate frosting")

# a:
word_count:dict[str,int]={}
for u in stori.split():
    if u in word_count:
        word_count[u]+=1
    else:
        word_count[u]=1
print(word_count)

# print(max(word_count))
# fr=stori.split()
# cv:list=fr
# print(cv)
# print(max(cv))
# print(max(cv))
print(max(word_count, key= word_count.get))
# b:
signal:dict[str,int]={}
for i in stori:
    if i in signal:
        signal[i]+=1
    else:
        signal[i]=1
print(signal)
# print(list(max(signal)))
print(min(word_count, key= word_count.get))



# 3:
numbers:dict[int,int]={1:1,2:8,3:27, 4:64, 5:125, 6:216 ,7:343 ,8:512,9:729 , 10:1000,11:1331,
                       12:1728, 13:2197,14:2744, 15:3375, 16:4096, 17:4913,18:5832,19:6859,20:8000}
number:int=int(input(" what is number? "))

print(numbers.get(number, "not exist"))


















# stop