***Settings***
Resource    ../../env/${env}/config.robot
Resource    ../../resources/resource_selenium.robot
Resource    ../../variables/variable_web_locator.robot

Suite Setup       Open Exchange on browser
Suite Teardown    Close Exchange

***Test Cases***
Test UI
    Login Exchange successfully    ${username_1}    ${password_1}

***Keywords***
Login Exchange successfully
    [Arguments]      ${username}             ${password}
    Input Text       ${signin_email}         ${username}
    Input Text       ${signin_password}      ${password}
    Click Element    ${signin_submit_btn}

Open Exchange on browser
    Open Browser                ${EXCHANGE_URL}    Chrome
    Set Window Size             1440               900
    Wait Until Page Contains    เข้าสู่ระบบ        timeout=120s    error=No Sign in page open

Close Exchange
    Close All Browsers