# **De Te Dicht-O-Meter (De Te DOM)**



# **1.**	**Business Requirements**



## **1.1.**	**Background**



In these strange times where a pandemic runs rampant, hospitals need a way to make sure people follow the rules inside their buildings. This could of course be done by an employee but most of them have a bit more important stuff to do right now and some hospitals just don’t have the manpower. Most people try to follow the rules but sometimes you forget, get distracted, etc.. This is bad because of an increased chance of infection and that is obviously not what we want, especially in a hospital.



## **1.2.**	**Business Opportunity**



In the current times with COVID, many businesses and other places with a lot of people flow, such as hospitals, could use a system that ensures every individual keeps his distance. The fact that a hospital has requested this system, proves that there is in fact a need for something like this. Not only will this system make sure that everyone keeps the appropriate distance at all times, it could also provide the business with useful data, such as the particular areas where the social distance is broken the most, and just how many violations there are each hour etc. This way they might be able to make changes to the layout of the room to try and decrease the number of violations.



## **1.3.**	**Business Improvement Objectives**



BO-1: Automated way to warn people if they are too close to each other.	

BO-2: Not compromising privacy by using the different systems i.e. Google or Amazon. 

BO-3: Simple to use and set up on multiple cameras 

BO-4: Cost effective. 

BO-5: A simple to use UI to see the statistics



## **1.4.**	**Success Metrics**



SM-1: The system marks most cases correctly and shows when social distancing is respected

SM-2: The system causes people to pay more respect to social distancing rules and the spread of covid is thus reduced.

SM-3: The business gets logs and easy to read statistics, to know when the most violations happen.



## **1.5.**	**Vision Statement**



For businesses who want to be able to monitor the people flow and how many of them respect the distance of 1.5 metres. The monitoring is done by an AI, who can recognize people and measure the distance between them. If people get too close, this is logged as a violation.

These logs will be dumped locally on the device, so that only the hospital itself gets access to them. There is also a user interface running on a web server, where employees can edit the configuration files, see the log files plotted in a graph and even see the camera view.



## **1.6.**	**Business Risks**



RI-1: The system will not be used a lot, reducing the accuracy and quantity of the collected data.

RI-2: The Jetson is not powerful enough for prolonged use, this can be solved by using a better edge device.

 

# **2.**	**Scope and Limitations**

## **2.1.**	**Major Features**



FE-1: Generate logs with the amount of violation at what time.

FE-2: A web interface with graphs, generated using the log files made by the device.

FE-3: A config file, editable on the web interface itself for ease of use.

FE-4: After initial configuration, the application can be ran entirely headless, and monitored using the web interface (which runs locally on the edge device)

FE-4: Live counter, updated every second. With the amount of people and the violations on them.

FE-5: Live video feed.




## **2.2.**	**Stakeholders profiles**

 

| **Stakeholder**       | **Major Value**                                              | **Attitudes** | **Major Interests**                                          | **Constraints**                                              |
| --------------------- | ------------------------------------------------------------ | ------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| UZ Leuven Staff       | Reduced workload due to the 		system taking over partly | n/a           | Cost and employee time 		savings must exceed development and usage costs | None identified                                              |
| Product Owner (David) |                                                              | ?             | Job preservation                                             | Training for staff in 		Internet usage needed; delivery staff and vehicles needed |

 



 

##  **3.Software requirements specifications**

**3.1  	Users and Characteristics**

 

**Person**

A person is someone who passes the camera and is detected bij the object detection model


**Violation**

A violation is when the software detects that 2 persons are closer to each other than 1.5 meters.

 

## 3.2 Operating Environment Constraints



OE-1: The te DOM (Dicht-O-Meter) shall operate correctly with the following web browsers: Windows Internet Explorer versions 7, 8, and 9; Firefox versions 12 through 26; Google Chrome (all versions); and Apple Safari versions 4.0 through 8.0.

OE-2: The te DOM shall operate on an NVIDIA Jetson which runs the AI and a local webserver for the interface

OE-3: The te DOM will ony be used locally and no connection is possible outside the local network.



## 3.3 Design and Implementation Constraints



CO-1: The system shall use the current corporate standard Jetson SDK for the Xavier model.

CO-2: All python code shall conform to the python 3.0 standard.

CO-3: Tensorflow 1 will be used alongside keras for the usage of the pre trained AI model

CO-4: Flask is used for the making of the web interface



## **3.4** Assumptions



· 	UZ Leuven has a set of cameras installed ready to be connected to the system 

# **4** 	**External Interface Requirements**



## **4.1 User Interfaces**

A user interface is provided in the form of a webapp. On the dashboard the logged violations will be plotted onto a graph.
There is also a live video feed where you can see the video which the software is processing now. 

There's also a settings page on which you can change the configuration file. So that you can change some configurations without needing direct access to the jetson (the jetson needs to be running for you to change the configurations)

## **4.2** Software Interfaces



SI-1: Web interface

SI-1.2: a settings tab is provided to change multiple configurations such as which camera stream to use.

.

## **4.3 Communications Interfaces**

CI-1: When a violation is detected the live counter will show the detect-o-meter as red 

CI-2: When a violation is detected the live counter will add 1 violation to the total violations

CI-3: When a violation is detected it will be logged and shown in the graph shown on the dashboard

CI-4: When a violation is detected this will be shown in the live video feed

CI-5: When a person is detected a purple box will show what the AI recognizes as a person
