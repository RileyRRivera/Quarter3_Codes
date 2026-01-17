import numpy as np
grades= np.array([
    [71, 78, 68, 54, 67],
    [80, 58, 63, 94, 73],
    [76, 85, 80, 95, 84]
])
print(grades[1][2])
grades[0][4]=70
maxi=np.max(grades)
