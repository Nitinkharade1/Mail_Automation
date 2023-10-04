#Email Automation with PDF Attachment

This Python script automates the process of sending emails to a list of recipients with a PDF attachment. It uses the smtplib library to send emails via Gmail's SMTP server and the schedule library to schedule the emails to be sent at regular intervals.

#Features
* Sends personalized emails with a common message and a PDF attachment to multiple recipients.
* Loads recipient email addresses from a CSV file.
* Handles Gmail SMTP server authentication using an application-specific password.

#Prerequisites

Before using this script, make sure you have the following:

* Python 3.x installed on your system.
* A Gmail account with an application-specific password generated for SMTP authentication.
* A CSV file ('Mail.csv') containing a list of recipient email addresses under the 'Email' column.
* A PDF file ('Resume.pdf') that you want to attach to the emails.
#Usage
1)Clone this Git repository to your local machine:
git clone <repository-url>

2)Install the required Python libraries if you haven't already:
pip install schedule pandas

3)Update the following variables in the script with your Gmail credentials and file paths:

'sender_email': Your Gmail email address.
'app_specific_password': Your Gmail application-specific password.
'pdf_attachment_path': The path to the PDF file you want to attach to the email.
'csv_file_path': The path to the CSV file containing recipient email addresses.

4)Run the script:
python email_automation.py

The script will commence sending emails to the recipients listed in the CSV file at regular intervals (default is every minute).

Customization
You can personalize the email message by modifying the 'message' variable in the script to suit your needs. Additionally, you can adjust the scheduling frequency by modifying the 'schedule.every()' line.



