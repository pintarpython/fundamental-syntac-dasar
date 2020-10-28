print('type data list/array')
anak = ['Eko', 'Dwi', 'Tri']
print(anak)
anak.append('Catur')
print(anak)

print('\nType data list, dengan looping')
for a in anak:
    print(f'Hai anak yg bernama {a}')

print('\nsapa anak ke 3')
print(anak[3])
print(f'Hai anak ke2 bernama {anak[3]}')

print('\nsapa anak dengan menggunakan fungsi len')
print(len(anak)) #menghitung jumlah anak dalam array
for a in range(0, len(anak)): #dimulai dari 0 krna agar data yg ditampilkan sesuai actual yaitu "4" (4-0)
    print(f'{a+1} Hai anak {anak[a]}')
