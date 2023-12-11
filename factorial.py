def calculate_factorial(number):
    i = 1
    sums = []
    sum = 1
    while i < number +1 :
      sums.append(i)
      i += 1
    for i in sums:
       sum = sum * i
    return(sum)
