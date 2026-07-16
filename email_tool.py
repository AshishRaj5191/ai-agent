import smtplib
from email.message import EmailMessage

from config import EMAIL_ADDRESS, EMAIL_APP_PASSWORD
from contacts import get_email


def execute(arguments: dict):

    receiver = arguments.get("to")
    subject = arguments.get("subject")
    body = arguments.get("body")

    if not receiver:
        return "Email Error: Recipient is required."

    # Agar user ne direct email diya hai
    if "@" in receiver:
        to_email = receiver

    # Warna contacts.json me search karo
    else:
        to_email = get_email(receiver)

        if to_email is None:
            return f"Contact '{receiver}' not found."

    if not subject:
        return "Email Error: Subject is required."

    if not body:
        return "Email Error: Body is required."

    try:

        msg = EmailMessage()

        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.set_content(body)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

            smtp.login(
                EMAIL_ADDRESS,
                EMAIL_APP_PASSWORD
            )

            smtp.send_message(msg)

        return f"✅ Email sent successfully to {to_email}"

    except Exception as e:
        return f"Email Error: {e}"


if __name__ == "__main__":

    # Contact Name
    print(
        execute(
            {
                "to": "rahul",
                "subject": "Testing",
                "body": "Hello from AI Agent!"
            }
        )
    )

    # Direct Email
    print(
        execute(
            {
                "to": "abc@gmail.com",
                "subject": "Testing",
                "body": "Hello from AI Agent!"
            }
        )
    )