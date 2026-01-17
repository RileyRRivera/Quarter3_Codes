import numpy as np
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
steps = np.array([
  [4500, 5200, 4800, 5000, 5300],
  [4000, 4100, 3900, 4200, 4600],
  [6000, 5800, 5900, 6100, 6200]
])
totday=[]
cal=len(steps)
yah=len(steps[0])

for i in range(yah):
    total=0
    for x in range(cal):
        num=steps[x][i]
        total+=num
    totday.append(total)
    print(f"The total amount of steps in {days[i]} is {total}")
act=max(totday)
mos=totday.index(act)
print(f"The most active day is {days[mos]}") 
