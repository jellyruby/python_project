#화씨온도를 섭씨온도로 치환하는 함수 
def getTemperatureC(temperatureF):
    return round((temperatureF-32)*(5/9))

#0에서 101 보다 작은경우 10씩 증가하여 반복
for i in range(0,101,10):
    print(i , "->" , getTemperatureC(i))
    