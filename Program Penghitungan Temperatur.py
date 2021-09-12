print("\nProgram Penghitungan Temperatur\n")

celcius = float(input('Masukan Suhu dalam Celcius : '))
print ("\nSuhu adalah", celcius, "Celsius\n")

#Konversi Ke Reamur
reamur = (4/5) * celcius
print ('Suhu', celcius, '°C dalam reamur =', reamur)

#Konversi Ke Fahrenheit
fahren = ((9/5) * celcius) +32
print ('Suhu', celcius, '°C dalam Fahrenheit =', fahren)

#Konversi Ke Kelfin
kel = celcius + 273
print ('Suhu', celcius, '°C dalam Kelfin =', kel)

