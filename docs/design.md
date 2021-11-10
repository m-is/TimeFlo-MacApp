# The TimeFlo Project: Design
*Andrew Free 2021*

## Introduction

This document describes the architecture design decisions and goes over some high level components of the program and how they will manage the state. It also goes over some of the risks in these decisions. 

## Architecture

The architecture design for this program is an event driven interface powered by Qt written in Python. Qt is an open source toolkit for GUIs that works cross platform and runs natively. The Qt package provides python bindings to create GUI elements. An advantage of using Qt/Python is that it should work cross-platform fairly eaisly. Testing other platforms outside of my own is outside the scope. This choice should also make development pretty straightforward and Qt is well developed with lots of documentation. 
I am able to use Qt for this use case without needing a commerical license under the LGPL 3.0 license. 

The app will have a single primary window with two buttons. One button to start a work or break period (labeled differently for both cases) and a button to end the timer (quit the app). Events will be tied to both buttons. For the start button it will start an event where a counter is decremented (and displayed) until the end of the work unit. When it is time for a break the same button and numeric display will be used but with an updated label.

The numeric display element will be used for both breaks and work periods. I will display different colored text for each. For work units, black numbers will be used and for breaks red numbers. When the timer reaches 0 the event will update the programs internal state depending so that it knows what the next state change is.

The risks with this architecture is low due to the simplicity. The app will be user tested rigorously to ensure that the user is unable to put the app into a invalid state or state that doesn't match with the requirements. Given that this is just a timer for work management, the risk from possible failure is very low. Worst case you take too long of a break or work longer than expected. There is no risk that failure of this program will cause physical harm to people or property as it is intended to run on personal computers, mine specifically. It is not recomended that this program is run on any computers that control industrial or medical equipment. 

The only other risks I can see is the fact that I have not worked with Qt before so I dont have an exact idea in my head of how things will be implemented outside of a high level view.