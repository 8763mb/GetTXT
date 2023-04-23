# read input data
account1 = int(input())
account2 = int(input())
transfer = int(input())

# make transfer
if transfer <= account1:
  afterAccount1 = account1 - transfer
  afterAccount2 = account2 + transfer
else:
  afterAccount1 = 0
  afterAccount2 = account2 + account1

# print results  
print(afterAccount1, afterAccount2)

