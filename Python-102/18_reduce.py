import functools

numbers = [1,2,3,4]

def accum(counter,item):
  print('Este es el counter =>',counter)
  print('Este es el item =>',item)
  return counter + item

result = functools.reduce(accum, numbers)

print(result)