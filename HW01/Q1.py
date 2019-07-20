import numpy as np
file1=open(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\01-Data\matrixA.txt")
file2=open(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\01-Data\matrixB.txt")

ma=[]
for line in file1:
    row=[int(x) for x in line.split(",")]
    ma.append(row)
    
mb=[]
for line in file2:
    row=[int(x) for x in line.split(",")]
    mb.append(row)

ans = np.dot(ma,mb)
ans.sort(axis=1)
np.savetxt(r"C:\Users\Administrator\Desktop\NTU-Machine-learning-homework\HW0\Q1out.txt", ans, fmt="%d", delimiter="\r\n")
