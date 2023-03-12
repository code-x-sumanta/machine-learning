import numbers


numbers=[2,9,7,6]
print(numbers)
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.append(10)
numbers.append(11)
print(numbers)
#

numbers.insert(2,0)
print(numbers)

numbers[1]=4
print(numbers)

#tuple
#tuple is inmutable but list is mutable . We can not add or remove any value from the tuple

tp=(1,3,5,6)
print(tp)
print(type(tp))

#Python interchange process

a=4
b=6
a,b=b,a
print(a,b)