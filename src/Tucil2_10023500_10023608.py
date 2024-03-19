import numpy as np
import matplotlib.pyplot as plt

def kuadrat_bezier_kurva(p0, p1, p2, t):
    # Fungsi untuk menghitung titik pada kurva Bézier kuadratik
    return (1 - t)**2 * p0 + (1 - t) * p1 + t**2 * p2

def brute_force_bezier_kurva(p0, p1, p2, nilai_t):
    # Metode Brute Force untuk menghitung titik pada kurva Bézier kuadratik
    kurva_point = []
    for t in nilai_t:
        q0 = (1 - t) * p0 + t * p1
        q1 = (1 - t) * p1 + t * p2
        r0 = (1 - t)**2 * p0 + (1 - t) *t * p1 + t**2 * p2
        kurva_point.append(r0)
    return np.array(kurva_point)

def divide_and_conquer_bezier_kurva(p0, p1, p2, nilai_t):
    # Metode Divide and Conquer untuk menghitung titik pada kurva Bézier kuadratik
    if len(nilai_t) == 1:
        return kuadrat_bezier_kurva(p0, p1, p2, nilai_t[0])
    else:
        t_mid = len(nilai_t) // 2 # Divide and conquer merupakan strategi algoritma dengan solusi bagi dua 
        kurva_kiri = divide_and_conquer_bezier_kurva(p0, p1, p2, nilai_t[:t_mid]) # Sehingga didapatlah titik tengah
        kurva_kanan = divide_and_conquer_bezier_kurva(p0, p1, p2, nilai_t[t_mid:])
        return np.vstack((kurva_kiri, kurva_kanan))

# Titik-titik kontrol

import numpy as np

# Input untuk titik p0
# Silahkan ganti x dan y yang diinginkan
p0 = np.array([6, 4]) 
p1 = np.array([3, 2])
p2 = np.array([4, 6])

# Menentukan jumlah iterasi
# Anda dapat memasukkan jumlah iterasi yang anda inginkan
jlh_iterasi = 10

# Header tabel iterasi
print("Tabel Iterasi:")
print("i\tt\tR0\t\tp0\t\tp1\t\tp2")

# Membuat array untuk menyimpan titik-titik iterasi
iterasi_point = []

# Membuat array parameter t
nilai_t = np.linspace(0, 1, jlh_iterasi + 1)

# Melakukan iterasi dan mencetak nilai t dan R0 pada setiap iterasi
for i, t in enumerate(nilai_t):
    r0 = (1 - t)**2 * p0 + (1 - t) * p1 + t**2 * p2
    print(f"{i}\t{t}\t{r0}\t{p0}\t{p1}\t{p2}")
    iterasi_point.append(r0)

# Membuat array parameter t untuk plot kurva Bézier kuadratik
nilai_t_plot = np.linspace(0, 1, 100)

# Menghitung titik pada kurva Bézier kuadratik dengan brute force
kurva_point_brute_force = brute_force_bezier_kurva(p0, p1, p2, nilai_t_plot)

# Menghitung titik pada kurva Bézier kuadratik dengan divide and conquer
kurva_point_divide_conquer = divide_and_conquer_bezier_kurva(p0, p1, p2, nilai_t_plot)

# Plotting kurva Bézier kuadratik dan titik-titik iterasi
plt.plot(kurva_point_brute_force[:, 0], kurva_point_brute_force[:, 1], label='Brute Force')
plt.plot(kurva_point_divide_conquer[:, 0], kurva_point_divide_conquer[:, 1], label='Divide and Conquer')
plt.scatter([p0[0], p1[0], p2[0]], [p0[1], p1[1], p2[1]], color='green', label='Titik Kontrol')
for i, txt in enumerate([p0, p1, p2]):
    plt.annotate(f'P{i}', (txt[0], txt[1]), textcoords="offset points", xytext=(0, 10), ha='center')
for i, txt in enumerate(iterasi_point):
    plt.annotate(f'R{i}', (txt[0], txt[1]), textcoords="offset points", xytext=(0, 10), ha='center')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Kurva Bézier Kuadrat dengan Divide and Conquer dan Brute Force') # Judul kurva
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show() # Menampilkan kurva

