# -- Needed info from user to send the email to many emails at same time -- #

# Title of the sent email
email_subject = "Example subject"

# Contents of the sent email
email_message = (
"Write email here!"
)

# Sender's email and password -- password from google settings or settings alike
sender_mail = "example.adress@gmail.com"
sender_mail_pass = "examplepassword1"  

# Path to csv.file
emails_csv = "example/emails.csv"




                                                                                
# -- Imports -- #
import smtplib
import csv





# -- the program / script -- #
def send_mails():
    # Cheking that user has inputted own mail and app password
    if not sender_mail or not sender_mail_pass:
        print("Email or password environment variables are not set.")
        return


    #sending the gmail
    try:
        with open(emails_csv, newline='') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                to_email = row[0].strip()
                try:
                    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                            connection.starttls()
                            connection.login(user=sender_mail, password=sender_mail_pass)
                            connection.sendmail(
                                from_addr=sender_mail,
                                to_addrs=to_email,
                                msg=f"Subject:{email_subject}\n\n{email_message}"
                            )
                    print(f"Email sent to {to_email}")
                
                except smtplib.SMTPException as e:
                    print(f"Failed to send email to {to_email}: {e}")
                except Exception as e:
                    print(f"An error occurred while sending email to {to_email}: {e}")

    except FileNotFoundError:
        print(f"The file {emails_csv} was not found.")
    except smtplib.SMTPAuthenticationError:
        print("Failed to login to the SMTP server. Check your email or password.")
    except Exception as e:
        print(f"An error occurred: {e}")




if __name__ == "__main__":
    send_mails()
