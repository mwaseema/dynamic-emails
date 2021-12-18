import argparse
import time
from glob import glob
from os import path

from tqdm import tqdm

from dynamic_emails.libs.csv_parser import get_csv_data
from dynamic_emails.libs.email import Email

parser = argparse.ArgumentParser(description='Send dynamic emails')
parser.add_argument('--smtp-host', type=str, required=True, help='SMTP server address for sending email')
parser.add_argument('--smtp-port', type=int, required=True, help='SMTP server port')
parser.add_argument('--from-email', type=str, required=True, help='Your email')
parser.add_argument('--app-key', type=str, required=True, help='App key for connecting with your account')
parser.add_argument('--cc-emails', type=str, required=False, help='CC Email or comma separated emails')
parser.add_argument('--bcc-emails', type=str, required=False, help='BCC Email or comma separated emails')
parser.add_argument('--subject', type=str, required=True, help='Subject for the email')
parser.add_argument('--data-csv-file', type=str, required=True, help='Path to the .csv file containing data')
parser.add_argument('--plain-email-body-file', type=str, required=True,
                    help='Path to .txt file containing your email body')
parser.add_argument('--html-email-body-file', type=str, required=False,
                    help='Path to .html file containing HTML formatted email body')
parser.add_argument('--attachment', type=str, required=False, help='Path to file or folder containing files')
args = parser.parse_args()


def load_file_content(file_path):
    assert path.isfile(file_path), f"Following file doesn't exist:\n{file_path}"

    with open(file_path, 'r') as f:
        data = f.read()
    return data


def replace_placeholders(csv_row_dict: dict, text: str):
    for k in csv_row_dict.keys():
        text = text.replace('{{' + k + '}}', csv_row_dict[k])
    return text


def get_attachment_list(attachment_path):
    if path.isdir(attachment_path):
        return glob(path.join(attachment_path, '*'))
    else:
        return [attachment_path]


def main():
    smtp_host = args.smtp_host
    smtp_port = args.smtp_port
    from_email = args.from_email
    app_key = args.app_key
    cc_emails = args.cc_emails
    bcc_emails = args.bcc_emails
    subject = args.subject
    data_csv_file = args.data_csv_file
    plain_email_body_file = args.plain_email_body_file
    html_email_body_file = args.html_email_body_file
    attachment = args.attachment

    plain_email_body = load_file_content(plain_email_body_file)

    html_email_body = None
    if html_email_body_file:
        html_email_body = load_file_content(html_email_body_file)

    email_obj = Email(smtp_host, smtp_port, from_email, app_key)
    csv_data = get_csv_data(data_csv_file)
    attachment_list = get_attachment_list(attachment) if attachment else []

    cc_emails = [cce.strip() for cce in cc_emails.split(',')] if cc_emails else []
    bcc_emails = [bcce.strip() for bcce in bcc_emails.split(',')] if bcc_emails else []

    for row in tqdm(csv_data, desc='Sending emails', unit='email'):
        assert 'to_email' in row, "'to_email' should be present in the CSV for sending emails"

        to_email = row['to_email']
        to_email = [te.strip() for te in to_email.split(',')]

        __plain_email_body = replace_placeholders(row, plain_email_body)
        __html_email_body = replace_placeholders(row, html_email_body) if html_email_body else None

        email_obj.send_email(to_email, subject, __plain_email_body, __html_email_body, cc_emails, bcc_emails,
                             attachment_list)

        time.sleep(0.5)


if __name__ == '__main__':
    main()
