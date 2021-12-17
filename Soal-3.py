#Soal-3
teori = int(input('Masukan Nilai Teori: '))
praktek = int(input('Masukan Nilai Praktek: '))
if teori >= 70 and praktek >= 70:
    print('Selamat, Anda Lulus')
elif teori >= 70 and praktek < 70:
    print('Anda harus mengulang ujian praktek')
elif teori < 70 and praktek >= 70:
    print('Anda harus mengulang ujian teori')
else: 
    print('Anda harus mengulang ujian teori dan praktek')