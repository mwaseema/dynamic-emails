import mimetypes
import smtplib
import ssl
from email.message import EmailMessage
from os import path
from typing import List, Union


class Email:
    def __init__(self, smtp_host, smtp_port, from_email, app_key):
        context = ssl.create_default_context()

        self.from_email = from_email

        self.server = smtplib.SMTP_SSL(smtp_host, smtp_port, context=context)
        self.server.login(from_email, app_key)

    def send_email(self, to_email: List[str], subject: str, plain_text_body, html_body: Union[None, str] = None,
                   cc: List[str] = [], bcc: List[str] = [], attachment_paths: List[str] = []):
        msg = EmailMessage()
        msg.set_content(plain_text_body)

        if html_body:
            msg.add_alternative(html_body, subtype='html')

        msg['Subject'] = subject
        msg['From'] = self.from_email
        msg['To'] = ', '.join(to_email)

        if len(cc) > 0:
            msg['Cc'] = ', '.join(cc)

        if len(bcc) > 0:
            msg['Bcc'] = ', '.join(bcc)

        for attachment_path in attachment_paths:
            assert path.isfile(attachment_path), "Attachment should be an existing file"

            attachment_filename = path.basename(attachment_path)
            with open(attachment_path, 'rb') as f:
                attachment = f.read()

            attachment_mimetype = mimetypes.guess_type(attachment_filename)[0]
            assert attachment_mimetype is not None, "Couldn't find mime type of the attachment " + attachment_filename
            attachment_mimetype = attachment_mimetype.split('/')
            msg.add_attachment(attachment, maintype=attachment_mimetype[0], subtype=attachment_mimetype[1],
                               filename=attachment_filename)

        # server.sendmail(from_email, to_email, msg.as_string())
        self.server.send_message(msg)
