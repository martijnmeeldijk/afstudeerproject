-**The Social Distance Agent (SDA)**

# **1.** **Business Requirements**

## **1.1.** **Background (Tim)**

In these strange times where a pandemic runs rampant, hospitals need a way to make sure people follow the rules inside their buildings. This could of course be done by an employee but most of them have a bit more important stuff to do right now and some hospitals just don&#39;t have the manpower. Most people try to follow the rules but sometimes you forget, get distracted, etc.. and this is bad because of an increased chance of infection and that is obviously not what we want.

## **1.2.** **Business Opportunity (Robbe)**

In the current times with COVID, many businesses and other places with a lot of people flow, such as hospitals, could use a system that ensures every individual keeps his distance. The fact that a hospital has requested this system, proves that there is in fact a need for something like this. Not only will this system make sure that everyone keeps the appropriate distance at all times, it could also provide the business with useful data, such as the particular areas where the social distance is broken the most, and just how many violations there are each hour etc. This way they might be able to make changes to the layout of the room to try and decrease the number of violations.

## **1.3.** **Business Improvement Objectives (Louis aka lekker ding)**

BO-1: Automated way to warn people if they are too close to each other.

BO-2: Not compromising privacy by using the different systems i.e. Google or Amazon.

BO-3: Simple to use and set up on multiple cameras

BO-4: cost effective.

## **1.4.** **Success Metrics (Martijn)**

SM-1: The system marks most cases correctly and shows when social distancing is respected

SM-2: The system causes people to pay more respect to social distancing rules and the spread of covid is thus reduced.

## **1.5.** **Vision Statement (Tim)**

For hospitals who want to secure their buildings with an application who checks if people are following the rules such as staying 1.5m apart or just simply too many people in a room. This application is an AI who has been trained on recognizing people and recording the distance between them to see if they are following the rules, if not they will be warned with a message on a screen that they need move further apart or any other custom message. Now no employee of the hospital will not need to waste any manpower on such a &#39;trivial&#39; task.

## **1.6.** **Business Risks (Robbe)**

RI-1: The Cafeteria Employees Union might require that their contract be renegotiated to reflect the new employee roles and cafeteria hours of operation. (Probability = 0.6; Impact = 3)

RI-2: Too few employees might use the system, reducing the return on investment from the system development and the changes in cafeteria operating procedures. (Probability = 0.3; Impact = 9)

RI-3: Local restaurants might not agree to offer delivery, which would reduce employee satisfaction with the system and possibly their usage of it. (Probability = 0.3; Impact = 3)

RI-4: Sufficient delivery capacity might not be available, which means that employees would not always receive their meals on time and could not always request delivery for the desired times. (Probability = 0.5; Impact = 6).

# **2.** **Scope and Limitations**

## **2.1.** **Major Features (Louis)**

FE-1: Warn when people are too close.

## **2.2.** **Stakeholders profiles (Martijn)**

| **Stakeholder**       | **Major Value**                                              | **Attitudes**                                                | **Major Interests**                                          | **Constraints**                                              |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| UZ Leuven Staff       | Reduced workload due to the system taking over partly        | n/a                                                          | Cost and employee time savings must exceed development and usage costs | None identified                                              |
| Product Owner (David) |                                                              |                                                              |                                                              |                                                              |
| ?                     | Job preservation                                             | Training for staff in Internet usage needed; delivery staff and vehicles needed |                                                              |                                                              |
| Visitors              | Easier to keep distance, sense of security due to reduced covid risk | Strong enthusiasm, but might not use it as much as expected because of social value of eating lunches in cafeteria and restaurants | Simplicity of use; reliability of delivery; availability of food choices | Corporate intranet access, Internet access, or a mobile device is needed |
| PayrollDepartment     | No benefit; needs to set up payroll deduction registration scheme | Not happy about the software work needed, but recognizes the value to the company and employees | Minimal changes in current payroll applications              | No resources yet committed to make software changes          |
| Restaurant Managers   | Increased sales; marketing exposure to generate new customers | Receptive but cautious                                       | Minimal new technology needed; concern about resources and costs of delivering meals | Might not have staff and capacity to handle order levels; might not have all menus online |

.

# **3.Software requirements specifications**

**3.1 Users and Characteristics (Tim)**

**Patient**

A patient is someone who stays at the hospital and might be walking around to stretch his/her legs who definitely has to stay away from any possible virus infections.

**Hospital Staff**

The hospital staff will not have to constantly check if people are following the rules because the AI will do that for them

## **3.2 Operating Environment Constraints (Robbe)**

OE-1: The COS shall operate correctly with the following web browsers: Windows Internet Explorer versions 7, 8, and 9; Firefox versions 12 through 26; Google Chrome (all versions); and Apple Safari versions 4.0 through 8.0.

OE-2: The COS shall operate on a server running the current corporate-approved versions of Red Hat Linux and Apache HTTP Server.

OE-3: The COS shall permit user access from the corporate Intranet, from a VPN Internet connection, and by Android, iOS, and Windows smartphones and tablets.

## **3.3 Design and Implementation Constraints (Louis)**

CO-1: The system shall use the current corporate standard Jetson SDK for the Xavier model.

CO-2: All python code shall conform to the python 3.0 standard.

## **3.4** **Assumptions (Martijn)**

·UZ Leuven has a set of cameras installed ready to be connected to the system

·

# **4**  **External Interface Requirements**

## **4.1 User Interfaces (Tim)**

No interfaces will be displayed because access to the system will be prohibited to unauthorized personnel. There will be documentation given as to how the AI can be used and should be used.

## **4.2** **Software Interfaces (Robbe)**

SI-1: Cafeteria Inventory System

SI-1.1: The COS shall transmit the quantities of food items ordered to the Cafeteria Inventory System through a programmatic interface.

SI-1.2: The COS shall poll the Cafeteria Inventory System to determine whether a requested food item is available.

SI-1.3: When the Cafeteria Inventory System notifies the COS that a specific food item is no longer available, the COS shall remove that food item from the menu for the current date.

SI-2: Payroll System

The COS shall communicate with the Payroll System through a programmatic interface for the following operations:

SI-2.1: To allow a Patron to register and unregister for payroll deduction.

SI-2.2: To inquire whether a Patron is registered for payroll deduction.

SI-2.3: To inquire whether a Patron is eligible to register for payroll deduction.

SI-2.4: To submit a payment request for a purchased meal.

SI-2.5: To reverse all or part of a previous charge because a patron rejected a meal or wasn&#39;t satisfied with it, or because the meal was not delivered per the confirmed delivery instructions.

.

## **4.3 Communications Interfaces (Louis)**

CI-1: When the alert is triggered a lamp will be lit up.