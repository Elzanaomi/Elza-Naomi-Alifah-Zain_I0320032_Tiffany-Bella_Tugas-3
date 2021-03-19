#dictionary
dict = {'Nama':'Elza Naomi Alifah Zain',
        'Hobi':['Menonton Film','Jajan','Menonton Youtube'],
        'Sosial Media':['Instagram : @Elzanazain','LinkedIn :  Elza Zain','Line : elzanaz21'],
        'Lagu Kesukaan':['Little Things','How Deep is Your Love','For You'],
        'Makanan Favorit':['Ayam Geprek','Ayam Hainan','Bakso']}
print(dict)
print("")

#ubah hobi dan sosial media
dict['Hobi'][1]= ('Mendengarkan Musik')
dict['Sosial Media'][1] = ('Twitter : @Elzanazain')

#hapus 2 makanan favorit
del dict['Makanan Favorit'][0:2]

#tambah 1 hobi
dict['Hobi'].append('Window Shopping')

#tampilan dictionary setelah diubah
print(dict)