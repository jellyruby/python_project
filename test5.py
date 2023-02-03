import turtle as t 


t.shape("turtle")

angle = 91
n = 200
t.bgcolor("black")  #문제의 요구사항에 따라 백그라운드 컬러 변경
t.color("green")    #문제의 요구사항에 따라 선 색 변경
t.speed(100)        #속도가 너무 답답해서 변경

for x in range(n):
    t.forward(x)    #안쪽에서부터 조금씩 큰 선을 그려야하므로 X로 지정한다
    t.right(angle)   #조금씩 각도 변경하기
