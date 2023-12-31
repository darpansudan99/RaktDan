﻿# RaktDan
# Blood Donation System Django

Most operations, surgeries and treatments to accidents require blood units to be used due to blood 
loss from the body. These blood units are donated by normal people like us, and stored in blood 
banks. The term “blood bank” refers to a division of a hospital laboratory or an independent 
entity where the storage of blood products occurs and where proper testing is performed to 
reduce the risk of transfusion related events. It processes blood that will be supplied to the 
patients according to their needs and connects requests to donations

The Project’s Aim is to make the process of blood donation and tranfusion effective by connecting hospitals with local donors and blood banks. Blood Donation Management System can help the entire procedure be automated, which saves manpower, allows for a systematic approach and increases efficiency. It shows the details like name, address, contact info stored in the system about various blood banks, hospitals and donation camps, filterable by the area. 

### Potential users

Hospitals: Hospitals can use this system to access data about various blood banks and their inventories easily to quickly contact a particular bank. They can also make a request to all the registered donors of a particular Blood Type living nearby. The system will automatically send an email to all these donors to notify them.  

Donors: Any person who wishes to donate blood can easily do so with the help of this system. They can see data like address and contact info about various blood banks, hospitals and donation camps like those organised by Social Welfare Clubs with their dates so that donors can regularly go to a donation place.

Hence, the Blood Bank Management System makes the blood bank stock more systematic and manageable.

### About project

This Web Application includes 6 Django models and uses JavaScript for munipulating the Front-End. This application is also Mobile Responsive achieved by using Media Queires in CSS and Bootstrap. It is fairly dictinct from any other Project in this course and fairly more Complex as it has features like multiple types of Registeration Options(Donors and Hospitals) and automated emails for blood donation requests.

**Special Features: **
1. Users can register as Donors or Hospitals.
2. Users can Filter Donation Places and Hospitals according to Area.
3. Hospitals can check for Blood Units Available for any Blood Type in Blood Banks.
4. Hospitals can make Blood Requests to registered Donors.
5. Automated Emails for Blood Requests.
6. Users can Respond to Donation Requests so that Hospitals know what to expect.

### Project structure
- Djangon Project named 'BloodDonation' has been created.
- 'donate' is an app inside this django project.

In the donate folder,
- A folder named 'templates' is created which contains all the html files of the project and the CSS and JavaScript files are inside the 'static' folder.
- In the models.py file, django models are created as python classes and their __str__ and serialize fucntions are defined.
- In the urls.py file, all the app urls and 2 api urls are defined.
- In the views.py file, functions are defined for each url.
- In the donate/index.js file inside static folder, JavaScript code is written. It helps us Filter Donation Places and show Blood Units search without reloading an entire page enhancing user experience.


### How to run this application
1. Clone or download this repository

2. In terminal run the following commands to download the required files
    - pip install django
    - pip install django-phonenumber-field
    - pip install django-phonenumber-field[phonenumbers]

3. Go inside the directory of the project and run in terminal from there - python manage.py runserver

### FUTURE SCOPE: 
In order to extend the applications of this system, blood banks and clubs can be given user access so that they can update details about their inventory and camps information respectively. Furthermore, users may be allowed to edit their profile details like address, and also upload their profile images. Currently all these functions are managed by the admin or superuser. Moreover, E-mail or phone messages can be used to notify about the authorization.

### Project Demo
<p align="center" >
<img  src="Images/ERD.png">  
 ER diagram 
 <hr>
 
<img  src="Images/schema diagram.png">
Schema diagram
  <hr>
  
<img  src="Images/home1.png">
Landing home page 
 <hr>

<img  src="Images/home2.png"> 
Home page
<hr>

<img  src="Images/login.png"> 
Login page
<hr>

<img  src="Images/register.png">
Register options
<hr>
 
<img  src="Images/reg2.png">
Register Page 
 <hr>

<img  src="Images/profile.png">
Profile Page
 <hr>

<img  src="Images/profile3.png"> 
Profile Page
 <hr>

<img  src="Images/requests.png">
Requests Page
<hr>
</p>
