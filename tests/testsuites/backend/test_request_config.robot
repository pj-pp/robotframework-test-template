***Settings***
Resource    ../../env/${env}/config.robot
Resource    ../../resources/resource_requests.robot

***Test Cases***
Test Request API for TH
    Get Config Successfully    ${config_th}    ${status_200}

Test Request API for ID
    Get Config Successfully    ${config_id}    ${status_200}

