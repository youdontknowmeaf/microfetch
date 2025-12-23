#!/usr/bin/env python3
from os import system as cmd

if cmd("uname | figlet") != 0:
    print("Install 'figlet' to show ASCII art!")
print("-----SOFTWARE-----")
print("System: ")
cmd("uname -o -n -r")
print("Memory: ")
cmd("free -Lh")
print("Drives: ")
cmd("lsblk -A -N")
print("uptime: ")
cmd("uptime")
print("-----HARDWARE-----")
print("GPUs: ")
cmd("lspci | grep -i vga")
print("CPU: ")
cmd('cat /proc/cpuinfo | grep "model name" | head -n 1')
