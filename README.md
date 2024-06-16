# CIP202406Final-HostDiscoveryTool

This project was my Final Project for 2024 Code in Place course at Stanford 

The original idea come from a current need for a standalone network scanning
device

I originally decide to use a spare Single Board Computer to have a watchdog
device, performing repeted check on the status of the other devices

I developed it on a 32-bit Debian Single Borad Computer with 2 Gb of RAM

Visual Studio Code was too heavy for the 1 Gb model

The code currently limit scanning capability to 255 hosts on the same network
as the scanning device, so some checks are performed while requesting user input

To run the code just execute from your shell

python main.py

The output is only on screen

Current release is 17th of June 2024
I am based in Northen Italy
