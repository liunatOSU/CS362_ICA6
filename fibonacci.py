def fibonacci(num):
  if(isinstance(num, int)):
    n1 = 0
    n2 = 1
    temp = 0
    count = 1
    if(num <= 0):
      return None
    elif(num == 1):
      return n1
    else:
      while(count < num):
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count += 1
      return n1
  else:
    print("Input is invalid")
    return None

def factorial(num):
  if(isinstance(num, int)):
    fact = 1
    if(num < 0):
      return None
    elif(num == 0):
      return 1
    else:
      for i in range(1, num+1):
        fact = fact * i
      return fact
  else:
    print("Input is invalid")
    return None



