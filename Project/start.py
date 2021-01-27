from ssibag.startup import StartupEnvironment
import os

def startup(ip):
    c = StartupEnvironment()
    c.setup(ip)
def endup(ip):
    c = StartupEnvironment()
    c.endup(ip)

if __name__ == "__main__":
    # manually do: sudo service ssh start, if not done yet.
    IP="172.22.250.48"  # check if environment changed IP address
    startup(IP)
