*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        chrome

*** Test Cases ***
CDP_menu_Bitrix_3
    Open Browser    https://stg-crm.smarthiz.vn/    ${BROWSER}
    Sleep    3s
    Wait Until Page Contains Element    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input
    Input Text    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input    cskh1@smarthiz.com
    Input Text    xpath=//*[@id="crmPassword"]    123456
    Click Element    xpath=//button[contains(text(), "Đăng nhập")]
    Sleep    7s
    Maximize Browser Window
    Comment    Click Element    xpath=//button[contains(text(), 'Allow')]
    Click Element    xpath=//*[@id="mainDiv"]/div[2]/img
    Click Element    xpath=//*[contains(text(),"Bitrix")]
    ${id_su_vu}    Set Variable    1151907
    Input Text    xpath=//*[@id="main-page"]/div[2]/div[2]/div/div/app-bitrix/div/form/div/div/div/input    ${id_su_vu}
    Sleep    3s
    Click Element    xpath=//*[@role="gridcell"][contains(text(), "${id_su_vu}")]
    Comment    @{crm_field}    Create List    Thông tin sự vụ    Chi tiết sự vụ    Kênh tiếp nhận:    Nhóm yêu cầu:    Loại yêu cầu:    Độ ưu tiên:    Mô tả sự vụ:    Kết quả hỗ trợ sơ bộ:    Ảnh sản phẩm:    Lý do quá hạn:    Ghi chú:    Thời gian hoàn thành:    Họ và tên:    Mã KH Core:
    ...    ID khách hàng:
    Comment    ...    Số điện thoại 1:    Số điện thoại 2:    Số điện thoại 3:    Địa chỉ:    Tên sản phẩm:    Serial:    Hãng:    Ngày sản xuất:    Ngày mua:    Tên KTV:    Sđt KTV:    Email:    Địa chỉ:    Hình thức bảo hành:    Tên sản phẩm:
    ...    Serial:
    Comment    ...    Ngày sản xuất:    Ngày mua:    Nhóm lỗi:    Nguyên nhân lỗi:    Đánh giá lỗi:    Cách xử lý:    Ghi chú:    Báo cáo KTV:    Mã yêu cầu:    Nhân viên CSKH tiếp nhận:    Thời gian hẹn xử lý:    Tiến độ hoàn thành:    Lý do hủy:    Product time:    Checkout location:
    ...    Checkin time:
    Comment    ...    XLSC Lý do quá hạn:    Ngày mua sản phẩm:    XLSC Doanh thu linh kiện:    XLSC Doanh thu dịch vụ:    Thời gian CSKH tiếp nhận:    Bộ phận xử lý:    KQ CS sơ bộ:    Lưu ý thông tin lỗi linh kiện:    Nội dung xử lý chi tiết:    Checkin location:    Checkout time:    XLSC Cách thức xử lý:    XLSC Km di chuyển:    XLSC Doanh thu sản phẩm:    Trưởng BP bảo trì:
    Comment    Sleep    2s
    Comment    FOR    ${var_crm_field}    IN    @{crm_field}
        Comment    Wait Until Page Contains    ${var_crm_field}
    Comment    END
    @{bitrix_field}    Create List    ${id_su_vu}    ĐL Huy Sơn    21417    \    0988378882    Bắc Ninh    Lương Tài    Mỹ Hương    An Mỹ    05/09/2022 13:23:22    Tổng đài    báo \ sự cố kh đỗ đăng điển 0397525436    Bùi Thị Phượng    CSKH Inbound    CCTT
    ...    Lẫn tạp    Bình thường    KRF    \    \    \    Hoàn thành XLSC    02/06/2020
    FOR    ${var_bitrix_field}    IN    @{bitrix_field}
        Wait Until Page Contains    ${var_bitrix_field}
    END
    Comment    Sửa chữa tại nhà    Đặng Trường Phú    12.222727_109.0846768

