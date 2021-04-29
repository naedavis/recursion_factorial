
#recursion activity

#declaring the function with one parameter
#  def factorial(n):
# # #creating a variable named x as a counter
#      x = 1
# # #using a for loop to loop through parameter starting from num 2 and not 1 or 0 because of restrictions
#      for y in range(2, n + 1):
# #     #increasing my counter by multiplying by which number its at in the loop
#          x = x * y
# #     #returning end counter
#      return x
# # #calling the function with the parameter 15 because it was our fixed parameter activity
#  print(factorial(15))


#declaring the function with one parameter
def factorial(n):
#if parameter equals 0 or 1 return 0 or 1
    if n == 1 or n == 0:
        return n
    else:
        #allows for function to return values to allow factorial calculation to occur
        return n * factorial(n-1)

print(factorial(15))
