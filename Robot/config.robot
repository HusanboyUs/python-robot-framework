*** Settings ***
Library           SeleniumLibrary

*** Variables ***
${BROWSER}        firefox
${TIMEOUT}        5s

*** Test Cases ***
Search and Open Wikipedia Link
    Open Browser    https://www.google.com/    ${BROWSER}
    Handle Pop-up
    Wait Until Page Contains Element    css=[name="q"]    timeout=${TIMEOUT}
    Input Text      css=[name="q"]        nokia wikipedia
    Press Keys      css=[name="q"]        ENTER  
    Wait Until Page Contains Element    css=h3.LC20lb.MBeuO.DKV0Md    timeout=${TIMEOUT}
    Check Wikipedia Link
    Open First Wikipedia Link
    Wait Until Page Loads

*** Keywords ***
Handle Pop-up
    ${popup_visible} =    Run Keyword And Return Status    Wait Until Element Is Visible    css=button#L2AGLb    timeout=${TIMEOUT}
    Run Keyword If    ${popup_visible}    Click Button    css=button#L2AGLb

Check Wikipedia Link
    ${wikipedia_link} =    Run Keyword And Return Status    Element Should Be Visible    css=h3.LC20lb.MBeuO.DKV0Md
    Run Keyword If    ${wikipedia_link}    Log    Wikipedia link found

Open First Wikipedia Link
    Click Element    css=h3.LC20lb.MBeuO.DKV0Md

Wait Until Page Loads
    Wait Until Page Contains Element    css=#firstHeading    timeout=${TIMEOUT}
