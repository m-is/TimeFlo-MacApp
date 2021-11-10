# The TimeFlo Project: Validation and Verification
*Andrew Free 2021*

(*Thanks to Chris Gilmore for the document template for this
document.*)

## Introduction

This document will describe the steps used to test the timer application.

### Target Audience

The target audience for this document is Bart Massey as a reviewer and myself as a record of verification

### Terms and Definitions

1. Flake8 - Python linter for code quality
2. pytest-qt - Test framework for Qt applications


## V&amp;V Plan Description

Below will explain the plan for testing and verification that the app meets the requirements defined. 

### Scope Of Testing

The scope of testing will include unit tests that cycle through the different states and encompass the fact that a user can change the constants regarding length of long breaks and work time. There are no integration or system test files. 

I also did some user QA testing where I used the app and verified that it acted in a way in line with the requirements. I used flake8 on my code to help with quality but that isn't testing in itself. 

In my unit test I was not able to test the button that quits the app because in doing so the tests would exit before completing. I did however test that functionality in user QA testing. I also had to increase the timeout in the tests to slightly longer than the exact time, This was required to encompass the time it takes for the alert sound to play before transitioning to the next state.  

### Testing Schedule

My testing schedule was the day it was due. I had been testing the app by hand during development and was not originally going to write unit tests but it felt wrong to leave them out and I figured out a way to make them work last minute.

### Release Criteria

1. The system must be a system running python 3.6 or newer. 
2. The system can technically be linux, windows, or OSX but it was only tested for OSX explicitly. 
3. Must be an x86 system.
4. The operating system must be able to withstand a crash of the Qt framework, although this has not been observed in the final version of the app. 

## Unit Testing

My unit test encompasses rotating through all the possible stage changes. I used pytest-qt to run the unit tests on the GUI. 
### Strategy

I only have unit tests, there are no real integration tests I could write for this. The strategy is to test all the possible states the app could be in. I was unable to test that a sound is playing but I accounted for the time it takes to play in the timeout of the unit tests. 

## System Testing

I only tested this on OSX 10.15.7 and on python 3.6.8 myself but the cross platform nature of python and Qt should allow this to run on other x86 systems in linux or windows. 

### Test Cases

My system testing was encompassed in my QA testing and unit tests. I have no additional tests that test for system compatibility explicitly.
