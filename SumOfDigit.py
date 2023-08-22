"""Cho phép người dùng nhập vào 1 số. Tính tổng các chữ số của số đó.
VD: 252 có tổng các chữ số là 2+5+2 = 9
"""
def SumDigits(digit):
    """Hàm tính tổng các chữ số trong 1 số. 
    ý tưởng: Chia dư cho 10 lấy hàng đơn vị. Sau đó chia chia cho 10 lấy phần nguyên sau đó lại chia dư cho 10 lấy hàng chuc... lắp lại quá trình.
    Args:
        digit (int): số cần tính tổng các chữ số

    Returns:
        int: kết quả. 
    """
    sum = 0
    while(digit > 0):
        sum += digit % 10
        digit = int(digit / 10)
    return sum
n = input("Nhập số cần tính: ")
n = int(n) 
result = SumDigits(n)
print(f"Tổng các chữ số của số {n} là: {result}")
input("Press Enter to continue...")
