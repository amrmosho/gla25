
from ins_kit._connect._email import Email

recipient_email = "heshamehab47@gmail.com"

email_sender = Email()
lang = {
    "body":"Hello",
    "subject":"Yes"
}
response = email_sender.send_email(recipient_email,"This is body @(body)","This is subject @(subject)",lang)

