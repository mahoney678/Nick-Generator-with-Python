#sesli_harfler = input("sesli harfler giriniz(tr karakter hariç) : ") alternatif kullanılabılır
#sessiz_harfler = input("sessiz harfler giriniz(tr karakter hariç) : ") alternatif kullanılabılır
sesli_harfler = "aeiuo"
sessiz_harfler = "bcdfghjklmnprstvxyz"

nick_generate = []
import random

b = sessiz_harfler[random.randint(0,18)]
a = sesli_harfler[random.randint(0,4)]
d = sessiz_harfler[random.randint(0,17)]
bx = sessiz_harfler[random.randint(0,18)] + sessiz_harfler[random.randint(1,17)]
c = sesli_harfler[random.randint(0,3)]
ax = sesli_harfler[random.randint(0,1)] + sessiz_harfler[random.randint(0,18)]
az = sessiz_harfler[random.randint(0,18)] + sesli_harfler[random.randint(0,2)]
bz = sesli_harfler[random.randint(1,4)] + sessiz_harfler[random.randint(0,18)]

# kullanici_degeri = int(input("Nickinizin daha güzel olması için uğurlu sayınız (girmek zorunlu*) : "))
kullanici_degeri = 7

nick_parameters = b,a,d,bx,c,ax,az,bz
print ("**********************************************")

print ("üretilen nick : ",nick_parameters[random.randint(0,kullanici_degeri)] + nick_parameters[random.randint(0,kullanici_degeri)]+nick_parameters[random.randint(0,kullanici_degeri)] + nick_parameters[random.randint(0,kullanici_degeri)])

print ("**********************************************")
