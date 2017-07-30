*** Settings ***
Library           Selenium2Library
Resource          Rescourse.robot

*** Test Cases ***
Login_success
    [Template]    common
    admin    123456    退出

Login_fail_username
    [Template]    common
    invalid    123456    用户名不存在

Login_fail_password
    [Template]    common
    admin    invalid    用户名和密码不匹配

*** Keywords ***
common
    [Arguments]    ${username}    ${password}    ${value_flag}
    log many    ${username}    ${password}    ${value_flag}
    Open_Login_page
    Input_Username    ${username}
    Input_Password    ${password}
    Click_Login_button
    Contain_page    ${value_flag}
