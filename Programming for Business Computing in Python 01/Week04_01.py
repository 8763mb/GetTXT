cost = int(input())      
price = int(input())     
maxDemand = int(input()) #固定是8
quantity = int(input())


expSales = 0.0


for demand in range(maxDemand + 1):  #跑8次
  prob = float(input())              #輸入8次機率

  if demand < quantity:         
    expSales += prob * demand        #計算獲利
  else:                        
    expSales += prob * quantity

# calculate and print the result
print(expSales)
profit = expSales * price - quantity * cost  #獲利減成本
print(int(profit))

