import numpy as np
sub=["Math 2", "CS", "SocSci"]
grades= np.array([
    [71, 78, 68, 54, 67],
    [80, 58, 63, 94, 73],
    [76, 85, 80, 95, 84]
])
total=0
smth=len(grades[0])
am=len(grades)
for i in range(am):
    to=0
    for x in range(smth):
        num=grades[i][x]
        total+=num
        to+=num
    aver=to/smth
    print(f"The total exam scores in {sub[i]} is {to}")
    print(f"The average exam scores in {sub[i]} is {aver}")
    print()
