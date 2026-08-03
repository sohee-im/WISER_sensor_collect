To run the magnetometer reading software:
1. Connect to the magnetometer.
2. Check the USB port that is connected to your computer. (in terminal, type "ls /dev/cu.*" and you will see your connected USB port name)
3. Go to line 13 and replace "/dev/cu.usbserial-AP08ZHFT" with your USB port name.
4. Run the command "python -m src.main" in nVectra directory
5. Type r to start a reading.
6. Type the current standoff distance from the target in cm. When you press enter, it will trigger a reading.
7. Repeat until you are done.
8. When you press x, you will be able to a file named output.csv that has all your reading results. 
