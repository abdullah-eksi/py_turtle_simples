import turtle
# Turtle kütüphanesinden bir nesne oluşturuyoruz.
ucgen = turtle.Turtle()
ucgen2= turtle.Turtle()
ucgen3= turtle.Turtle()
ucgen4= turtle.Turtle()
# Kalem nesnesine renk veriyoruz
ucgen.pencolor("blue")
ucgen2.pencolor("red")
ucgen3.pencolor("blue")
ucgen4.pencolor("red")
#Kalem nesnesine kalınlık veriyoruz.
ucgen.pensize(2)
ucgen2.pensize(2)
ucgen3.pensize(2)
ucgen4.pensize(2)
# Kalem nesnesine çizim hızı veriyoruz
ucgen.speed(7)
ucgen2.speed(7)
ucgen3.speed(7)
ucgen4.speed(7)
# Döngü ile çizgi uzunluğu ve açısına göre çizim yaptırıyoruz.
for i in range(50):
    ucgen.forward(300)
    ucgen2.forward(300)
    ucgen3.forward(-300)
    ucgen4.forward(-300)
    ucgen.right(123)
    ucgen2.left(123)
    ucgen3.left(-123)
    ucgen4.right(-123)
turtle.done()
