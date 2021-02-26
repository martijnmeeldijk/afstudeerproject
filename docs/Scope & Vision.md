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

 

**Patient**

A patient is someone who stays at the hospital and might be walking around to stretch his/her legs who definitely has to stay away from any possible virus infections.



**Hospital Staff**

The hospital staff will not have to constantly check if people are following the rules because the AI will do that for them

 

## 3.2 Operating Environment Constraints



OE-1: The COS shall operate correctly with the following web browsers: Windows Internet Explorer versions 7, 8, and 9; Firefox versions 12 through 26; Google Chrome (all versions); and Apple Safari versions 4.0 through 8.0.

OE-2: The COS shall operate on a server running the current corporate-approved versions of Red Hat Linux and Apache HTTP Server.

OE-3: The COS shall permit user access from the corporate Intranet, from a VPN Internet connection, and by Android, iOS, and Windows smartphones and tablets.



## 3.3 Design and Implementation Constraints



CO-1: The system shall use the current corporate standard Jetson SDK for the Xavier model.

CO-2: All python code shall conform to the python 3.0 standard.



## **3.4** Assumptions



· 	UZ Leuven has a set of cameras installed ready to be connected to the system 

# **4** 	**External Interface Requirements**



## **4.1 User Interfaces (Tim)**



No interfaces will be displayed because access to the system will be prohibited to unauthorized personnel. There will be documentation given as to how the AI can be used and should be used.

## **4.2** Software Interfaces



SI-1:  Cafeteria Inventory System

SI-1.1: The COS shall transmit the quantities of food items ordered to the Cafeteria Inventory System through a programmatic interface.

SI-1.2: The COS shall poll the Cafeteria Inventory System to determine whether a requested food item is available.

SI-1.3: When the Cafeteria Inventory System notifies the COS that a specific food item is no longer available, the COS shall remove that food item from the menu for the current date.

SI-2:  Payroll System

The COS shall communicate with the Payroll System through a programmatic interface for the following operations:

 

SI-2.1: To allow a Patron to register and unregister for payroll deduction.

SI-2.2: To inquire whether a Patron is registered for payroll deduction.

SI-2.3: To inquire whether a Patron is eligible to register for payroll deduction.

SI-2.4: To submit a payment request for a purchased meal.

SI-2.5: To reverse all or part of a previous charge because a patron rejected a meal or wasn’t satisfied with it, or because the meal was not delivered per the confirmed delivery instructions.

.

## **4.3 Communications Interfaces (Louis)**

CI-1: When the alert is triggered a lamp will be lit up. 