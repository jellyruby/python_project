from tracemalloc import stop
import turtle


# 정다각형을 그린다.

def make_regular_Polygon(t, angle,length):
    def make_line(t):
        t.forward(length)
        t.right(360/angle)

    for i in range(1,abs(angle)+1):
        make_line(t)

# 몸체를 그린다.
def make_body(t):
    make_regular_Polygon(t,4,100)

#  지붕을 그린다.
def make_head(t):
    make_regular_Polygon(t,-3,100)
    
t = turtle.Pen()

make_body(t)
make_head(t)



    