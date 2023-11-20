## Giới thiệu

Tên dự án: Histogram Equalization - Cân bằng mức xám
Phiên bản: 1.0

Dự án Histogram Equalization là một dự án mã nguồn mở cung cấp một thư viện Python để thực hiện cân bằng biểu đồ cho hình ảnh. Thư viện này sử dụng phương pháp cân bằng biểu đồ toàn cục để phân bố lại các giá trị cường độ pixel trong hình ảnh sao cho chúng được phân phối đồng đều hơn. Điều này có thể cải thiện độ tương phản của hình ảnh, làm cho các chi tiết nhỏ hơn dễ nhìn thấy hơn và làm cho hình ảnh trông tổng thể sáng hơn hoặc tối hơn.

Các tính năng chính của dự án bao gồm:
- Hỗ trợ cân bằng biểu đồ toàn cục cho hình ảnh xám.
- Cung cấp một số tùy chọn để điều chỉnh kết quả cân bằng biểu đồ.
- Được viết bằng Python và được tối ưu hóa để sử dụng hiệu quả.
![image](https://github.com/lastonton/Histogram_Equallization_Flask_SourceCode/assets/138580872/50e2f25a-b713-471d-b036-049ed213fcae)


## Hướng dẫn sử dụng

### Yêu cầu hệ thống
* Window, Linux, MacOs
* Python  version >= 3.9, opencv-python version 4.8.0, matplotlib version 3.7.1, seaborn version 0.12.2, pandas version 1.5.3, numpy version 1.23.5, Flask version 1.1.2
### Cách cài đặt

1. git clone https://github.com/lastonton/Histogram_Equallization_Flask_SourceCode.git
2. Tạo cây thư mục trong source đã clone về
-static
    -histogram
    -saveimages
    -uploads
3. Cài đặt các thư viên đã nêu ở yêu cầu hệ thống qua câu lệnh pip install
- https://www.python.org/downloads/ (Python dowload)
- pip install opencv-python==4.8.0
- pip install matplotlib==3.7.1
- pip install pandas==1.5.3
- pip install seaborn==0.12.2
- pip install numpy==1.23.5
- pip install flask==1.1.2


### Cách chạy

1. Mở file app.py trong IDLE hoăc Visual Studio Code
2. Chọn Run -> Starting Debugging hoặc F5 để khởi chạy ứng dụng

### Cách sử dụng

1. Khởi động websie và truy cập vào đường dẫn http://localhost:5000
2. Nhấn chọn Generate Histogram để vào giao diện chính xử lý cân bằng mức xám
![image](https://github.com/lastonton/Histogram_Equallization_Flask_SourceCode/assets/138580872/ca15dd10-f49e-4ccc-92a7-1936f179d39a)

3. Nhấn chọn Choose File và chọn hình ảnh cần xử lý
4. Kéo thanh Slider bên dưới hình đã qua xử lý để chọn mức sáng phù hợp với nhu cầu (mặc định là 255)
5. Nhấn chọn Upload and Render và chờ hệ thống xử lý
6. Hình ảnh sẽ được hiển thị sau khi hoàn thành xử lý và hình ảnh kết quả được lưu trong thư mục static/saveimages, biểu đồ trước và sau khi xử lý được lưu trong thư mục histogram
