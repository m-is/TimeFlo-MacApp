# The TimeFlo Project: Requirements Document
*Andrew Free 2021*

(*Thanks to Chris Gilmore for the document template for this
document.*)

## Introduction

The goal of this project is to create software to help a user manage time by implmenting a technique developed by Francesco Cirilo.
This technique dictates that a user work in intervels of time followed by small breaks, repeating work & small breaks a few times until taking a longer break. 
This is a general time managment technique to help people better utilize their time and stay focused.
### Purpose and Scope

Implmentation of the technique is flexible in work units and breaks regarding time. I have chosen to break down work intervals into 25 min segments followed by 5-10 min breaks. After completing at least 3 of these work/break intervals a 25 min break should be taken. This 25 min long break will be configurable by a constant defined in the program. The goal of this software is to help force the user to take breaks and break out of their flow state (also to get into the flow state). This is useful in development as it can be easy to get stuck in a flow state while working leading you to dig into the weeds and loose the bigger picture.

This projects only technical aim is to to be a timer that alerts the user audibly with a fog horn when a work unit or break has ended. I am the only user of this code so the scope of testing and installation will only include OSX as the target OS. Python and Qt are cross platform so it should be possible to run this on a flavor of Linux or on Windows but I can't guarantee those results. 

I haven't used Qt before so I also took this project as a chance to play around with Qt and learn something about basic GUI development as part of the project purpose. 

I am farmiliar with git and use it daily so I wont be using this project to learn that explicitlly. I plan to commit most all my work at once or in fairly large chunks as there is no one upstream depending on my changes for this project.  
### Target Audience

The target audience is myself as a user and instructor (Bart Massey) as a reader and reviewer. The software should be useable and easy to setup and run for anyone else who whishes to use it as the libraries and languages work cross platform. OS's other than my own (OSX) are outside the intended scope of the project and have not been explicitly tested. This software is designed for personal machines and should not be run on any computers that control systems that could caues harm to people or property if they were to fail. 

### Terms and Definitions

1. Target OS - This is the operating system the program is intended to run on.
2. pip - Package managment software for Python programs
3. Qt - Cross platform GUI library with python bindings
4. Flow state - "In positive psychology, a flow state, also known colloquially as being in the zone, is the mental state in which a person performing some activity is fully immersed in a feeling of energized focus, full involvement, and enjoyment in the process of the activity. In essence, flow is characterized by the complete absorption in what one does, and a resulting transformation in one's sense of time." - (https://en.wikipedia.org/wiki/Flow_(psychology)) 

## Product Overview

The project will be written in Python. It will use Qt for the timer interface. The software should be easy to set up and use for anyone wishing to utilize it. The user in the context of this program is me. I am also the only stake holder as no one else will be relying on this project. This project aims to be as simple as possible which hopefully will encourage my usage of it and make it easy to maintain or use on other OS's in the future. As stated above, the scope of the project in regards to the target OS is just my own laptop running OSX. There are no real hard limitations on what can be done so long as the technique is implemented but I intended to keep things simple. As I am working with Qt for the first time I don't plan on writing explicit unit tests but will unideally test my code by hand.

### Use cases

1. This software can be used anytime you are working on a bigger project and need something to help you both get into and out of the flow state. In development you want to be able to get into a flow state while working but also have time set to break out and allow yourself to see the bigger picture / give yourself a chance to take a break.
2. Anytime you are working through tasks in general that aren't software related but where you need to focus for a bit this software could be used. The breaks are good to encourage you to move your body and legs for health reasons.
## Functional Requirements

This section will describe the functional behavior of the program and what the state is expected to be at any point.

### *Functional Requirements 1*

The program should launch a program with 4 interface elements when run.
1. A window
2. A numeric counter of time in minutes
3. A button to quit the app
4. A button that will start any work units or breaks.

### *Functional Requirement 2*

The program will have two constants at the top of the timer.py file to control behavior
1. A constant that defines how long a long break is (default 25).
2. A constant that defines how many work/short break cycles are completed until a long break starts. (default 3).

## Extra-functional Requirements

1. Each time the timer ends, the user will be required to start the next timer, for work, short breaks, or long breaks. 
2. The same fog horn sound will play at the end of any of these. 
3. The time for a short break will be random between 5-10 min. 
4. The quit button must work at any time, even if in the middle of a countdown.
### *Extra-functional Requirement 1*

1. The button label should tell you if you are starting a unit of work, a short break, or a long break.
2. The color of the numbers will be red for any break type and black for work.
### *Extra-functional Requirement 2*

1. The program must run on the target OS (OSX version 10.15.7).
2. The program must work with python 3.6.8.
3. The dependencies should be pinned to specific versions to avoid install issues. 