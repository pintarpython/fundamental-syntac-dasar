"""
Type data Dictionary hanya sekedar menghubungkan KEY dan VALUE
KVP = KEY VALUE PAIR
"""

kamus = {}
kamus['anak'] = 'son'
kamus['istri'] = 'wife'
kamus['ayah'] = 'father'

print(kamus)
print(kamus['ayah'])

print('\nData ini dikirimkan server gojek, memberikan info driver di sekitar pemakai aplikasi')
data_server_gojek = {
    'tanggal': '2020-10-27',
    'driver_list': [  # diver_list merupakan array yang bertipe dictionary krna memiliki beberapa atribut
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 100},
        {'nama': 'Tri', 'jarak': 1000}
    ]
}
print(data_server_gojek)
print(f"Driver di sekitar sini {data_server_gojek['driver_list']}")
print(f"Driver #1 {data_server_gojek['driver_list'][0]}")
print(f"Driver #3 {data_server_gojek['driver_list'][2]}")

print('\nCara mengambil data jarak terdekat')
print(f"jarak driver terdekat {data_server_gojek['driver_list'][0]['jarak']} meter")
