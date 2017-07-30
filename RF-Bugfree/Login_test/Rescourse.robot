*** Settings ***
Library           Selenium2Library

*** Variables ***
${base_url}       http://localhost/bugfree/index.php/site/login

*** Keywords ***
Open_Login_page
     open browser    ${base_url}
    Title Should Be    登录 - BugFree

Input_Username
    [Arguments]    ${username}
    input text     id=LoginForm_username    ${username}

Input_Password
    [Arguments]    ${password}
    input text    id=LoginForm_password    ${password}

Click_Login_button
    Click Button    id=SubmitLoginBTN

Contain_page
    [Arguments]    ${arg}
    Page Should Contain    ${arg}
