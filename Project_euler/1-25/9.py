for a in range (0, 400):
  for b in range (0, 400):
    for c in range (0, 500):
      if a+b+c==1000:
        while a**2+b**2==c**2:
          print(a*b*c)
          print(a, b, c)
          break