print("\n PROGRAM CHALL °F to °K & °K to °F \n")

#Memasukan Input untuk Output

kelvin = float(input('Masukan Suhu dalam Kelvin : '))

#Menampilkan hasil perintah

print ("\nSuhu adalah", kelvin, "°K \n")

#Konversi Ke °C lalu ke °F

k_c = (kelvin - 273)

c_f = ((9/5) * k_c) +32
print ('Suhu', kelvin, '°k dalam Fahrenheit =', c_f)

#Memasukan Input untuk Output (2)

fahren = float(input('\n \nMasukan Suhu dalam Fahrenheit : \n \n'))

#Menampilkan hasil perintah (2)

print ("\nSuhu adalah", fahren, "°F \n")

#konversi ke °C lalu ke °K

ke_c_s01 = 5/9
ke_c_s02 = ke_c_s01 * (fahren - 32)
print ('Suhu', fahren, '°F dalam Kelvin =', ke_c_s02)

