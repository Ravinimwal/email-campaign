# Email-Campaign-Manager

## Table of Contents
1. [Configuration Setup](#configuration-setup)
2. [Testing Add Subscriber API](#testing-add-subscriber-api)
3. [Testing Remove Subscriber API](#testing-remove-subscriber-api)
4. [Testing Send Campaign Mails API](#testing-send-campaign-mails-api)


### Configuration Setup
1) Open Command Prompt and  enter the following command - git clone https://github.com/Mayankrai01/Email-Campaign-Manager.git
2) Open the emaildb2.sql in workbench and execute all the commands to create tables
3) Now open the code editor and browse to the newly created folder using the command - cd Email-Campaign-Manager
4) Run the following command to create a new conda virtual environment in current folder- conda create -p ./venv python=3.8 -y
5) Enter Command to activate the environment - conda activate venv/  ---(note this will work only in command prompt, not in powershell make sure you are using that)
6) Run the following command to install the required libraries- {pip install -r requirements.txt} 
7) In the config.py file, set up your MySQL database configuration:
8) Enter Command -> python campaignFunctions.py
9) Note Down the server and port and open brower and paste it in url box for testing purpose (below image is for reference)
![image](https://github.com/Mayankrai01/Email-Campaign-Manager/assets/103130321/bb456abf-23b6-4885-8f47-17e8278f3995)



### Testing Add Subscriber API
1) Edit the URL to - http://127.0.0.1:5000/subscribe
2) Note-Either User Email is an admin or they are the same user as Customer Email, since either the admin or the user itself can add customer in database
3) {
    User Email:m@g.com
    Password: 1234
    Customer Email:mayank.101120@gmail.com
    First Name: mayank
  }
4) Run the following command in your MYSQL workbench to check if the users are added- {select * from Subscribers;}
5) It would reflect the changes along with their details

### Testing Remove Subscriber API
1) Edit the URL to - http://127.0.0.1:5000/unsubscribe
2) Note-Either User Email is an admin or they are the same user as Customer Email, since either the admin or the user itself can remove customer from database
3) {
    User Email:m@g.com
    Password: 1234
    Customer Email:mayank.101120@gmail.com
    Reason: Provide any reason
  }
4) Run the following command in your MYSQL workbench to check if the users are added- {select * from Subscribers;}
5) It would reflect the changes along with their details

### Testing Send Campaign Mails API
1) Turn on the server if you haven't already done that (this is done so that if a user wants to unsubscribe we can do that, if the application is not running mail will be delivered but user can't unsubscribe)
2) Update the FROM_EMAIL variable in line 25 of html-mail.py file with your email and enter your corresponding password.
3) Run the command {python html-mail.py} to send mails to all active users
4) In inbox you can click on Unsubscribe link to unsubscribe from campaign
5) You can add your email in the Subscribers list and verify the same.


