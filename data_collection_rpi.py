import csv
import os
from time import sleep
import datetime
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from picamera import PiCamera
import os, shutil, sys
import urllib.request

# Initialize a counter
count = 0

# Initialize the PiCamera
camera = PiCamera()

# Set the memory path
memory_path = "/home"

# Function to read data from Thingspeak
def read_data_thingspeak():
    URL = 'URL to your thingspeak'
    KEY = 'TestKEY'
    HEADER = '&results=1'
    NEW_URL = URL + KEY + HEADER

    # Get data from Thingspeak API
    get_data = requests.get(NEW_URL).json()

    # Extract field data
    feild_1 = get_data['feeds']
    feild_2 = get_data['feeds']
    feild_3 = get_data['feeds']
    feild_4 = get_data['feeds']

    pms = []
    pmst = []
    t = []
    h = []

    # Extract specific values from field data
    for x in feild_1:
        pms.append(x['field1'])
        pmst.append(x['field2'])
    for x in feild_3:
        t.append(x['field3'])
    for x in feild_4:
        h.append(x['field4'])

    # Return the extracted values
    return t.pop(), h.pop(), pms.pop(), pmst.pop()

# Function to get the current timestamp
def get_time():
    ct = datetime.datetime.now()
    time_stamp = (
        str(ct.year)
        + '-'
        + str(ct.month)
        + '-'
        + str(ct.day)
        + ' '
        + str(ct.hour)
        + ':'
        + str(ct.minute)
        + ':'
        + str(ct.second)
    )
    return time_stamp

# Function to take a picture using PiCamera
def take_picture(time_stamp, save_path):
    camera.start_preview()
    sleep(1)
    camera.capture(save_path)
    camera.stop_preview()

# Initialize email parameters
device_id = "124"
time_stamp = get_time()
mail_content = time_stamp
sender_address = 'enter mail id'
sender_pass = 'password'
receiver_address = 'testmail@gmail.com'
subject_text = device_id
attach_file_name = device_id + ' ' + time_stamp + '.jpg'
save_path = '/home/pi/Desktop/dataset/' + attach_file_name
host = 'http://google.com'

# Function to send an email
def send_email(sender_address, sender_pass, receiver_address, subject_text, attach_file_name, data):
    message = MIMEMultipart()
    message['Subject'] = subject_text
    message['From'] = sender_address
    message['To'] = receiver_address
    message.attach(MIMEText(data, 'plain'))

    # Attach the image file
    attach_file = open(attach_file_name, 'rb')
    data = attach_file.read()
    payload = MIMEBase('application', 'octet-stream')
    payload.set_payload(data)
    encoders.encode_base64(payload)
    payload.add_header('Content-Disposition', 'attachment', filename=attach_file_name)
    message.attach(payload)

    # Create SMTP session to send the email
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except SMTPException:
        print("Error: unable to send email")

# Function to check internet connectivity
def connect(host):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

# Main loop
while True:
    count = count + 1
    if count == 10:
        count = 0
        print("Sleep For 10 Sec")
        sleep(10)

    # Read sensor data from Thingspeak
    temp, humidity, pm, Pm = read_data_thingspeak()

    # Write data to a CSV file
    filename = 'Data.csv'
    time_stamp = get_time()
    data = (
        'Date & Time = '
        + ' '
        + str(time_stamp)
        + '.'
        + ' \n'
        + 'Temperature = '
        + ' '
        + str(temp)
        + '.\n'
        + 'Humidity = '
        + str(humidity)
        + '.\n'
        + 'PM2.5 = '
        + ' '
        + str(pm)
        + '.\n'
        + 'PM10 = '
        + ' '
        + str(Pm)
    )
    
    # Write data to CSV file
    with open(filename, 'a') as file:
        obj = csv.writer(file)
        csvwriter = csv.writer(file)
        rows = [time_stamp, temp, humidity, pm, Pm]
        csvwriter.writerow(rows)

    # Take a picture
    time_stamp = get_time()
    mail_content = time_stamp.split()[0]
    attach_file_name = device_id + ' ' + time_stamp + '.jpg'
    save_path = '/home/pi/Desktop/dataset/' + attach_file_name
    take_picture(time_stamp, save_path)

    # Send email if internet is connected
    if connect(host):
        send_email(sender_address, sender_pass, receiver_address, subject_text, attach_file_name, data)

    # Check available disk space and exit if less than 10GB
    stat = shutil.disk_usage(memory_path)
    if (stat[2] / 1000000000) < 10:
        sys.exit()

    print('Iteration over. Going to sleep.')
    print(count)
    sleep(15)
