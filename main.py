total = 0
binaryArray = []

def binary_reader():
  try:
    print("Enter 8 binary values with no white space:")
    binaryInput = input()
    eachNum = binaryInput.split(",")
    binaryArray = eachNum
    binary_converter(total, binaryArray)
  except:
    print("Error!")
    exit()
		
def binary_converter(total, binaryArray):
   if(binaryArray[0].__eq__("1")):
     total = total + 128
   if(binaryArray[1].__eq__("1")):
     total = total + 64
   if(binaryArray[2].__eq__("1")):
     total = total + 32
   if(binaryArray[3].__eq__("1")):
     total = total + 16
   if(binaryArray[4].__eq__("1")):
     total = total + 8
   if(binaryArray[5].__eq__("1")):
     total = total + 4
   if(binaryArray[6].__eq__("1")):
     total = total + 2
   if(binaryArray[7].__eq__("1")):
     total = total + 1
   print(total)
   c = chr(total)
   print(c)
   total = 0;

print("How many characters would you like to convert?")
try:
    userRepeat = int(input())
    print("You will now convert", userRepeat, "characters.")
    count = 1
    binary_reader()
    while(count < userRepeat):
      count = count + 1
      binary_reader()
      print("bell")
except:
  print ("Error")