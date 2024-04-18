from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import tkinter as tk
from tkinter import messagebox

# Khởi tạo trình duyệt WebDriver
driver = webdriver.Chrome()
# Mở URL cần kiểm tra
driver.get("https://stg-factory.smarthiz.vn")

# Tìm phần tử bằng XPath
element = driver.find_element(By.XPATH, '//*[@id="mat-input-0"]')

# Thực hiện thao tác click
element.click()

# Điền email vào ô nhập liệu
element.send_keys("employee7@gmail.com")

# Thực hiện thao tác click vào password và điền password
element = driver.find_element_by_xpath('//*[@id="mat-input-1"]')
element.click()
element.send_keys("Nothing@123")

# Thực hiện thao tác click vào submit
element = driver.find_element_by_xpath('/html/body/app-root/app-login/div/div/div[2]/button')

# Thực hiện thao tác click vào submit 

element.click()

# phóng to trình duyệt
driver.maximize_window()

# Đợi 3s
time.sleep(3)

# Danh sách các văn bản cần kiểm tra
texts_to_check = ["Mã nhân viên", "Tên nhân viên", "Số điện thoại", "Email", "Vị trí công tác", "Trạng thái hoạt động", "Thao tác", "Quản lý", "Tài khoản", "Tổng cộng", "kết quả"]

# Kiểm tra xem các văn bản có tồn tại trên trang web hay không
def check_text(texts_to_check):
    for text in texts_to_check:
        if text in driver.page_source:
            print(f"'{text}' được tìm thấy trên trang web.")
        else:
            error_flag = True
             # Nếu có lỗi, hiển thị popup báo lỗi
            root = tk.Tk()
            root.withdraw()  # Ẩn cửa sổ chính của Tkinter
            messagebox.showerror("Lỗi", f'"Không tìm thấy {text}!"')
            root.destroy()
            print(f"'{text}' KHÔNG được tìm thấy trên trang web.")
            error_flag = False
#Gọi hàm check
check_text(texts_to_check)

element = driver.find_element_by_xpath("/html/body/app-root/app-home/mat-drawer-container/mat-drawer-content/main/div[2]/div/app-employee/div/form/div/div[1]/div[1]/button/span[1]")
element.click()
time.sleep(1)

texts_to_check = ["Lọc tiêu chuẩn","Vị trí công tác","Trạng thái"]
#Gọi hàm check
check_text(texts_to_check)

#Bộ lọc vị trí công tác
element = driver.find_element_by_xpath('//*[@id="mat-select-value-7"]/span')
element.click()
element = driver.find_element_by_xpath('//*[@id="mat-option-3"]/span/input')
element.send_keys('Nhân viên OQC')
time.sleep(1)
element = driver.find_element_by_xpath('//*[@class="mat-option-text" and contains(text(), "Nhân viên OQC")]')
element.click()
time.sleep(1)
element = driver.find_element_by_xpath('//*[contains(text(), "Chọn trạng thái")]')
element.click()
time.sleep(1)
element = driver.find_element_by_xpath('//*[contains(text(), "Hoạt động ")]')
element.click()
time.sleep(1)
element = driver.find_element_by_xpath('//*[contains(text(), "Áp dụng")]')
element.click()

tk.Tk().withdraw()
messagebox.showinfo("Kết quả", "HOÀN THÀNH KIỂM TRA")
tk.Tk().destroy()
print("HOÀN THÀNH KIỂM TRA")