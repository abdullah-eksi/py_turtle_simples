from turtle import *

# Kütüphaneyi 't' olarak içeri aktarın (as t yerine direkt olarak from turtle import * kullanıldı)
# Kalem hızını değiştir
speed(1)

# Ekran rengini değiştir
bgcolor("black")

# Kalem kaldır (hareket etmeden çizim yapmayı sağlar)
penup()

# Kalem pozisyonunu değiştir
goto(-50, 60)

# Kalem iniyor (çizim yapmaya başlar)
pendown()

# Çizim rengini ayarla
color('#00adef')

# Şeklin içini doldurmak için başlangıcı işaretle
begin_fill()

# Pozisyonu değiştirerek çizim yap
goto(100, 100)
goto(100, -100)
goto(-50, -60)

# Başlangıç noktasına geri dönerek içi doldurmayı bitir
goto(-50, 60)
end_fill()

# "I LOVE YOU" yazısını siyah renkte yaz
color("black")
goto(15, 100)
color("black")
width(10)
goto(15, -100)

# Kalem kaldır
penup()

# Yeni bir çizim yapma pozisyonuna git
goto(100, 0)
pendown()

# Diğer taraftan başka bir çizim yapma pozisyonuna git
goto(-100, 0)

# Çizim işlemi bitir
done()
