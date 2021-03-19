#membuat program dictionary
dict = {'Nama':'Fagih','Hobi1':'Futsal','Hobi2':'Basket','Hobi3':'Bermain Game','Sosmed1':'ig:@fagih_','Sosmed2':'line:fagihbafagih','Sosmed3':'twitter:@ffaaggiihh','Lagu1':'Ruang Rindu','Lagu2':'Guru oemar Bakrie','Lagu3':'Monokrom','Makanan1':'Ayam Goreng','Makanan2':'Telur','Makanan3':'Ikan Bakar'}

# Mengubah salah satu hobi dan sosmed, hapus 2 makanan, dan tambah 1 hobi
dict['Hobi2'] = 'Menonton film'
dict['Sosmed3'] = 'snapchat:fagih13'
del dict['Makanan3']
del dict['Makanan2']
dict['Hobi4'] = 'bertemu teman'

print(dict)