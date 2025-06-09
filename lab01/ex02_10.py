def dao_nguoc(chuoi):
    return chuoi[::-1]

# Sử dụng hàm và in kết quả
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
print("Chuỗi đảo ngược là:", dao_nguoc(input_string))
