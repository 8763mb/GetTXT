# 讀取輸入資料
cost = int(input())      # 每單位進貨成本
price = int(input())     # 每單位零售價格
maxDemand = int(input()) # 固定8
quantity = int(input())  # 訂購數量

# 初始化預期銷售為 0
expSales = 0.0


for demand in range(maxDemand + 1):  #跑9次
    
    prob = float(input())              

    
    if demand < quantity:         
        # 將需求量乘以概率加入預期銷售
        expSales += prob * demand       
    else:                        
        # 將訂購量乘以概率加入預期銷售
        expSales += prob * quantity

print(expSales)

# 計算利潤，並輸出整數部分
profit = expSales * price - quantity * cost  
print(int(profit))
