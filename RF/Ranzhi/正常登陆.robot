*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot

*** Test Cases ***
Login
    [Setup]    Open the browser to login
    [Template]    common
    admin    admin8888
    [Teardown]    close browser

*** Keywords ***
common
    [Arguments]    ${username}    ${password}
    Input_username&password    ${username}    ${password}
    Submit login
    屏幕截图
