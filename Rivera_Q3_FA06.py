student={}
n=input("Enter your name:")
student['Name']=n
a=input("Enter your age:")
student['Age']=a
fs=input("Enter your favorite subject:")
student['Favorite Subject']=fs
for i in student:
    print(f"{i}: {student[i]}")
