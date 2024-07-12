from turtle import *

# Kırmızı kalem rengi ve beyaz arka plan ayarı
color("red")
bgcolor("white")

# Şeklin içini doldurma işlemi başlatılıyor
begin_fill()
pensize(4)  # Kalem kalınlığı ayarlanıyor

# İlk yay çiziliyor
left(50)
forward(133)
circle(50, 200)

# İkinci yay çiziliyor
right(140)
circle(50, 200)
forward(133)

# Şeklin içini doldurma işlemi tamamlanıyor
end_fill()

# "I LOVE YOU" yazısı siyah Verdana fontuyla ve kalın olarak yazdırılıyor
color("black")
write("I LOVE YOU", font=("verdana", 15, "bold"))

exitonclick()  # Çıkış yapmak için tıklanmasını bekleyen komut