CDP_menu_Bitrix_2
    Open Browser    https://stg-crm.smarthiz.vn/login    ${BROWSER}
    Sleep    5s
    Wait Until Page Contains Element    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input
    Input Text    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input    cskh1@smarthiz.com
    Input Text    xpath=//*[@id="crmPassword"]    123456
    Click Element    xpath=//button[contains(text(), "Đăng nhập")]
    Sleep    5s
    Maximize Browser Window
    Comment    Click Element    xpath=//button[contains(text(), 'Allow')]
    Click Element    xpath=//*[@id="mainDiv"]/div[2]/img
    Click Element    xpath=//*[contains(text(),"Bitrix")]
    ${id_su_vu}    Set Variable    1893118
    Input Text    xpath=//*[@id="main-page"]/div[2]/div[2]/div/div/app-bitrix/div/form/div/div/div/input    ${id_su_vu}
    Sleep    3s
    Click Element    xpath=//*[@role="gridcell"][contains(text(), "${id_su_vu}")]
    @{crm_field}    Create List    Thông tin sự vụ    Chi tiết sự vụ    Kênh tiếp nhận:    Nhóm yêu cầu:    Loại yêu cầu:    Độ ưu tiên:    Mô tả sự vụ:    Kết quả hỗ trợ sơ bộ:    Ảnh sản phẩm:    Lý do quá hạn:    Ghi chú:    Thời gian hoàn thành:    Họ và tên:    Mã KH Core:    ID khách hàng:
    ...    Số điện thoại 1:    Số điện thoại 2:    Số điện thoại 3:    Địa chỉ:    Tên sản phẩm:    Serial:    Hãng:    Ngày sản xuất:    Ngày mua:    Tên KTV:    \    Email:    Địa chỉ:    Hình thức bảo hành:    Tên sản phẩm:    Serial:
    ...    Ngày sản xuất:    Ngày mua:    Nhóm lỗi:    Nguyên nhân lỗi:    Đánh giá lỗi:    Cách xử lý:    Ghi chú:    \    Mã yêu cầu:    Nhân viên CSKH tiếp nhận:    Thời gian hẹn xử lý:    Tiến độ hoàn thành:    Lý do hủy:    Product time:    Checkout location:    Checkin time:
    ...    XLSC Lý do quá hạn:    Ngày mua sản phẩm:    XLSC Doanh thu linh kiện:    XLSC Doanh thu dịch vụ:    Thời gian CSKH tiếp nhận:    Bộ phận xử lý:    KQ CS sơ bộ:    Lưu ý thông tin lỗi linh kiện:    Nội dung xử lý chi tiết:    Checkin location:    Checkout time:    XLSC Cách thức xử lý:    XLSC Km di chuyển:    XLSC Doanh thu sản phẩm:    Trưởng BP bảo trì:
    Sleep    2s
    FOR    ${var_crm_field}    IN    @{crm_field}
        Wait Until Page Contains    ${var_crm_field}
    END
    @{bitrix_field}    Create List    ${id_su_vu}    Thái Đại Lạc    78949    0340829    0909345975    Gia Lai    Pleiku    Hội Phú    369 Lê Thánh Tông    25/02/2024 15:28:00    Tổng đài    Máy bị rò nước trong máy - mua 3,4 năm    Nguyễn Thiều Hoa    CSKH Inbound    XLSC chung
    ...    Rò nước    Bình thường    KRF    Máy lọc nước KAROFI K9IQ-2    Lõi lọc phụ trợ lỗi -1    Chuyển tiếp BHBT sự cố    Hoàn thành XLSC    27/02/2024 09:59:00    Lõi phụ trợ nối nhanh rò nước do hạt nối nhanh lỗi    27/05/2018    13.952952761815629_107.99698469926626    27/02/2024 09:59:00    27/02/2024 09:48:00    gắn lại cút nối vòi cổ ngỗng    27/10/2018    25/02/2024 15:28:00
    ...    Quản lý khu vực MN4    150000
    FOR    ${var_bitrix_field}    IN    @{bitrix_field}
        Wait Until Page Contains    ${var_bitrix_field}
    END
    Comment    Sửa chữa tại nhà    Đặng Trường Phú    12.222727_109.0846768    Sđt KTV:    Báo cáo KTV:

