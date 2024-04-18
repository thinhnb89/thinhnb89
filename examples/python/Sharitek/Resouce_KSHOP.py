import random
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time
import tkinter as tk
from tkinter import messagebox
from selenium.webdriver.support.wait import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC #type: ignore

# Khởi tạo trình duyệt WebDriver
driver = webdriver.Chrome()

def clickOnElement_by_xpath(xpath):
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    element = driver.find_element_by_xpath(xpath)
    element.click()

def inputTextOnElement_by_xpath_ID(type, arrgument, text):
    time.sleep(0.2)
    if type == "xpath":
        element = driver.find_element_by_xpath(arrgument)
    elif type == "ID":
        element = driver.find_element(By.ID, arrgument)
    element.clear()
    element.send_keys(text)

def cmsNotification(noti):
    clickOnElement_by_xpath('//*[@type = "button" and contains(text(),"Lưu")]')
    time.sleep(0.7)
    if noti in driver.page_source:
        print("CMS thông báo ĐÚNG")
    else:
        messagebox.showerror("CÓ LỖI","CMS thông báo SAI")

def page_Should_contain_text(textList):
    for i in textList:
        try:
            element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, f'//*[contains(text(), "{i}")]')))
            print(f'Element with text "{i}" found.')
        except Exception as e:
            print(f'Element with text "{i}" NOT found. Error: {e}')
            tk.Tk().withdraw()
            messagebox.showinfo("CÓ LỖI",f'Text "{i}" NOT found')
            tk.Tk().destroy()
def Login_KShop(cms_url,email,password,textCheck):
    driver.get(cms_url)
    inputTextOnElement_by_xpath_ID("ID","email",email)
    inputTextOnElement_by_xpath_ID("ID","password",password)
    clickOnElement_by_xpath("//button[@type='submit']")
    driver.maximize_window()
    try:
        element = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//*[contains(text(), '{textCheck}')]"))
            )
        print("Đăng nhập THÀNH CÔNG")
    except Exception as E:
        messagebox.showinfo("CÓ LỖI","Đăng nhập THẤT BẠI")

Login_KShop("https://stg-kshop.karofi.com/login","thi_truong_stg@gmail.com","abc123",'Admin Nghiên cứu thị trường')

#Mở rộng menu KTEAM
clickOnElement_by_xpath('//*[@id="main-page"]/div[1]/app-sidebar/div/div[2]/app-collapse/div[1]/div/span[contains(text(), "K-Team")]')

clickOnElement_by_xpath('//*[contains(text(), "Khảo sát")]')

danhSachKhaoSat_List = ["Nhập tìm kiếm","Ngày tạo","Thời gian bắt đầu","Thời gian kết thúc","Trạng thái","Trạng thái hoạt động","STT","Tên khảo sát","Mô tả","Đơn vị áp dụng","Thời gian tạo","Thời gian bắt đầu","Thời gian kết thúc","Tiến trình khảo sát","Trạng thái","Hoạt động","Tác vụ","Tổng cộng"]


page_Should_contain_text(danhSachKhaoSat_List)

#tìm kiếm và kiểm tra

