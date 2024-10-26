nh = 143
np = 166
while True:
  if np*(3*np -1)/2 > nh*(2*nh-1):
    nh +=1
  elif np*(3*np -1)/2 < nh*(2*nh-1):
    np += 1
  if np*(3*np -1)/2 == nh*(2*nh-1):
    break

print(np*(3*np -1)/2, nh*(2*nh-1), np, nh)