i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

  def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(country = "Norway", moves = 6):
  print("I am from %s and I have moved %d times" %(country, moves))

my_function("Sweden", 3)
my_function("India", 4)
my_function()
my_function("Brazil", 5)

print ("Done")
