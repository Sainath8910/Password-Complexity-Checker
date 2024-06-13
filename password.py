import re


def password(p):
  l = [
      "your password doen't have atleast 8 characters",
      "your password doen't have any special characters",
      "your password doen't have any uppercase letter",
      "your password doen't have any lowercase letter",
      "your password doen't have any numerical"
  ]
  a = [0, 1, 2, 3, 4]
  k = 0
  if len(p) > 8:
    k = k + 1
    a.remove(0)

  if re.search(r'[\W_]', p):
    k = k + 1
    a.remove(1)

  if re.search(r'[A-Z]', p):
    k = k + 1
    a.remove(2)

  if re.search(r'[a-z]', p):
    k = k + 1
    a.remove(3)

  if re.search(r'[0-9]', p):
    k = k + 1
    a.remove(4)

  for i in a:
    print(l[i])
  return k


p = input("enter your password :")
k = password(p)
print("In the range of 1 to 5 your password strength is ----- " + str(k))