CDP_menu_Bitrix
    Open Browser    https://stg-crm.smarthiz.vn/login    ${BROWSER}
    Sleep    5s
    Wait Until Page Contains Element    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input
    Input Text    xpath=/html/body/app-root/app-login/main/div/div/form/div/div[1]/input    cskh1@smarthiz.com
    Input Text    xpath=//*[@id="crmPassword"]    123456
    Click Element    xpath=//button[contains(text(), "Đăng nhập")]
    Sleep    5s
    Maximize Browser Window
    Comment    Click Element    xpath=//button[contains(text(), 'Allow')]
    Click Element    xpath=//*[@id="mainDiv"]/div[2]/img
    Click Element    xpath=//*[contains(text(),"Bitrix")]
    Input Text    xpath=//*[@id="main-page"]/div[2]/div[2]/div/div/app-bitrix/div/form/div/div/div/input    1895021
    Sleep    3s
    Click Element    xpath=//*[@role="gridcell"][contains(text(), "1895021")]
    @{crm_field}    Create List    Thông tin sự vụ    Chi tiết sự vụ    Kênh tiếp nhận:    Nhóm yêu cầu:    Loại yêu cầu:    Độ ưu tiên:    Mô tả sự vụ:    Kết quả hỗ trợ sơ bộ:    Ảnh sản phẩm:    Lý do quá hạn:    Ghi chú:    Thời gian hoàn thành:    Họ và tên:    Mã KH Core:    ID khách hàng:
    ...    Số điện thoại 1:    Số điện thoại 2:    Số điện thoại 3:    Địa chỉ:    Tên sản phẩm:    Serial:    Hãng:    Ngày sản xuất:    Ngày mua:    Tên KTV:    \    Email:    Địa chỉ:    Hình thức bảo hành:    Tên sản phẩm:    Serial:
    ...    Ngày sản xuất:    Ngày mua:    Nhóm lỗi:    Nguyên nhân lỗi:    Đánh giá lỗi:    Cách xử lý:    Ghi chú:    \    Mã yêu cầu:    Nhân viên CSKH tiếp nhận:    Thời gian hẹn xử lý:    Tiến độ hoàn thành:    Lý do hủy:    Product time:    Checkout location:    Checkin time:
    ...    XLSC Lý do quá hạn:    Ngày mua sản phẩm:    XLSC Doanh thu linh kiện:    XLSC Doanh thu dịch vụ:    Thời gian CSKH tiếp nhận:    Bộ phận xử lý:    KQ CS sơ bộ:    Lưu ý thông tin lỗi linh kiện:    Nội dung xử lý chi tiết:    Checkin location:    Checkout time:    XLSC Cách thức xử lý:    XLSC Km di chuyển:    XLSC Doanh thu sản phẩm:    Trưởng BP bảo trì:
    Sleep    2s
    FOR    ${var_crm_field}    IN    @{crm_field}
        Wait Until Page Contains    ${var_crm_field}
    END
    @{bitrix_field}    Create List    1895021    NTB_KHH - Kho GHLĐ TT ĐMX Khánh Hòa    869471    SNDLKW0ALTZ8    0965264565    Khánh Hòa    Cam Ranh    Cam Linh    Tổ dân phố Đá Bạc    28/02/2024 11:41:00    Mail-ĐMX    Ca báo trùng chỉ sửa chữa BH không thu hồi \ Không tặng lõi lần 2/Lỗi rỉ nước    Đỗ Thị Thu Thủy    CSKH Outbound    XLSC tại kho ĐMX
    ...    Rò nước    Bình thường    KRF    Máy lọc nước nóng lạnh KAROFI KAD-D66    Lỗi kết nối đường nước - 1    JDL015792402010587    Chuyển tiếp BHBT sự cố    Hoàn thành XLSC    28/02/2024 12:54:00    Cốc ABS trắng bị rò nước do cút, dây RO cắm không kịch    15/10/2023    12.2227297_109.084667    28/02/2024 12:54:00    28/02/2024 12:53:00    xử lý cút bình áp    22/02/2024
    ...    Sửa chữa tại nhà    12.222727_109.0846768    Đặng Trường Phú CTV Khánh Hòa
    ...    28/02/2024 11:41:00    Quản lý khu vực MN4    Tổ dân phố Đá Bạc
    FOR    ${var_bitrix_field}    IN    @{bitrix_field}
        Wait Until Page Contains    ${var_bitrix_field}
    END
    Comment    Đặng Trường Phú    Sđt KTV:    Báo cáo KTV:

Open two browser with their window
    [Setup]
    Open Browser    https://robotframework.org    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Execute Javascript    window.open()    \    \    # In BrowserA second window is opened.
    Switch Window    locator=NEW    timeout=None    browser=CURRENT    # Switched to second window in BrowserA
    Go To    https://robocon.io
    Execute Javascript    window.open()    \    \    # In BrowserA third window is opened.
    ${handle}    Switch Window    locator=NEW    browser=CURRENT    # Switched to third window in BrowserA
    Go To    https://github.com/robotframework/
    Open Browser    https://github.com    ${BROWSER}    alias=BrowserB    # BrowserB with first windows is opened.
    ${location}    Get Location
    Switch Window    ${handle}    timeout=None    browser=BrowserA    # BrowserA second windows is selected.
    ${location}    Get Location
    @{locations 1}    Get Locations
    @{locations 2}    Get Locations    browser=ALL

