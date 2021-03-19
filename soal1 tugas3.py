#list 10 nama teman
list_teman = ['hasan', 'hafizh', 'rafli', 'ahmed', 'afin', 'abi', 'aron', 'abel', 'fakhri', 'ali']

#isi list index nomor 4,6,7
print("List indeks nomor 4,6, dan 7 adalah", list_teman[4], ",", list_teman[6], ", dan", list_teman[7])

#mengganti nama teman di list 3,5,9
list_teman[3] = 'ilham'
list_teman[5] = 'ayu'
list_teman[9] = 'ridho'

#tambahkan 2 teman
list_teman.append('rizky')
list_teman.append('naima')

#tampilkan semua teman setelah perulangan
print(list_teman * 2)

#tampilkan panjang list
print(len(list_teman))