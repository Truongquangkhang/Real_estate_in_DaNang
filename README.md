# Các thư viện cần của dự án
  + numpy (https://pypi.org/project/numpy/)
  + pandas (https://pypi.org/project/pandas2/)
  + matplotlib (https://pypi.org/project/matplotlib/)
  + seaborn (https://pypi.org/project/seaborn/)
  + re (https://pypi.org/project/regular-regexes/)
  + beautifulsoup4 (https://pypi.org/project/beautifulsoup4/)
  + Sklearn (https://pypi.org/project/scikit-learn/)
  + request (https://pypi.org/project/request2/)

Trang Web để Craw Data: https://alonhadat.com.vn/can-ban-nha-da-nang-t3.htm

### Cách crawl Data
- Chạy file Crawl_Data.ipynb, sau khi chạy xong dữ liệu mới đào được sẽ được thêm vào file raw_data.csv (>14000 sample)
- Tách file raw_data thành raw_SmallDS(>1000 sample) và raw_BigDS (>10000 sample)

### Chạy file Real_ESTATE.ipynb để thực hiện:
 - import file SmallDS.csv/BigDS.csv để chạy file
 - Clean data như loại bỏ nhưng ký tự đặc biệt, định dạng dữ liệu ...
 - Thực hiện Feature Engineering như xử lý dữ liệu trống, xử lý ngoại lệ ...
 - Tạo đặc trưng mới từ những đặc trưng cũ
    + sử dụng API BingMap
 - Dự án sử dụng 3 mô hình Linear Regression, Random Forest Regression, Decission Tree Regression
 - Đánh giá 3 mô hình theo 3 metrics R2_score, RMSE, MAE
