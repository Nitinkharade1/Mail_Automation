import time
import schedule
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

sender_email = 'your_mail@gmail.com'     # Replace with your Actual mail
app_specific_password = '#### #### ####' # Replace your app specific password from google
subject = 'About Job Application'
message = """
Hello Good Morning,

"""

pdf_attachment_path = r"C:\\Users\\user\\OneDrive\\Desktop\\python\\Automation\\Resume.pdf"  # Replace with the actual path to your PDF file

def send_email(recipient_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Read the PDF file into a variable
        with open(pdf_attachment_path, 'rb') as pdf_file:
            pdf_attachment_data = pdf_file.read()

        # Attach the PDF file
        pdf_attachment = MIMEApplication(pdf_attachment_data, Name="Resume.pdf")
        pdf_attachment['Content-Disposition'] = f'attachment; filename="Resume.pdf"'
        msg.attach(pdf_attachment)

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_specific_password)
        print("Login Successful...")

        # Send the email to each recipient in the list
        for recipient in recipient_email:
            server.sendmail(sender_email, recipient, msg.as_string())
            print(f"Email sent to {recipient}")

        server.quit()
        print("Emails successfully sent to all recipients")

    except Exception as e:
        print('An error occurred while sending the email:', str(e))

def main():
   

    # Load the recipient email addresses from the CSV file
    try:
        csv_file_path = r"C:\\Users\\user\\OneDrive\\Desktop\\python\\Automation\\Mail.csv"  # Replace with your CSV file path
        df = pd.read_csv(csv_file_path)
        recipient_emails = df['Email'].tolist()
        print(recipient_emails)

        # Schedule the email to be sent every minute
        schedule.every(1).seconds.do(send_email, recipient_emails)

        # Run the scheduler
        while True:
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print(f"An error occurred while reading the CSV file: {str(e)}")

if __name__ == "__main__":
    main()
