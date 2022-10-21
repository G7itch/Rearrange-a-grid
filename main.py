##### NOTES BEFORE PROJECT #####
# -there is going to be A LOT of counter varaibles, name them properly
# -0 -> black, 1 -> white

from random import randint

amountoflists = int(input("Enter how many rows there will be: "))
grid = [list() for i in range(amountoflists)]
lengthoflists = int(input("Enter how long the lists should be: "))

howmanynumbers = int(input("How many numbers should be used for the grid?: "))

for i in range(amountoflists):
  for j in range(lengthoflists):
    randomselector = randint(0, howmanynumbers)
    grid[i].append(randomselector)
      
print("----------ORIGINAL GRID----------\n")
for i in range(amountoflists):
  print(grid[i])

def sortgrid(grid, amountoflists, lengthoflists):
  numberlist = []
  print("\n\n----------SORTED GRID----------")
  for i in range(amountoflists):
    for j in range(lengthoflists):
      numberlist.append(grid[i][j])
       
  numberlist = sorted(numberlist)    

  newgrid = [list() for i in range(amountoflists)]

  n = 0

  for i in range(amountoflists):
    for j in range(lengthoflists):
      newgrid[i].append(numberlist[n])
      n += 1


  print("")
  for i in range(amountoflists):
    print(newgrid[i])


def removenumber(grid):
  pass

def replaceinstances(grid, amountoflists, lengthoflists):
  numberlist = []
  whatreplaced = input("\nWhat do you want to replace?: ")
  replacedwith = input("Replace with?: ")
  for i in range(amountoflists):
    for j in range(lengthoflists):
      numberlist.append(grid[i][j])
       
  numberlist = sorted(numberlist)    
  n = 0
  newgrid = [list() for i in range(amountoflists)]


  for i in range(amountoflists):
    for j in range(lengthoflists):
      if numberlist[n] == whatreplaced:
        numberlist[n] = replacedwith
      else:
        pass  
      newgrid[i].append(numberlist[n])
      n += 1 

  for i in range(amountoflists):
    print(grid[i])


print("\n\n1. Sort grid")
print("2. Remove number")
print("3. Replace instances")
option = int(input(">> "))
if option == 1:
  sortgrid(grid, amountoflists, lengthoflists)
elif option == 2:
  removenumber(grid)
elif option == 3:
  replaceinstances(grid, amountoflists, lengthoflists)
else:
  print("Thats not an option")  