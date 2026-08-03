import typer
import click
# import pyserial
import serial
import os
import csv


from typing_extensions import Annotated

def dataAcquisition():
    ans = ""
    ser = serial.Serial("/dev/cu.usbserial-AP08ZHFT", timeout=1.0)
    ser.baudrate = 9600
    # ser.port = "COM1"
    # fileWrite = csv.writer()
    ser.write(b"S\r")
    ser.read(100)

    while True:
        print()
        ans = input("Press x to quit, r to read ")
        if (ans == "x" or ans == "X"): 
            break
        elif ans=="r" or ans=="R":
            location = typer.prompt("Write sensor distance in centimeters with no space in between. eg) 130 ")
            #ls = location.split(',')
            ls = [location]
            # print("jhdfj")
            ser.write(b"D\r")
            # print("serial read failure")
            reading = ser.read(100)
            # print("reading decode failure")
            reading = reading.decode('utf-8').strip()
            # print(reading)
            reading = reading[3:]
            # print(reading)
            ls2 = reading.split(" ")
            ls = ls+ls2
            file_exists = os.path.exists("output.csv")
            with open('output.csv', 'a') as csvfile:
                filewrite = csv.DictWriter(csvfile, delimiter=" ", quoting=csv.QUOTE_MINIMAL, fieldnames=["distance","bx","by","bz"])
                if not (file_exists):
                    filewrite.writeheader()
                filewrite.writerow({"distance":ls[0], "bx":ls[1], "by":ls[2], "bz":ls[3]})
            print(ls)
    with open('output.csv') as csvfile:
        fileread = csv.reader(csvfile)
        for row in fileread:
            print(', '.join(row))
   
    # click.pause(info=)