import serial
import time

serial_port = 'COM7'
baud_rate = 9600
write_to_file_path = "output.txt"
output_file = open(write_to_file_path, "w+")
ser = serial.Serial(serial_port, baud_rate)
start_time = time.time()
while True:
    line = ser.readline();
    line = line.decode("utf-8")
    print(line);
    output_file.write(line)

    current_time = time.time()
    if (current_time > start_time + 5):
        output_file.close()
        break
