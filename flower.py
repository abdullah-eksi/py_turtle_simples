import turtle

# Turtle modülünü içeri aktarıyoruz.

# Başlangıç pozisyonunu ayarlıyoruz
turtle.penup()  # Kalem kaldırılarak çizim yapılacak yer belirlenir.
turtle.left(90)  # Kaplumbağayı sola döndürür.
turtle.fd(200)  # İleri doğru 200 birim hareket ettirir.
turtle.pendown()  # Kalem tekrar kağıda indirilir.
turtle.right(90)  # Kaplumbağayı sağa döndürür.

# Çiçek tabanı çizimi
turtle.fillcolor("red")  # Dolgu rengini kırmızı olarak belirler.
turtle.begin_fill()  # Dolgu işlemi başlatılır.
turtle.circle(10, 180)  # 10 birim yarıçapında yarı daire çizer.
turtle.circle(25, 110)  # 25 birim yarıçapında 110 derece yay çizer.
turtle.left(50)  # 50 derece sola döner.
turtle.circle(60, 45)  # 60 birim yarıçapında 45 derece yay çizer.
turtle.circle(20, 170)  # 20 birim yarıçapında 170 derece yay çizer.
turtle.right(24)  # 24 derece sağa döner.
turtle.fd(30)  # İleri doğru 30 birim hareket eder.
turtle.left(10)  # 10 derece sola döner.
turtle.circle(30, 110)  # 30 birim yarıçapında 110 derece yay çizer.
turtle.fd(20)  # İleri doğru 20 birim hareket eder.
turtle.left(40)  # 40 derece sola döner.
turtle.circle(90, 70)  # 90 birim yarıçapında 70 derece yay çizer.
turtle.circle(30, 150)  # 30 birim yarıçapında 150 derece yay çizer.
turtle.right(30)  # 30 derece sağa döner.
turtle.fd(15)  # İleri doğru 15 birim hareket eder.
turtle.circle(80, 90)  # 80 birim yarıçapında 90 derece yay çizer.
turtle.left(15)  # 15 derece sola döner.
turtle.fd(45)  # İleri doğru 45 birim hareket eder.
turtle.right(165)  # 165 derece sağa döner.
turtle.fd(20)  # İleri doğru 20 birim hareket eder.
turtle.left(155)  # 155 derece sola döner.
turtle.circle(150, 80)  # 150 birim yarıçapında 80 derece yay çizer.
turtle.left(50)  # 50 derece sola döner.
turtle.circle(150, 90)  # 150 birim yarıçapında 90 derece yay çizer.
turtle.end_fill()  # Dolgu işlemi sonlandırılır.

# Taç yaprakları çizimi
turtle.left(150)  # 150 derece sola döner.
turtle.circle(-90, 70)  # -90 birim yarıçapında 70 derece yay çizer.
turtle.left(20)  # 20 derece sola döner.
turtle.circle(75, 105)  # 75 birim yarıçapında 105 derece yay çizer.
turtle.setheading(60)  # Kaplumbağanın yönelim açısını 60 derece olarak ayarlar.
turtle.circle(80, 98)  # 80 birim yarıçapında 98 derece yay çizer.
turtle.circle(-90, 40)  # -90 birim yarıçapında 40 derece yay çizer.

# Diğer taç yaprağı çizimi
turtle.left(180)  # 180 derece sola döner.
turtle.circle(90, 40)  # 90 birim yarıçapında 40 derece yay çizer.
turtle.circle(-80, 98)  # -80 birim yarıçapında 98 derece yay çizer.
turtle.setheading(-83)  # Kaplumbağanın yönelim açısını -83 derece olarak ayarlar.

# Yaprak 1 çizimi
turtle.fd(30)  # İleri doğru 30 birim hareket eder.
turtle.left(90)  # 90 derece sola döner.
turtle.fd(25)  # İleri doğru 25 birim hareket eder.
turtle.left(45)  # 45 derece sola döner.
turtle.fillcolor("green")  # Dolgu rengini yeşil olarak belirler.
turtle.begin_fill()  # Dolgu işlemi başlatılır.
turtle.circle(-80, 90)  # -80 birim yarıçapında 90 derece yay çizer.
turtle.right(90)  # 90 derece sağa döner.
turtle.circle(-80, 90)  # -80 birim yarıçapında 90 derece yay çizer.
turtle.end_fill()  # Dolgu işlemi sonlandırılır.
turtle.right(135)  # 135 derece sağa döner.
turtle.fd(60)  # İleri doğru 60 birim hareket eder.
turtle.left(180)  # 180 derece sola döner.
turtle.fd(85)  # İleri doğru 85 birim hareket eder.
turtle.left(90)  # 90 derece sola döner.
turtle.fd(80)  # İleri doğru 80 birim hareket eder.

# Yaprak 2 çizimi
turtle.right(90)  # 90 derece sağa döner.
turtle.right(45)  # 45 derece sağa döner.
turtle.fillcolor("green")  # Dolgu rengini yeşil olarak belirler.
turtle.begin_fill()  # Dolgu işlemi başlatılır.
turtle.circle(80, 90)  # 80 birim yarıçapında 90 derece yay çizer.
turtle.left(90)  # 90 derece sola döner.
turtle.circle(80, 90)  # 80 birim yarıçapında 90 derece yay çizer.
turtle.end_fill()  # Dolgu işlemi sonlandırılır.
turtle.left(135)  # 135 derece sola döner.
turtle.fd(60)  # İleri doğru 60 birim hareket eder.
turtle.left(180)  # 180 derece sola döner.
turtle.fd(60)  # İleri doğru 60 birim hareket eder.
turtle.right(90)  # 90 derece sağa döner.
turtle.circle(200, 60)  # 200 birim yarıçapında 60 derece yay çizer.
turtle.done()  # Çizim işlemi tamamlandı.
