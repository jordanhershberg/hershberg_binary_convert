def DecimalToBinary(num):

  if num == 0:
    return "0"
  binary_num = ""
  while num > 0:
    remainder = num % 2
    binary_num = str(remainder) + binary_num
    num = int(num / 2)
  return binary_num

decimal = int(input("What is your decimal number? \n"))

print(DecimalToBinary(decimal))



def BinaryToDecimal(binaryNum):

  decimal_num = 0
  power = 0
  for digit in binaryNum[-1::-1]:
    if digit == '1':
      decimal_num += 2**power
    power += 1
  return decimal_num
binaryNum = input("What is your binary number\n")

print(BinaryToDecimal(binaryNum))