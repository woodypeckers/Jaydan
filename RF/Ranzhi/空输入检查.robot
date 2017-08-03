*** Settings ***
Library           Selenium2Library
Resource          公共关键字.robot
Resource          业务关键字.robot

*** Test Cases ***
点击_X
    [Setup]    Open the browser to login
    [Template]    common
    ${EMPTY}    ${EMPTY}    xpath=/html/body/div[2]/div/div/div[1]/button
    [Teardown]    close browser

点击_确定
    [Setup]    Open the browser to login
    [Template]    common
    ${EMPTY}    ${EMPTY}    xpath=/html/body/div[2]/div/div/div[2]/button
    [Teardown]    close browser

*** Keywords ***
common
    [Arguments]    ${username}    ${password}    ${button}
    Input_username&password    ${username}    ${password}
    Submit login
    空输入时页面弹窗
    点击按钮    ${button}
    屏幕截图
