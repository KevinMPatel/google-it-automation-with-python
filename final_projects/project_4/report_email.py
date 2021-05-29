#!/usr/bin/env python3

import reports
import os
import emails
from datetime import datetime
import run

def main():
  # to get today's date
  today = datetime.today()
  date, time = str(today).split()

  # title
  title = 'Processed Update on {}'.format(date)
  # Paragraph
  paragraph = ""
  data = run.extract_data('./supplier-data/descriptions/')
  for fruit in data:
    paragraph = paragraph + "<br/><br/>{}<br/>{}<br/>".format(fruit['name'], fruit['weight'])
  # Attachment Path
  attachment_path = './processed.pdf'
  reports.generate_report(attachment_path, title, paragraph)
  # set parameters for email message
  sender = 'automation@example.com'
  recipient = 'student-01-b810bfcba9b8@example.com'
  subject = 'Upload Completed - Online Fruit Store'
  body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
  # generate email message
  message = emails.generate_email(sender, recipient, subject, body, attachment_path)
  # send email
  emails.send_email(message)


if __name__ == "__main__":
  main()

