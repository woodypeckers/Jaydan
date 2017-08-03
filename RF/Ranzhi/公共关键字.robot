*** Settings ***
Library           Selenium2Library
Library           OperatingSystem

*** Variables ***
${base_url}       http://localhost/ranzhi/www/sys/user-login
${Browser}        Chrome
${DELAY}          2
${DIR}            G:\

*** Keywords ***
Open the browser to login
    Open Browser    ${base_url}    ${Browser}
    Maximize Browser Window
    Set Selenium Speed    ${DELAY}
    The page must contain

The page must contain
    Title Should Be    登录 - 然之协同

Input_username&password
    [Arguments]    ${username}    ${password}
    Input Text    xpath=//*[@id="account"]    ${username}
    Input Password    id=password    ${password}

Submit login
    #Click Element    id=submit    #value="登录"
    Click Button    id=submit

点击按钮
    [Arguments]    ${button}
    Click Button    ${button}

屏幕截图
    ${file1} =    Capture Page Screenshot    ${DIR}${/}abc.png
    File Should Exist    ${DIR}${/}abc.png
    #Should Be Equal    ${file1}    ${OUTPUTDIR}${/}selenium-screenshot-1.png
