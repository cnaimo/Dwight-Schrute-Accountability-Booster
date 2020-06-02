import os
import json
from pathlib import Path
import smtplib
import mimetypes
from datetime import datetime, timedelta
from threading import Thread
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
import config
import logging

app = Flask(__name__)


def send_accountability_msg(wait=True):
    if wait:
        # sleep until 5PM
        now = datetime.now()
        send_time = datetime.now().replace(hour=17, minute=0, microsecond=0)
        if now > send_time:
            # after 5PM, wait for tomorrow
            send_time += timedelta(days=1)
            logging.info("Email thread sleeping until tomorrow at 5PM")
        else:
            logging.info("Email thread sleeping until 5PM")
        time.sleep((send_time - now).seconds)

    msg = MIMEMultipart()
    msg['Subject'] = config.accountability_email_subject
    msg['From'] = config.gmail_username
    msg['To'] = config.robert_california_email_addr

    with open(config.accountability_email_msg_file, 'r') as fp:
        msg.attach(MIMEText(fp.read()))

    for file in os.listdir(config.attachment_dir):
        full_path = os.path.join(config.attachment_dir, file)
        c_type, encoding = mimetypes.guess_type(full_path)
        maintype, subtype = c_type.split('/', 1)
        attachment = MIMEBase(maintype, subtype)
        with open(full_path, 'rb') as fp:
            attachment.set_payload(fp.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition',
                              'attachment; filename="{}"'.format(Path(file).name))
        msg.attach(attachment)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(config.gmail_username, config.gmail_authentication)
    server.sendmail(config.gmail_username, config.robert_california_email_addr, msg.as_string())
    logging.info("Accountability email sent!")


@app.route('/api/add_strikes', methods=['POST'])
def add_strikes():
    data = request.json
    with open(config.office_stats_file, 'r') as fp:
        stats = json.load(fp)

    stats['Strikes'] += data['strikes to add']
    if stats['Strikes'] >= 5:
        stats['Home Runs'] = 1
    with open(config.office_stats_file, 'w') as fp:
        json.dump(stats, fp, indent=4)
    if stats['Home Runs'] == 1:
        thread = Thread(target=send_accountability_msg)
        thread.start()
        return "Success! Accountability email will be sent!"
    return "Success!"


@app.route('/api/office_stats', methods=['GET'])
def office_stats():
    with open(config.office_stats_file, 'r') as fp:
        return jsonify(json.load(fp))


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(host=config.flask_host_ip, port=config.flask_port)


