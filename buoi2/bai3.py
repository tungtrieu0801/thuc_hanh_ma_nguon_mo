import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])
arr_sv = in_data[:, 1]
diemA = in_data[:, 3]
diemBc = in_data[:, 4]
diemB = in_data[:, 5]
diemCc = in_data[:, 6]
diemC = in_data[:, 7]
diemDc = in_data[:, 8]
diemD = in_data[:, 9]
diemF = in_data[:, 10]
arr_svl1 = in_data[:, 11]
arr_svl2 = in_data[:, 12]
arr_svtx1 = in_data[:, 13]
arr_svtx2 = in_data[:, 14]
arr_svck = in_data[:, 15]

print("Tổng sinh viên tham gia môn học: ", np.sum(arr_sv))

print("Tổng sinh viên đạt A: ", np.sum(diemA))
print("Tổng sinh viên đạt B+: ", np.sum(diemBc))
print("Tổng sinh viên đạt B: ", np.sum(diemB))
print("Tổng sinh viên đạt C+: ", np.sum(diemCc))
print("Tổng sinh viên đạt C: ", np.sum(diemC))
print("Tổng sinh viên đạt D+: ", np.sum(diemDc))
print("Tổng sinh viên đạt D+: ", np.sum(diemD))
print("Tổng sinh viên đạt F: ", np.sum(diemF))

print("Tỷ lệ sinh viên đạt A: ", (np.sum(diemA)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt B+: ", (np.sum(diemBc)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt B: ", (np.sum(diemB)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt C+: ", (np.sum(diemCc)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt C: ", (np.sum(diemC)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt D+: ", (np.sum(diemDc)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt D+: ", (np.sum(diemD)/np.sum(arr_sv))*100,'%')
print("Tỷ lệ sinh viên đạt F: ", (np.sum(diemF)/np.sum(arr_sv))*100,'%')

print("Tbc sinh viên đạt A: ", np.mean(diemA))
print("Tbc sinh viên đạt B+: ", np.mean(diemBc))
print("Tbc sinh viên đạt B: ", np.mean(diemB))
print("Tbc sinh viên đạt C+: ", np.mean(diemCc))
print("Tbc sinh viên đạt C: ", np.mean(diemC))
print("Tbc sinh viên đạt D+: ", np.mean(diemDc))
print("Tbc sinh viên đạt D+: ", np.mean(diemD))
print("Tbc sinh viên đạt F: ", np.mean(diemF))


kdatl1 = np.subtract(arr_sv, arr_svl1)
kdatl2 = np.subtract(arr_sv, arr_svl2)
kdattx1 = np.subtract(arr_sv, arr_svtx1)
kdattx2 = np.subtract(arr_sv, arr_svtx2)
kdatck = np.subtract(arr_sv, arr_svck)
print("Tổng sinh viên không đạt L1: ", np.sum(kdatl1))
print("Tổng sinh viên không đạt L2: ", np.sum(kdatl2))
print("Tổng sinh viên không đạt TX1: ", np.sum(kdattx1))
print("Tổng sinh viên không đạt TX2: ", np.sum(kdattx2))
print("Tổng sinh viên không đạt cuối kỳ: ", np.sum(kdatck))

maxa = diemA.max()
i, = np.where(diemA == maxa)
mina = diemA.min()
z, = np.where(diemA == mina)
maxf = diemF.max()
j, = np.where(diemF == maxf)
minf = diemF.min()
a, = np.where(diemF == minf)
print('Lớp có nhiều điểm A là {0} có {1} sv đạt điểm A'.format(in_data[i, 0], maxa))
print('Lớp có ít điểm A là {0} có {1} sv đạt điểm A'.format(in_data[z, 0], mina))
print('Lớp có nhiều điểm F là {0} có {1} sv đạt điểm F'.format(in_data[j, 0], maxf))
print('Lớp có ít điểm F là {0} có {1} sv đạt điểm F'.format(in_data[a, 0], minf))

width = 0.1  # Độ rộng của mỗi cột
index = np.arange(len(diemA))  # Danh sách các chỉ mục

plt.bar(index, diemA, width=width, color="red",align='center', label="Diem A")
plt.bar(index + width, diemBc, width=width, color="blue",align='center', label="Diem B+")
plt.bar(index + 2 * width, diemB, width=width, color="green",align='center', label="Diem B")
plt.bar(index + 3 * width, diemCc, width=width, color="black",align='center', label="Diem C+")
plt.bar(index + 4 * width, diemC, width=width, color="pink",align='center', label="Diem C")
plt.bar(index + 5 * width, diemDc, width=width, color="yellow",align='center', label="Diem D+")
plt.bar(index + 6 * width, diemD, width=width, color="brown",align='center', label="Diem D")
plt.bar(index + 7 * width, diemF, width=width, color="purple",align='center', label="Diem F")

plt.xlabel('Lớp')
plt.ylabel('Số sinh viên đạt điểm')
plt.legend(loc='upper right')
plt.xticks(index + 3.5 * width, np.arange(len(diemA)))  # Đặt nhãn trục x cho từng lớp
plt.show()