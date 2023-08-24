"""
bubble sort là thuật toán sắp xếp đơn giản nhất. DÙng để sắp xếp 1 dãy số từ thấp -> cao, hoặc cao -> thấp
video mo tả thuật toán bubble sort(Xem video trước): https://www.youtube.com/watch?v=9I2oOAr2okY&ab_channel=4GeeksAcademy
"""
def BubbleSort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]: # nếu phần tử đúng trước > phần tử đứng sau. thì đổi chỗ 2 phần tử. để phần tử nhỏ hơn về phía sau. 
                swapped = True   
                
                temp = arr[j]  # biến temp dùng làm trung gian.
                arr[j] = arr[j+1]
                arr[j+1] = temp

                #trong python có 1 cách viếtt gọn hơn để đổi chỗ ko dùng biến trung gian(nhiều ngôn ngữ ko hỗ trợ cách viết này):
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:  #sau khi chạy lượt 1 của vòng lặp. nếu swapped == false tức là ko có phần tử nào đứng trước lớn hơn phần tử đứng sau => chuỗi đã được sắp xếp. Thoát luôn. 
            return
 
arr = [64, 34, 25, 12, 22, 11, 90]    # đây gọi là 1 list. Dùng để lưu nhiều giá trị trong 1 biến. https://www.w3schools.com/python/python_lists.asp
BubbleSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("% d" % arr[i], end=" ")