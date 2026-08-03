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
def test() :
    #
    while True:
        print()
        ans = input("Press x to quit, r to read")
        if (ans == "x" or ans == "X"): 
            break
        elif ans=="r" or ans=="R":
             y = typer.prompt("Say sth")
             print(y)
             # break

def greet(
    # name: Annotated[str, typer.Option(prompt="The (last, if --title is given) name of the person to greet")],
    name: Annotated[str, typer.Argument(help="The (last, if --title is given) name of the person to greet")] = "",
    title: Annotated[str, typer.Option(help="The preferred title of the person to greet")] = "",
    doctor: Annotated[bool, typer.Option(help="Whether the person is a doctor (MD or PhD)")] = False,
    count: Annotated[int, typer.Option(help="Number of times to greet the person")] = 1
):
    greeting = "Greetings, "
    if doctor and not title:
        title = "Dr."
    if not name:
        if title:
            name = title.lower().rstrip(".")
        else:
            name = "friend"
    if title:
        greeting += f"{title} "
    greeting += f"{name}!"
    for i in range(0, count):
        print(greeting)