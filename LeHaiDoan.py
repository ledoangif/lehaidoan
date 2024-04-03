'''
Gibhub
1, Tạo 1 project trong Github
2, Invite thành viên
training.huudungle@gmail.com (daica23)
3, tạo 1 file code TenSV.py
Ghi đề bài vào file
Commit 1
Lập trình giải đề bài
Commit lần 2
Đề bài : 
-Đọc 1 file văn bản gồm nhiều dòng
- Ghi ra màn hình theo thứ tự ngược lại của các dòng
Vd: Nam quốc sơn hà Nam đế cư
-> Nam đế cư Nam quốc sơn hà
'''
def reverse_display(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in reversed(lines):
            print(line.strip())

file_path = 'Lehaidoankt.txt'  # Thay đổi đường dẫn đến file của bạn
reverse_display(file_path)