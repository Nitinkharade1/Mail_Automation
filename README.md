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


#Information About google app Specific password

A Google App-specific password is a unique password generated by Google that allows you to access your Google account securely when using third-party apps or services that don't support the usual two-step verification process using your regular Google account password. It is designed to enhance the security of your Google account while still allowing you to use various apps and services that require access to your Google account data.

Here's how App-specific passwords work and how to generate them:

1. **Enable Two-Step Verification:** Before you can create an App-specific password, you need to enable two-step verification for your Google account. This adds an extra layer of security to your account by requiring you to provide a second verification method, such as a text message or authentication app, in addition to your regular password when signing in.

2. **Generate an App-Specific Password:**
   - Go to your Google Account settings. You can access this by clicking on your profile picture in the upper-right corner of any Google service (e.g., Gmail).
   - Click on "Security" in the left-hand sidebar.
   - Under the "Signing in to Google" section, find the "App passwords" option. If you don't see it, make sure you've enabled two-step verification.
   - Click on "App passwords," and you may be prompted to sign in again for security purposes.
   - Click on the "Select app" dropdown menu to choose the app or service for which you want to generate an App-specific password. If the app is not listed, you can select "Other (Custom name)" and specify the app's name.
   - Click "Generate" to create the App-specific password.

3. **Use the App-Specific Password:** After generating the App-specific password, you will receive a 16-character code. Use this code as your password when signing in to the specific app or service you selected in step 2. Do not share this password with anyone, and store it securely.

4. **Revoking or Regenerating Passwords:** If you no longer use an app or suspect that your App-specific password has been compromised, you can revoke the password and generate a new one at any time. Simply go back to the "App passwords" section in your Google Account settings and manage your existing app-specific passwords.

Remember that App-specific passwords are designed for third-party apps and services that don't support the usual two-step verification process. For added security, it's essential to regularly review and manage the permissions granted to these apps and revoke access for any you no longer use or trust.
