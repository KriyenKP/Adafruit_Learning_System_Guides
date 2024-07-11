# SPDX-FileCopyrightText: 2024 Liz Clark for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio

# baud rate for your device
baud = 38400
uart = busio.UART(board.TX, board.RX, baudrate=baud)

print("Enter commands to send to the RS-232 device. Press Ctrl+C to exit.")
while True:
    user_input = input("Please enter your command: ").strip()
    if user_input:
        # send the command with a telnet newline (CR + LF)
        uart.write((user_input + "\r\n").encode('ascii'))

    # empty buffer to collect the incoming data
    response_buffer = bytearray()

    # check for data
    time.sleep(1)
    while uart.in_waiting:
        data = uart.read(uart.in_waiting)
        if data:
            response_buffer.extend(data)

    # decode and print
    if response_buffer:
        print(response_buffer.decode('ascii'), end='')
        print()
