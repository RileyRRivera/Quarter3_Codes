import numpy as np
names = ["Me", "Lia", "Jake"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])
aver=[]
cal=len(steps)
yah=len(steps[0])

for i in range(cal):
    total=0
    for x in range(yah):
        num=steps[i][x]
        total+=num
    aver.append(total)
    print(f"The total amount of steps: {names[i]} = {total}")
maxi=np.max(steps)
print(f"The highest amount of steps in a day is {maxi}")
fi=max(aver)
f=min(aver)
diff=fi-f
print(f"The difference between the highest and lowest total is {diff}")
