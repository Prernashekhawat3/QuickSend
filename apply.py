from flask import Flask, render_template, request, redirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Email Configuration
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Email address from .env
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RESUME_PATH = "/mnt/d/prerna_resume/CV_Prerna_Shekhawat.pdf"  


@app.route("/send-email", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        hr_emails = request.form.get("hr_email").split(',')
        subject = request.form.get("subject")
        message = request.form.get("message")

        # Send email logic
        try:
            for hr_email in hr_emails:
                hr_email = hr_email.strip()

                # Create the email message
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = hr_email
                msg['Subject'] = subject
                msg.attach(MIMEText(message, 'plain'))

                # Send email using SMTP
                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    server.sendmail(EMAIL_ADDRESS, hr_email, msg.as_string())

            return redirect("/send-email")  # Redirect to the home page after sending emails
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
