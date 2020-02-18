#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  while (x<5):
    print(x)
    x = x + 1

  # define a for loop
  for x in range(0, 105, 5):
    print(x)

  # use a for loop over a collection
  days = ["Monday","Tuesday","Wednesday","Thursday","Saturday","Sunday"]
  for d in days:
    print(d)
  # use the break and continue statements
    for x in range(0, 105, 5):
      if x == 25:
        continue
      if x == 55:
        break
      print(x)

  #using the enumerate() function to get index 
  days = ["Monday","Tuesday","Wednesday","Thursday","Saturday","Sunday"]
  for i, d in enumerate(days):
    print(i, d)

if __name__ == "__main__":
  main()
