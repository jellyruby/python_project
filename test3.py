from matplotlib import pyplot as plt

def bubble_sort(arr): 
    #탐색 범위 지정, 1부터 최대 크기-1까지 지정하면 된다.(당장 크기 비교를 하는 반복이 아니다. 0부터 X까지 탐색을 한다. 라는 크기 지정 반복문) 
    #버블 정렬은 가장큰 항목이 맨 뒤부터 정렬되기에 다음과같이 가능.
    
    plt.show()
    for i in range(len(arr) - 1, 0, -1): 
        for j in range(i):
            if arr[j] > arr[j + 1]: # 크기 비교 후, 현재 index가 가지고 있는 값이 더 클때 실행하는 조건문
                arr[j], arr[j + 1] = arr[j + 1], arr[j] #2개의 항목 위치 변경
                
                plt.bar(range(len(arr)), arr)
                plt.draw()
                plt.pause(1)
                plt.clf()
    return arr



sorted_arr = bubble_sort([90,10,23,17,56,39])


print(sorted_arr)






