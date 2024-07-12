from turtle import *

# Tüm öğeleri turtle kütüphanesinden içeri aktar

# Kalem hızını değiştir
speed(20)

# İstenilen konuma gitmek için fonksiyon tanımla
def insta1(x, y):
    penup()     # Kalemi kaldır
    goto(x, y)  # Belirtilen koordinatlara git
    pendown()   # Kalemi indir

# Kare çizimi fonksiyonu tanımla
def insta2(x, y, f, c, c1, c2):
    color(c)        # Renk ayarla
    insta1(x, y)    # İstenilen konuma git
    begin_fill()    # İçi doldurmayı başlat
    for i in range(4):
        forward(f)      # Belirtilen uzunlukta ilerle
        circle(c1, c2)  # Belirtilen yarıçap ve açıda daire çiz
    end_fill()      # İçi doldurmayı bitir

# Daire çizimi fonksiyonu tanımla
def insta3(c, x, y, c1):
    color(c)        # Renk ayarla
    begin_fill()    # İçi doldurmayı başlat
    insta1(x, y)    # İstenilen konuma git
    circle(c1)      # Belirtilen yarıçapta daire çiz
    end_fill()      # İçi doldurmayı bitir

# Kontroller
insta2(-150, -120, 350, "pink", 20, 90)    # Büyük pembe kare çizimi
insta2(-110, -70, 260, "white", 20, 90)    # Orta boy beyaz kare çizimi
insta2(-90, -50, 220, "pink", 20, 90)      # Küçük pembe kare çizimi
insta3("white", 20, 10, 70)                # Beyaz daire çizimi
insta3("pink", 20, 30, 50)                 # Pembe daire çizimi
insta3("white", 110, 160, 15)              # Küçük beyaz daire çizimi

hideturtle()    # Kaplumbağayı gizle
done()          # Çizimi tamamla
