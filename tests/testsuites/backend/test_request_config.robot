***Settings***
Resource    ../../env/${env}/config.robot
Resource    ../../resources/resource_requests.robot
Resource    ../../variables/variable_path.robot

***Test Cases***
Test Request API
    Get Config Successfully    ${config_th}    200

***Keywords***
Get Config Successfully
    [Arguments]     ${config_path}    ${expected_response}
    Get Requests    ${config_path}    ${expected_response}

Get Requests
    [Arguments]                   ${request_uri}         ${expected_response}
    ##### HTTP Request ######
    ${alias}                      Set Variable           backend
    ${url}                        Set Variable           ${BACKEND_URL}
    ${uri}                        Set Variable           ${request_uri}
    ${headers}                    Create Dictionary      content-type=application/json
    Create Session                ${alias}               ${url}                           ${headers}    verify=True
    ${resp}                       Get Request            ${alias}                         ${uri}        params=None    headers=${headers}
    ${resp_json}                  Set Variable           ${resp.json()}
    Log                           ${resp_json}
    Should Be Equal As Strings    ${resp.status_code}    ${expected_response}
    Set Test Variable             ${get_resp_json}       ${resp_json}
    [Return]                      ${resp_json}