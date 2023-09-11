[9/4, 1:41 PM] Thulasiraman: 1.1 Implement a recursive function ti calculate he factorial of a given number


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter the value :"))
res = fact_rec(number)

print("The factorial of {} is {}".format(number, res))
[9/4, 2:08 PM] Thulasiraman: def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


num = 5
print("Factorial of", num, "is", factorial(num))