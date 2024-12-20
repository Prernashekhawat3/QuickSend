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
RESUME_PATH = "/mnt/d/prerna_resume/Resume_Prerna_Shekhawat.pdf"  

# Default message and subject
DEFAULT_SUBJECT = "Application for Python Developer - Prerna Shekhawat"
DEFAULT_MESSAGE = """Dear [Recipient's Name],
Hello HR,
I hope this email finds you well.

I am writing to express my keen interest in the Software Developer position. With a solid foundation in Python development and hands-on experience in building and deploying software solutions, I am eager to contribute to your team’s innovative projects.

My recent experience includes working on a timesheet management platform using Flask, Python, and PostgreSQL, which has honed my skills in designing scalable systems and collaborating with cross-functional teams to deliver impactful results. I am confident that my technical expertise and problem-solving mindset align well with the requirements of this role.

I have attached my resume for your review. I would welcome the opportunity to discuss how my skills and experiences can benefit your company goals. Please feel free to reach out to me at 8955495635 or via email at shekhawatprerna3@gmail.com to schedule an interview.

Thank you for considering my application. I am excited about the possibility of joining your esteemed organization and contributing to its success.

Best regards,
Prerna Shekhawat
LinkedIn: https://www.linkedin.com/in/prernashekhawat3/
Phone: 8955495635
"""

@app.route("/send-email", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        hr_emails = request.form.get("hr_email").split(',')
        subject = request.form.get("subject") or DEFAULT_SUBJECT
        message = request.form.get("message") or DEFAULT_MESSAGE

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
            # Handle error by displaying an error message
            return render_template("error.html", error_message=str(e))
    
    return render_template("index.html", default_subject=DEFAULT_SUBJECT, default_message=DEFAULT_MESSAGE)

@app.route("/")
def landing_page():
    return render_template("landing_page.html")

if __name__ == "__main__":
    app.run(debug=True)