Page Screenshot
    Open Browser    https://robotframework.org    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Set Screenshot Directory    Image
    ${path}=    Capture Page Screenshot    D:\ROBOT\capture{index:03}.png    #Nếu có Arg thì ảnh sẽ lưu ở cùng thư mục với file .robot

Add&Get_cookie
    Open Browser    https://www.google.com.vn/    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Add Cookie    foo    bar
    ${cookie} =    Get Cookies    foo
    Should Be Equal    ${cookie.foo}    bar
    Comment    Should Be Equal    ${cookie.value}    bar

Open two browser with their window_windowTitles
    [Setup]
    Open Browser    https://robotframework.org    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Execute Javascript    window.open()    \    \    # In BrowserA second window is opened.
    Switch Window    locator=NEW    timeout=None    browser=CURRENT    # Switched to second window in BrowserA
    Go To    https://robocon.io
    Execute Javascript    window.open()    \    \    # In BrowserA third window is opened.
    ${handle}    Switch Window    locator=NEW    browser=CURRENT    # Switched to third window in BrowserA
    Go To    https://github.com/robotframework/
    Open Browser    https://github.com    ${BROWSER}    alias=BrowserB    # BrowserB with first windows is opened.
    Switch Window    ${handle}    timeout=None    browser=BrowserA    # BrowserA second windows is selected.
    @{browser_ids}=    Get Browser Ids
    FOR    ${id}    IN    @{browser_ids}
        @{window_titles}=    Get Window Titles    browser=${id}
        Log    Browser ${id} has these windows: @{window_titles}    # sử dụng ${window_titles} và @{window_titles} là như nhau
    END

Textbox
    Open Browser    https://www.tutorialspoint.com    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Input Text    name:key    angular.js
    Click Button    id:btnSearch

RadioButton
    Open Browser    https://vnexpress.net/    ${BROWSER}    alias=BrowserA    # BrowserA with first window is opened.
    Maximize Browser Window
    Execute JavaScript    document.getElementsByClassName('ss-scroll')[0].scrollTop += 36


ThịGiá
    Open Browser    https://finance.tvsi.com.vn/tools/topcompany    ${BROWSER}
    Sleep    1s
    Click Element    ID:btn-show-loc-doanh-nghiep
    Select Checkbox    ID:5
    Click Element    CSS:#quick-link-status > div.on > i
    Scroll Element Into View    XPATH://*[@id="topCompanyPart"]/div[1]/table/tbody/tr[1]/td[2]
    Select From List By Value    id:exchange    HOSTC
    Scroll Element Into View    ID:12
    Unselect Checkbox    ID:12
    Scroll Element Into View    ID:21
    Select Checkbox    ID:21
    Click Element    XPATH://*[@id="collapse-one"]/div/form/div/div[1]/ul/li[2]/a
    Mouse Up    XPATH://*[@id="collapse-one"]/div/form/div/div[2]/div
    Unselect Checkbox    ID:13
    Scroll Element Into View    ID:23
    Unselect Checkbox    ID:23
    Click Element    XPATH://*[@id="collapse-one"]/div/form/div/div[1]/ul/li[6]/a
    Mouse Up    XPATH://*[@id="collapse-one"]/div/form/div/div[2]/div
    Comment    Sleep    5s
    Unselect Checkbox    ID:50
    Scroll Element Into View    ID:53
    Select Checkbox    ID:53
    Scroll Element Into View    ID:54
    Select Checkbox    ID:54
    Click Element    XPATH://*[@id="collapse-one"]/div/form/div/div[1]/ul/li[8]/a
    Mouse Up    XPATH://*[@id="collapse-one"]/div/form/div/div[2]/div
    Scroll Element Into View    ID:70
    Select Checkbox    ID:70
    Click Button    CSS:#collapse-one > div > form > div > div.dtbc.show-details > div.buttons > button
    Sleep    2s
    Scroll Element Into View    XPATH://*[@id="topCompanyPart"]/div[2]/a/img
    Click Element    XPATH://*[@id="topCompanyPart"]/div[2]/a/img
    Sleep    1s
    Mouse Up    XPATH://*[@id="collapse-one"]/div/form/div/div[2]/div
    [Teardown]    abc

*** Keywords ***
abc
    Close All Browsers
