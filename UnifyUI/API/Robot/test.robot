*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com
${browser}  headlesschrome


*** Test Cases ***
TC1
    open browser    ${url}  ${browser}
    set browser implicit wait    10
    input text    //input[@id='phone']      Hello
    sleep    5
#    click button
    maximize browser window



