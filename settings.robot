*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Search and Open Wikipedia Link
    Open Browser    https://www.google.com    Chrome
    Input Text    css=input[name="q"]    nokia wikipedia
    Press Keys    css=input[name="q"]    \\13
    Wait Until Element Is Visible    css=#search
    Click Link    xpath=//h3[contains(text(), 'Wikipedia')]
    Wait Until Page Contains    Wikipedia

*** Keywords ***
Wait Until Element Is Visible
    [Arguments]    ${locator}
    Wait Until Element Is Visible    ${locator}    timeout=10s


