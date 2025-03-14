# ptud-gk-de-1


## Thông tin cá nhân
- Họ và tên: Thân Trọng Tính
- MSSV: 22665711
- Lớp: PTUD
- Email: thantrongtinh12a1@gmail.com

## Hướng dẫn cài đặt project

### Yêu cầu:
- asgiref==3.8.1
- Django==5.1.7
- sqlparse==0.5.3
- typing_extensions==4.12.2
- tzdata==2025.1


# Blog Project PTUD
🚀 Giới thiệu
My Blog là một dự án blog được xây dựng bằng Django, hỗ trợ các tính năng quản lý bài viết, đăng ký người dùng, đăng nhập, đăng xuất, phân quyền rõ ràng (Editor, Collaborator, Viewer), giao diện trực quan, hiện đại và thân thiện người dùng.

🛠️ Các tính năng chi tiết

✅ Đăng ký tài khoản: Người dùng có thể tạo tài khoản mới trực tiếp trên website.

✅ Đăng nhập và Đăng xuất: Người dùng bắt buộc phải đăng nhập để sử dụng tính năng của website.

✅ Phân quyền người dùng:

Editor: Có đầy đủ quyền thêm, sửa, xóa bài viết.

Collaborator: Chỉ có quyền thêm và sửa bài viết, không được phép xóa.

Viewer: Chỉ có thể xem bài viết, không thể thêm, sửa hay xóa.

✅ Quản lý bài viết:

Thêm mới bài viết với tiêu đề và nội dung.

Chỉnh sửa bài viết hiện có.

Xóa bài viết theo quyền hạn.

✅ Sử dụng hình ảnh ngẫu nhiên từ Picsum.photos để minh họa cho từng bài viết.

✅ Giao diện được tổ chức gọn gàng bằng sidebar chứa các liên kết hữu ích.

📌 Công nghệ sử dụng

Backend: Django (Python)

Database: SQLite3 (database mặc định của Django)

Frontend: HTML, CSS

### Các bước cài đặt:

1. Clone dự án từ GitHub

2. Tạo môi trường ảo(sau đó kích hoạt môi trường ảo)
    ```
    python -m venv env
    env\Scripts\activate
    ```
    
3. Cài đặt các thư viện cần thiết
    ```
    pip install -r requirements.txt
    ```
4. Migrate database
    ```
    python manage.py migrate
    ```
5. Tạo superuser
    ```
    python manage.py createsuperuser
    ```
6. Chạy server
    ```
    python manage.py runserver
    ```
