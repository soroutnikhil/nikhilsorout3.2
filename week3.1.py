# Ans 1
data = [('Sachin Tendulkar', 34357), ('Ricky Ponting', 27483), ('Jack Kallis', 25534), ('Virat Kohli', 24936)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)



# Ans 2
a=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b=list(map(lambda x:x*x, a))
print(b)


# Ans 3
list=[1,2,3,4,5,6,7,8,9,10]
string_number=tuple(map(lambda x : str(x),list) )
print(string_number)


# Ans 4
from functools import reduce
list=range(1,25)
square=reduce(lambda x,y : x*y ,list)
print(square)

# Ans 5
number_list = [2, 3, 6, 9, 27, 60, 90, 120, 55, 46]

filtered_list = filter(lambda x: x % 2 == 0 and x % 3 == 0, number_list)

print(list(filtered_list))


# Ans 6
word = ['python', 'php', 'aba', 'radar', 'level']

palindromes = list(filter(lambda word: word == word[::-1], word))

print(palindromes)




