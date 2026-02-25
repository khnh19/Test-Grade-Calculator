# Test Grade Calculator

Chương trình Python chấm điểm bài thi trắc nghiệm từ các file dữ liệu lớp học.

## Yêu cầu

- Python 3.x
- pandas

## Cài đặt

1. Clone repo này về máy:
   ```bash
   git clone https://github.com/khnh19/Test-Grade-Calculator.git
   cd Test-Grade-Calculator
   ```

2. Cài đặt thư viện:
   ```bash
   pip3 install pandas
   ```

## Chạy chương trình

```bash
python3 Nguyen_Khanh_grade_the_exams.py
```

Nhập tên lớp (ví dụ: `class1` cho `class1.txt`):

```
Enter a class file to grade (i.e. class1 for class1.txt): class1
Successfully opened class1.txt
```

## Tính năng

- **Mở file**: Nhắc người dùng nhập tên file cho đến khi hợp lệ, tự động thêm đuôi `.txt`.
- **Kiểm tra dữ liệu**: Phát hiện các dòng không hợp lệ (thiếu/thừa giá trị, sai định dạng mã số sinh viên).
- **Chấm điểm**: `+4` đúng, `0` bỏ qua, `-1` sai.
- **Thống kê**: Điểm trung bình, cao nhất, thấp nhất, miền giá trị, trung vị.
- **Xuất kết quả**: Tạo file `<lớp>_grades.txt` chứa mã số và điểm của từng học sinh.