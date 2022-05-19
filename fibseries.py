# the og code
# m = 0
# n = 1

# print(m)
# print(n)

# while m <= 10:
#    x = m + n
#    print(x)
#    m = n
#    n = x

#the better version, after my brother's chastisement

# getting the number from the user
times = int(input("Enter till which number you want the series: "))

# function to calculate the series until the said number
def fib(times):
   # creating an array to sort the values
   fibnochi = [0, 1]
   m = 0
   n = 1
   # loop to calculate the series
   while n + m <= times:
      swap = n + m
      fibnochi.append(swap)
      m = n
      n = swap
   return fibnochi

# mentioning my brother because he is a bully
yogi = fib(times)

# printing the array
print(yogi)