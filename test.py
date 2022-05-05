# # Write you code here

# def fib(m, n):
#     """Find The Fib Nums!"""

#     # fib_nums = [0, 1]
#     n = 1
#     for m in range(0,90):
#         x = m + n
#         # fib_nums.append(x)
#         print(x)
#         m = n
#         n = x
#     # return fib_nums

# # print(fib(0, 1))
# fib(0, 1)

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1



