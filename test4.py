import turtle as t 


t.shape("turtle")

n=100
t.bgcolor("black")  #문제의 요구사항에 따라 백그라운드 컬러 변경
t.color("green")    #문제의 요구사항에 따라 선 색 변경
t.speed(100)        #속도가 너무 답답해서 변경
for x in range(n):
    t.circle(100)   #원 크기 100으로 그리기
    t.left(360/n)   #원 개수에 따라 나누기