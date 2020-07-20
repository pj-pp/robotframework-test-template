***Settings***
Library     SeleniumLibrary
Library     String
Resource    ../variables/variable_web_locator.robot

***Keywords***
Login Exchange successfully
    [Arguments]                 ${username}             ${password}
    Open Exchange on browser
    Input Text                  ${signin_email}         ${username}    
    Input Text                  ${signin_password}      ${password}    
    Click Element               ${signin_submit_btn}

Open Exchange on browser
    Open Browser                ${EXCHANGE_URL}    chrome
    Set Window Size             1440               900
    Wait until Page contains    เข้าสู่ระบบ        timeout=10s    error=title not found