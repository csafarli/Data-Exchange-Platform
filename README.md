# Data-Exchange-Platform
Data Exchange Through Supply Chain 

The application developed based on the proposed model (see Fig.1).

![Centralized Circularity Data Exchange](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%201.png)

Figure 1 – Centralized Circularity Data Exchange
 
To build the desktop application, the Python programming language, MYSQL database management, Tkinter toolkit, Pandas, NumPy, Seaborn, and Matplot libraries have been used. The project is consisting of 6 different modules, which are, a user log in and registration interfaces, supplier, customer and designer dashboards, database connectivity, and design dashboard.

## 1.1.1 User Registration and Login
The module provides the functionality of registration of the new user and sign-in process for the registered user. The main screen has two buttons, which give register and login options.

![Register and Login screens](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/login%20register.png)
Figure 2 – Registration and login screens
   
The registration has the functionality of checking the uniqueness of username, selecting different sessions where only one designer is allowed to register in the system, saving registration information to the system for the login processes.
The register user function verifies user name and redirects to the session verify function.
In the session – verify function codes checks the session info and directs to the save function
to store the data.

The registered user can sign in to the system from the login screen. The main functionality of the screen is to check username and password and directs the user to the relevant dashboard based on registry data.
To understand which user is in the system every user who logged in to the system, their username is saved to the system as their user key, which then is used to identify data entries.
The logged-in user will be directed to the session based on their registration data, and import lines provide connectivity to the other modules.
Every wrong user name and password will direct the user to the error screen. In the registration form, if the user enters existent user name or there is a designer in the system, and the new user wants to register as a designer who will also direct to the warning screen (see Fig.3)

![Warning windows](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/warnings.png)
  
Figure 3 – Warnings

## 1.1.2 Dashboards
The user that is registered as the supplier will be directed to the relevant dashboard from the
login page. The dashboard has the functionality of inserting data into the database, visualizing the stored data rows and charts as a graphical representation. From the panel, the user can also delete inserted data and update the charts to see changes in graphs.
The mainboard is consisting of two main, data entry and data visualization frames (see Fig.4).

![Supplier dashboard main frames](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%209.png)
 
 Figure 4 – Supplier dashboard main frames

The entry frame is designed with widgets like text or combo box entry. At the same time, the visualization frame has two primary parts, first, on the top graphical tools like trend lines or pie chart, second on the bottom, list box.
The entries inserted by the user will be illustrated on the list box where it can be selected the specific data row to delete it after the delete operation list box will present a new table.

The board has Add, Clear, View, Delete, Exit buttons that process functions as follows.
The first button is taking user inputs from entry boxes, building a connection to the database, and writing the information to the table. The CO2 value is calculated automatically based on the given formula, taking fuel consumption, electricity, and transportation as an input. (EPA 2018).
For the deletion process, the main challenge is to link the selected data to the related row in the database table.
The show data function takes the values to form the data table with the help of view data function in the database module and visualize it in the list box
The view data filters out the table rows based on the user key and gives the only rows that belong to the recent user.
  
All the basic functions work with the database connectivity, which means every process done by the user affects the data set in the MYSQL database server. The database and the table were developed by the two main functions in the database module. Two secondary functions have been explained in the delete and view processes.

As aforementioned above, for the visualization of the plots, the matplotlib, and seaborn libraries have been imported, and CSV (comma-separated values) library helps to export data from MYSQL database and save it as CSV file for the further analysis.
Now the application can import data as a data frame and study it for the statistical visualization.
The application has a functionality to examine data and built correlation matric as well as to represent the percentage proportion of the CO2 emission to process steps (see Fig 5).

![Statistical Graphics](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%2010.png)

 Figure 5 – Statistical Graphics

There are two different main sessions, supplier and designer. The suppliers’ primary functions are to add delete and visualize analyzed data (see Fig 6).

![Supplier Dashboard GUI](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%2011.png)

 Figure 6 – Supplier Dashboard Graphical Representation

## 1.1.3 Design simulation board
The designer has about the same functionality as the supplier. From the platform, it is possible to add data to the database, analyze and visualize it, and delete unwanted information. Moreover, the designer session gives the possibility to simulate design parameters and see the effects of the sustainability side.
One of the main features is the checking design inputs’ (Dvorak and Kosior 2012) like closure material and bottle colour, effects on the environment.

![Design Warnings](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%2011.png)

 Figure 7 – Design Warnings

In the design board, the application reads all the data from the database and not filtering out by the user. However, in terms of confidentiality, the designer does not have direct access to specific data. Exported data is used to analyze and present statistical graphics which does not share specific data but only percentage proportion and correlation.

Therefore, the presented graphics are based on the total data and illustrates the sustainability performance of the overall system.
The design board gives the possibility to examine the overall system with graphical statistical tools. From the simulation, the designer side can identify problematic areas and see overall sustainability performance.

![Design Simulation Board](https://github.com/csafarli/Data-Exchange-Platform/blob/master/.idea/Picture%2013.png)

 Figure 8 – Design Simulation Board
 
For the proposed model, no economically sensitive data will be shared. The organization can only have access to its own data from the database. The overall sustainability performance data is accessible from OEM; however, to get a right to see and evaluate the specific metrics, they must have authorization from the data owner company.
 
