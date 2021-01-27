from ssibag.execute import ExecuteEnvironment
import os

def startUseCaseEnvironment(ip,who):
    c = ExecuteEnvironment()
    c.startEnvironment(ip,who)

if __name__ == "__main__":
    # manually do: sudo service ssh start, if not done yet.
    IP="172.22.250.48"  # check if environment changed IP address
    startUseCaseEnvironment(IP,"faber")
    #startUseCaseEnvironment(IP,"acme")
    #startUseCaseEnvironment(IP,"alice")
    #startUseCaseEnvironment(IP,"bob")