#coding=utf-8

import paramiko
from time import sleep
import sys
import time

root_command = "whoami\n"
root_command_result = "root"

def send_string_and_wait(command, wait_time, should_print):
    # Send the su command
    shell.send(command)
    # Wait a bit, if necessary
    sleep(wait_time)
    # Flush the receive buffer
    receive_buffer = shell.recv(1024)
    # Print the receive buffer, if necessary
    if should_print:
        print receive_buffer

def send_string_and_wait_for_string(command, wait_string, should_print):
    # Send the su command
    shell.send(command)
    # Create a new receive buffer
    receive_buffer = ""
    while not wait_string in receive_buffer:
        # Flush the receive buffer
        receive_buffer += shell.recv(1024)
    # Print the receive buffer, if necessary
    if should_print:
        print receive_buffer

# Create an SSH client
client = paramiko.SSHClient()

# Make sure that we add the remote server's SSH key automatically
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect to the client
client.connect("192.168.xx.xx", username="xx", password="xx")

# Create a raw shell
shell = client.invoke_shell()

# Send the su command
send_string_and_wait("su\n", 1, True)

# Send the client's su password followed by a newline
send_string_and_wait("xx" + "\n", 1, True)

# Send the install command followed by a newline and wait for the done string
send_string_and_wait_for_string(root_command, root_command_result, True)

send_string_and_wait("cd /export/App/xx/xx/" + "\n", 1, True)
send_string_and_wait("./rc.sh" + "\n", 1, True)
send_string_and_wait("cat now.Log" + "\n", 1, True)
# Close the SSH connection
client.close()
