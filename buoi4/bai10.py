import tkinter as tk
from tkinter import ttk
from math import pi
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Đọc dữ liệu từ file CSV
df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = np.array(df.iloc[:, :])

# Lấy các dữ liệu cần thiết
arr_sv = in_data[:, 1]
diemA = in_data[:, 3]
diemBc = in_data[:, 4]
diemB = in_data[:, 5]
diemCc = in_data[:, 6]
diemC = in_data[:, 7]
diemDc = in_data[:, 8]
diemD = in_data[:, 9]
diemF = in_data[:, 10]
maxa = diemA.max()
i, = np.where(diemA == maxa)
mina = diemA.min()
z, = np.where(diemA == mina)
maxf = diemF.max()
j, = np.where(diemF == maxf)
minf = diemF.min()
a, = np.where(diemF == minf)
# Tạo cửa sổ chính
root = tk.Tk()
root.geometry("800x800")
root.title("Kết quả môn học")

# Hàm để hiển thị kết quả
def display_result():
    result_text.delete(1.0, tk.END)  # Xóa kết quả trước khi hiển thị mới

    result_text.insert(tk.END, "Tổng sinh viên tham gia môn học: {}\n".format(np.sum(arr_sv)))
    result_text.insert(tk.END, "Tbc sinh viên đạt A: {}\n".format(round(np.mean(diemA),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt B+: {}\n".format(round(np.mean(diemBc),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt B: {}\n".format(round(np.mean(diemB),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt C+: {}\n".format(round(np.mean(diemCc),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt C: {}\n".format(round(np.mean(diemC),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt D+: {}\n".format(round(np.mean(diemDc),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt D: {}\n".format(round(np.mean(diemD),2)))
    result_text.insert(tk.END, "Tbc sinh viên đạt F: {}\n".format(round(np.mean(diemF),2)))

    result_text.insert(tk.END, 'Lớp có nhiều điểm A là {0} có {1} sv đạt điểm A\n'.format(in_data[i, 0], maxa))
    result_text.insert(tk.END,'Lớp có ít điểm A là {0} có {1} sv đạt điểm A\n'.format(in_data[z, 0], mina))
    result_text.insert(tk.END,'Lớp có nhiều điểm F là {0} có {1} sv đạt điểm F\n'.format(in_data[j, 0], maxf) )
    result_text.insert(tk.END, 'Lớp có ít điểm F là {0} có {1} sv đạt điểm F\n'.format(in_data[a, 0], minf))

# Tạo nút để hiển thị kết quả
result_button = tk.Button(root, text="Hiển thị Kết Quả", command=display_result)
result_button.pack()

# Tạo Text widget để hiển thị kết quả
result_text = tk.Text(root, height=20, width=80)
result_text.pack()

# Thêm thư viện matplotlib vào giao diện tkinter
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Vẽ biểu đồ
width = 0.1
index = np.arange(len(diemA))

ax.bar(index, diemA, width=width, color="red", align='center', label="Diem A")
ax.bar(index + width, diemBc, width=width, color="blue", align='center', label="Diem B+")
ax.bar(index + 2 * width, diemB, width=width, color="green", align='center', label="Diem B")
ax.bar(index + 3 * width, diemCc, width=width, color="black", align='center', label="Diem C+")
ax.bar(index + 4 * width, diemC, width=width, color="pink", align='center', label="Diem C")
ax.bar(index + 5 * width, diemDc, width=width, color="yellow", align='center', label="Diem D+")
ax.bar(index + 6 * width, diemD, width=width, color="brown", align='center', label="Diem D")
ax.bar(index + 7 * width, diemF, width=width, color="purple", align='center', label="Diem F")

ax.set_xlabel('Lớp')
ax.set_ylabel('Số sinh viên đạt điểm')
ax.legend(loc='upper right')
ax.set_xticks(index + 3.5 * width)
ax.set_xticklabels(np.arange(len(diemA)))

# Hiển thị giao diện
root.mainloop()
