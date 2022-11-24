import sys
from colorama import Fore, init # for fancy colors, nothing else
import subprocess
import shlex # usefull for unix command

def main():
    host = sys.argv[1] # get agr 1 host
    if host: 
        print("===Nmap TCP all port is running===")
        run_command(enum_command(nmap),host,outfile())
        

def run_command(command):
    subprocess.run(shlex.split(command)) #subprocess.run get parameter as array and we need to split it by shlex. Shlex can support the space character like "User document"
    
def enum_command(c):
    match c: 
        case "nmap": 
            return "nmap -sV -p-"
    
def outfile(outfile):
    if outfile:
        return ">" + outfile
    else:
        return "> enum_result.txt"
