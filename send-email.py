#!/usr/bin/env python
__author__ = 'kalcho'
# Send emails using different providers

import smtplib
from email.mime.text import MIMEText
import re
import base64


def request_send_info():
    
    info = []
    info.append(raw_input("Enter sender email address: "))
    info.append(raw_input("Enter recepient email address: "))
    info.append(raw_input("Enter email subject: "))
    info.append(raw_input("Enter text to send: "))
    
    return info


def construct_message():
    
    info = request_send_info()
    body = MIMEText(info[3])
    body['From'] = info[0]
    body['To'] = info[1]
    body['Subject'] = info[2]
    
    return body


def send_email(provider):
    
    if re.match(r'outlook.com', provider):
        body = construct_message()
        # TODO: get better method of encryption as this can be
        # potentionaly exploitable, if the execution stack is tempered
        # TODO: Investigate possibility for password hidding (stars),
        # during input
        passwd = base64.b64encode(raw_input("Enter your email password: "))

        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(body['From'], base64.b64decode(passwd))
        server.sendmail(body['From'], body['To'], body.as_string())
        # TODO: investigate close connection result to see if properly
        # send closed
        print server.quit()
    
    elif re.match(r'gmail.com', provider):
        body = construct_message()
        # TODO: get better method of encryption as this can be
        # potentionaly exploitable, if the execution stack is tempered
        # TODO: Investigate possibility for password hidding (stars),
        # during input
        passwd = base64.b64encode(raw_input("Enter your email password: "))

        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.login(body['From'].split('@')[0], base64.b64decode(passwd))
        server_ssl.sendmail(body['From'], body['To'], body.as_string())
        # TODO: investigate close connection result to see if properly
        # send closed
        print server_ssl.quit()
    
    else:
        # TODO: add what happens if neither of previous provided
        # selected
        """Print information that provided not supported"""
        pass


provider = raw_input("Enter your e-mail provider (outlook.com or gmail.com)? ")
send_email(provider)