try:
    inputTextOnElement_by_xpath_ID("xpath",'//*[@id="mat-input-0"]',"chị một chút được không ah?")
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[2]/form/div/div[7]/button/span[contains(text(),"Tìm kiếm")]')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[3]/table/tbody/tr[1]/td[3][contains(text(),"chị một chút được không ah?")]')))
    print ("Tìm kiếm theo keyword mô tả THÀNH CÔNG")
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-21-input"][@aria-checked="true"]')))
    print ("Trạng thái là ACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-21"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-21-input"][@aria-checked="false"]')))
    print ("Trạng thái được chuyển sang INACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-21"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-21-input"][@aria-checked="true"]')))
    print ("Trạng thái trở lại là ACTIVE")
except Exception as e:
    print ("Tìm kiếm theo keyword mô tả THẤT BẠI")

#Kiểm tra màn Thêm mới khảo sát
clickOnElement_by_xpath('//*[contains(text(),"Thêm mới")]')

danhSachThemMoi_List = ["Thông tin cơ bản", "Cấu hình", "Người nhận báo cáo", "Người nhận báo cáo ", "Không giới hạn", "lượt","Tên khảo sát ", "Mô tả ", "Đơn vị áp dụng "]
page_Should_contain_text(danhSachThemMoi_List)


try:
    cmsNotification('Trường bắt buộc không được trống')
    #tab Hoạt động
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-28-input"][@aria-checked="true"]')))
    print ("Trạng thái HOẠT ĐỘNG là ACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-28"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-28-input"][@aria-checked="false"]')))
    print ("Trạng thái HOẠT ĐỘNG chuyển sang INACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-28"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-28-input"][@aria-checked="true"]')))
    print ("Trạng thái HOẠT ĐỘNG trở lại là ACTIVE")
    #tab Thời gian ngày bắt đầu, chọn ngày m1
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-29-input"][@aria-checked="false"]')))
    print ("Trạng thái Ngày Bắt Đầu là INACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-29"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-29-input"][@aria-checked="true"]')))
    print ("Trạng thái Ngày Bắt Đầu chuyển sang ACTIVE")
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[1]/div/div[2]/form/div[1]/mat-form-field[2]/div/div[1]/div/mat-datepicker-toggle')
    clickOnElement_by_xpath('//*[@id="mat-datepicker-3"]/div/mat-month-view/table/tbody/tr[2]/td[2]')
    #tab Thời gian ngày Kết thúc, chọn ngày m17
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-30-input"][@aria-checked="false"]')))
    print ("Trạng thái Ngày Kết thúc là INACTIVE")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-30"]/label/div')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-slide-toggle-30-input"][@aria-checked="true"]')))
    print ("Trạng thái Ngày Kết thúc chuyển sang ACTIVE")
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[1]/div/div[2]/form/div[1]/mat-form-field[4]/div/div[1]/div/mat-datepicker-toggle')
    clickOnElement_by_xpath('//*[@id="mat-datepicker-4"]/div/mat-month-view/table/tbody/tr[4]/td[4]')
    #Nhập số lượt
    clickOnElement_by_xpath('//*[@id="mat-radio-3"]/label/span[1]/span[1]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-6","12345678")
    print("Nhập số lượt thành công")
    #Nhập tên khảo sát bị trùng
    inputTextOnElement_by_xpath_ID("ID","mat-input-7","1")
    print("Nhập tên khảo sát thành công")
    cmsNotification('Trường bắt buộc không được trống')
    #Nhập mô tả
    inputTextOnElement_by_xpath_ID("ID","mat-input-8","Đây là mô tả")
    print("Nhập mô tả thành công")
    cmsNotification('Trường bắt buộc không được trống')
    #Chọn agency
    clickOnElement_by_xpath('//*[@id="mat-select-value-5"]/span')
    inputTextOnElement_by_xpath_ID("xpath",'//*[@id="mat-option-7"]/span/input','vIệT')
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="mat-option-28"]/span')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[1]/div/div[2]/form/div[6]/div/span[contains(text(),"AGENCY0035 -  Tên Tiếng Việt")]')))
    print("Chọn agency thành công")
    #bấm Lưu
    cmsNotification('Cấu hình không được trống')
    #Thêm cấu hình kiểu văn bản
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[1]/span[contains(text(),"Văn bản")]')
    vanban_List = ["Thêm trường văn bản","Tên trường","Mô tả trường thông tin"]
    page_Should_contain_text(vanban_List)
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Văn bản không bắt buộc")
    inputTextOnElement_by_xpath_ID("ID","mat-input-11","Mô tả của Văn bản không bắt buộc")
    clickOnElement_by_xpath('//*[@type="submit"][contains(text(),"Lưu")]')
    print("Thêm văn bản 1 thành công")    
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[1]/span[contains(text(),"Văn bản")]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Văn bản bắt buộc")
    inputTextOnElement_by_xpath_ID("ID","mat-input-11","Mô tả của Văn bản bắt buộc")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-31"]/label/div')
    clickOnElement_by_xpath('//*[@id="mat-dialog-1"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Thêm văn bản thành công")    
    #Thêm cấu hình Thời gian
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[2]/span[contains(text(),"Thời gian")]')
    thoigian_List = ["Thêm trường thời gian","Tên trường"]
    page_Should_contain_text(thoigian_List)
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Thời gian không bắt buộc + KO chọn đc quá khứ")
    clickOnElement_by_xpath('//*[@id="mat-dialog-2"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Thêm cấu hình Thời gian 1 thành công")
    time.sleep(0.5)    
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[2]/span[contains(text(),"Thời gian")]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Thời gian bắt buộc + Chọn đc quá khứ")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-32"]/label/div/div')
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-31"]/label/div/div/div[1]')
    clickOnElement_by_xpath('//*[@id="mat-dialog-3"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Thêm cấu hình Thời gian thành công")
       
    #Thêm cấu hình Danh sách 1 chọn
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[3]/span[contains(text(),"Danh sách")]')
    danhSach_List = ["Thêm trường danh sách","Tên trường","Loại danh sách","Danh sách lựa chọn"]
    page_Should_contain_text(danhSach_List)
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Danh sách không bắt buộc + 1 chọn")
    clickOnElement_by_xpath('//*[@id="mat-select-value-9"]/span')
    clickOnElement_by_xpath('//*[@id="mat-option-29"]/span[contains(text(),"Danh sách 1 chọn")]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-13","a,a,a")
    clickOnElement_by_xpath('//*[@id="mat-dialog-4"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Thêm cấu hình Danh sách 1 chọn thành công")
    #Thêm cấu hình Danh sách nhiều chọn
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[2]/div/div[2]/button[3]/span[contains(text(),"Danh sách")]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-9","Danh sách bắt buộc + nhiều chọn")
    clickOnElement_by_xpath('//*[@id="mat-select-value-9"]/span')
    clickOnElement_by_xpath('//*[@id="mat-option-30"]/span[contains(text(),"Danh sách nhiều chọn")]')
    inputTextOnElement_by_xpath_ID("ID","mat-input-13","a,a,a")
    clickOnElement_by_xpath('//*[@id="mat-slide-toggle-31"]/label/div/div')
    clickOnElement_by_xpath('//*[@id="mat-dialog-5"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Thêm cấu hình Danh sách nhiều chọn thành công")
    #cmsNotification('Thực hiện thất bại')
    clickOnElement_by_xpath('//*[@type = "button" and contains(text(),"Lưu")]')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="mat-dialog-6"]/div/div[1]/div[contains(text(),"Tên mẫu khảo sát đã tồn tại")]')))
    clickOnElement_by_xpath('//*[@id="mat-dialog-6"]/div/div[2]/button[contains(text(),"Đóng")]')
    print("Kiểm tra xong về Tên mẫu khảo sát đã tồn tại")
    #Sửa tên khảo sát không bị trùng
    ran = str(random.random())
    inputTextOnElement_by_xpath_ID("ID","mat-input-7",ran)
    clickOnElement_by_xpath('//*[@type = "button" and contains(text(),"Lưu")]')
    print("Sửa tên khảo sát thành công")
    #Sửa lại list 1 chọn
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="mat-dialog-7"]/div/div[1]/div[contains(text(),"chứa lựa chọn trùng lặp")]')))
    clickOnElement_by_xpath('//*[@id="mat-dialog-7"]/div/div[2]/button[contains(text(),"Đóng")]')
    clickOnElement_by_xpath('//*[@id="0"]/div[5]/div[1]/div/button[2]/i')
    inputTextOnElement_by_xpath_ID("ID","mat-input-13","a1,a2,a3")
    clickOnElement_by_xpath('//*[@id="mat-dialog-8"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Sửa lại list 1 chọn thành công")
    #Sửa lại list nhiều chọn
    clickOnElement_by_xpath('//*[@type = "button" and contains(text(),"Lưu")]')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="mat-dialog-9"]/div/div[1]/div[contains(text(),"chứa lựa chọn trùng lặp")]')))
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="mat-dialog-9"]/div/div[2]/button[contains(text(),"Đóng")]')
    clickOnElement_by_xpath('//*[@id="0"]/div[6]/div/div/button[2]/i')
    inputTextOnElement_by_xpath_ID("ID","mat-input-13","b1,b2,b3")
    clickOnElement_by_xpath('//*[@id="mat-dialog-10"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    cmsNotification('Thêm tờ phê duyệt thành công')
    print("Đã tạo xong phê duyệt mới")
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[3]/table/tbody/tr[1]/td[2][contains(text(),"{ran}")]')))
    print("Đã check tên khảo sát mới")
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[3]/table/tbody/tr[1]/td[11]/div/button')
    #Bắt đầu cập nhật, thêm Agency
    clickOnElement_by_xpath('//*[@id="mat-menu-panel-30"]/div/button[1][contains(text(),"Cập nhật")]')
    print("Đã bấm cập nhật")
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="mat-select-value-15"]/span')
    inputTextOnElement_by_xpath_ID("xpath",'//*[@id="mat-option-38"]/span/input','QA_Agency')
    time.sleep(0.5)
    clickOnElement_by_xpath('//*[@id="mat-option-60"]/span')
    element = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main-page"]/div[2]/div[2]/app-survey-create/div/div[1]/div[1]/div/div[2]/form/div[6]/div[2]/span[contains(text(),"AGENCY0004 -  QA_Agency_Do not Inactive")]')))
    print("Thêm agency thành công")
    #Sửa lại list 1 chọn lần 2
    clickOnElement_by_xpath('//*[@id="0"]/div[5]/div[1]/div/button[2]/i')
    inputTextOnElement_by_xpath_ID("ID","mat-input-25","a11,a22,a33")
    clickOnElement_by_xpath('//*[@id="mat-dialog-11"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    print("Sửa lại list 1 chọn lần 2 thành công")
    #Sửa lại list nhiều chọn
    clickOnElement_by_xpath('//*[@id="0"]/div[6]/div/div/button[2]/i')
    inputTextOnElement_by_xpath_ID("ID","mat-input-25","b11,b22,b33")
    clickOnElement_by_xpath('//*[@id="mat-dialog-12"]/div/div[3]/button[2][contains(text(),"Lưu")]')
    #bấm Lưu
    cmsNotification('Cập nhật tờ phê duyệt thành công')
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[3]/table/tbody/tr[1]/td[4]/a')
    donVi_List = ["Danh sách đơn vị áp dụng","STT","Mã đơn vị","Tên đơn vị","Trạng thái","AGENCY0035","Tên Tiếng Việt","AGENCY0004","QA_Agency_Do not Inactive","Hoạt động"]
    page_Should_contain_text(donVi_List)
    clickOnElement_by_xpath('//*[@id="mat-dialog-13"]/div/div[3]/button')
    #Kiểm tra tính năng Sao chép
    clickOnElement_by_xpath('//*[@id="main-page"]/div[2]/div[2]/app-survey/div/div[3]/table/tbody/tr[1]/td[11]/div/button')
    clickOnElement_by_xpath('//*[@id="mat-menu-panel-51"]/div/button[2][contains(text(),"Sao chép")]')
    clickOnElement_by_xpath('//*[@type = "button" and contains(text(),"Lưu")]')
    time.sleep(1)
    clickOnElement_by_xpath('//*[@id="mat-dialog-14"]/div/div[2]/button[contains(text(),"Đóng")]')
    ran = str(random.random())
    inputTextOnElement_by_xpath_ID("ID","mat-input-33",ran)
    cmsNotification('Thêm tờ phê duyệt thành công')
    
    print ("Test Script PASS")
except Exception as e:
    print ("Test Script FAIL")

