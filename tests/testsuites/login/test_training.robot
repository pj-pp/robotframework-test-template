***Settings***
Resource    ../../env/${env}/config.robot
Resource    ../../resources/resource_selenium.robot

Test Teardown    Close all Browsers

***Test Cases***
TEST1
    Login Exchange successfully    ${username_1}    ${password_1}

TEST2
    Login Exchange successfully    ${username_2}    ${password_2}
