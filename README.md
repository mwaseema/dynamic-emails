# Motivation

Motivation for this is to send personalized emails based on a plain text or HTML template using data from a CSV file.

# Prerequisite

You need a PC with following requirements:

- Python 3.6 and above
- Git

# Installation and Getting Started

Following command can be used to install the package:

`python -m pip install git+https://github.com/mwaseema/dynamic-emails.git`

Following command can be used to send the emails:

`python -m dynamic_emails --smtp-host "smtp.gmail.com" --smtp-port 465 --from-email "your-email-address-here" --app-key "your-app-key-here" --subject "Email subject" --data-csv-file "path-to-csv-file.csv" --plain-email-body-file "path-to-plain-email-body.txt" --html-email-body-file "path-to-html-email-body.html" --attachment "path-to-attachment-file-or-folder-of-attachments"`

## Flags

`--smtp-host` if you are using Gmail for sending your email then use the above mentioned server for this flag. You’ll have to look for an SMTP server for other services like Outlook and Ymail.

`--smtp-port` 465 is the default port for most of the SMTP mail servers but this may vary if you want to use some other service such as Outlook or Ymail.

`--from-email` You'll need to give your email address which will be used for authentication on the server and will be used for sending out emails.

`--app-key` You'll need to put your app key or password here. If you are using gmail and don't have 2 factor authentication enabled on your gmail then this can be the password of your account. I would suggest you to enable 2 factor authentication and generate an app password for your account. Visit [here](https://myaccount.google.com/apppasswords) for generating app password for your gmail account.

`--subject` This will be used as an email subject.

`--data-csv-file` Path to CSV file containing data for sending emails. `email_to` column is essential in the CSV file and you can have as many columns as you want. First row in the CSV will be representing column names. Try to use lower case letters for columns without spaces and only use dashes and underscores between them.

`--plain-email-body-file` This should be the absolute path of the .txt file containing your email body in plain text form.

`--html-email-body-file` **(Optional)** This should contain an absolute path to the .html file. If you know how formatting in HTML works, you can format your email using HTML and attach that file path here. Even if this is provided, a plain email body is still required because some email readers don’t parse HTML content and only process plain text of the email.

`--attachment` **(Optional)** This should be an absolute path to a file which you want to send as attachment or absolute path to a folder which contains different files which will be sent as attachments.

# Sample Files

[sample_files](https://github.com/mwaseema/dynamic-emails/tree/main/sample_files) folder contains `html_body.html`, `plain_body.txt` and `data.csv` files. Minimum requirement for the `data.csv` file is to contain `email_to` column. Other than this, any number of columns with unique names can be added. These columns can be referenced in the plain text and html email body templates i.e. `{{email_to}}`

`email_to` column in the CSV file can have multiple emails separated by a comma e.g. abc@example.com, abc2@example.com

# Caution
Every email provider can have different limits on number of emails per second and per day. Gmail has a limit of 2000 per day, please make sure you don't go beyond that or your account can be suspened temporarily.
