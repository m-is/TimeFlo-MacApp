# The TimeFlo Project: Project Plan
*Andrew Free 2021*

(*Thanks to Chris Gilmore for part of the document template
for this document.*)

## Resources


1. I will be using python (version 3.6.8). It is not the latest version but is sufficent for this project. Newer versions should also work.
2. VSCode / vim for editing of code and documentation files
3. Qt library files and documentation
4. For development, a computer running OSX version 10.15.7 as the latest apple operating systems are inherently unstable from my experience. 
5. pip, a python package manager (version 18.1)
6. Flake8, a linter for python code to help improve code quality and catch errors
7. An alarm sound from https://freesound.org/. A fog horn specifically


## Work Breakdown

1. Finish the requirements.
2. Finish the design.
3. Finish the plan.
4. Figure out how to develop a basic interface with buttons and a numeric disiplay.
5. Figure out how to tie events to the buttons and numeric display.
6. Work out the logic side of things for managing the state based on events and the current state.
7. Test and work on the vnv document.
8. Update the README and license files.

## Schedule

| Task | Time to completion |
| --- | ----------- |
| Requirements | 10-20-2021 |
| Design | 10-25-2021 |
| Plan | 10-27-2021 |
| Basic Interface | 10-30-2021 |
| Events | 11-2-2021 |
| State Logic | 11-5-2021 |
| Testing / vnv | 11-8-2021 |
## Milestones and Deliverables

I will describe the milestones for the programming aspects of this project. The requirements, design, and plan are farily self explanatory in what the deliverable is and I dont feel they need to be described further as the provided templates already outline what is expected. 

### *Basic Interface Deliverable*

A basic interface that includes a window with a numeric display and buttons to start/stop the timer along with a button to click. This deliverable does not include interaction between the components or any explicit events to manage the state. 

### *Events Deliverable*

This includes the ability for the interface elements above to interact with each other based off of events and an internal timer. From my precursory research Qt provides a timer class which I can utilize for this. This deliverable includes the ability to tie events to interface elements that interact with a timer. It will also include some basic internal state variables like how long breaks will be and how many work + break cycles have been completed before a long break is due. 
### *State Logic Deliverable*

This deliverable is polishing up of the previous step and tweaking the state logic and event interactions to meet the requirements. By the end of this deliverable the app should be working and useable for the intended purpose. 

### *Testing Deliverable*

Testing for this will mostly be done by hand. I choose to use Qt which I am unfarmilar with so I'm unsure if I will be able to include unit tests. This deliverable may include unit tests but will primarly be testing the app in a QA fashion where I try to break the app by clicking around in ways that the app that could be considered unexpected. I will also attempt to build the app from scratch once development is done to ensure the README steps are accurate. I will be using flak8 as a linter to help ensure the code has no explicit problems.  

### *Readme + License Deliverable*

Once the app is complete and tested I will need to update the readme to reflect the steps to build the project. A license file for Qt also needs to be included to the root of the repo. 