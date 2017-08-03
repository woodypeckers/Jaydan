*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot

*** Keywords ***
空输入时页面弹窗
    Page Should Contain    登录失败，请检查您的成员名或密码是否填写正确。
