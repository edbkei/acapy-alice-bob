# reference: https://kctheservant.medium.com/demonstration-of-hyperledger-aries-cloud-agent-6e476a5426b0

import os
import socket
import paramiko
import time
import webbrowser

class Switch():
    def switch(self, port):
        default = "9999"
        return getattr(self, str(port), lambda: default)()

    def faber(self):
        return "8021"

    def acme(self):
        return "8041"

    def alice(self):
        return "8031"

    def bob(self):
        return "8051"

class ExecuteEnvironment:

	def startEnvironment(self, vhost, vwho):
		vport = 22
		vusername = "ubu20w"
		vpassword = "ubu20w"

		# Lets create an Object SSH
		SSH = paramiko.SSHClient()

		# Lets override the default policy behavior
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		OK=0

		try:
			SSH.connect(vhost, port=vport, username=vusername, password=vpassword)
		except paramiko.AuthenticationException:
			print("Authentication failed, please verify your credential")
		except paramiko.SSHException:
			print("Could not establish SSH connection: %s" % paramiko.SSHException)
		except Exception as TimeoutError:
			print("Unable to connect, please verify network connectivity")
		except socket.timeout as e:
			print("Connection got timed out")
		else:
			print('SSH is successful to device ' + vhost)
			new=2 # open a tab in web browser
			my_port = Switch()
			port_no=my_port.switch(vwho)
			#my_switch = Switch()
			#print(my_switch.switch("alice"))
			print("Port "+port_no)
			url="http://localhost:"+port_no
			webbrowser.open(url,new=new)
			slogan=url+" is opened for "+vwho+" API"
			print(slogan)
			vcommand='bash /home/ubu20w/acapy-alice-bob/demo/run_demo '+vwho
			print(vcommand)
			stdin, stdout, stderr = SSH.exec_command(vcommand, get_pty=True)
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))

	def stopEnvironment(self, vhost):
		vport = 22
		vusername = "ubu20w"
		vpassword = "ubu20w"

		# Lets create an Object SSH
		SSH = paramiko.SSHClient()

		# Lets override the default policy behavior
		SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		OK = 0

		try:
			SSH.connect(vhost, port=vport, username=vusername, password=vpassword)
		except paramiko.AuthenticationException:
			print("Authentication failed, please verify your credential")
		except paramiko.SSHException:
			print("Could not establish SSH connection: %s" % paramiko.SSHException)
		except Exception as TimeoutError:
			print("Unable to connect, please verify network connectivity")
		except socket.timeout as e:
			print("Connection got timed out")
		else:
			OK = 1
			print('SSH is successful to device for stop ' + vhost)

		if (OK == 1):
			stdin, stdout, stderr = SSH.exec_command('bash /home/ubu20w/von-network/manage down')
			print("manage down")
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
			print("manage stop")
			dockercmd='bash docker container rm $(docker container ls -aq)'
			print(dockercmd)
			stdin, stdout, stderr = SSH.exec_command(dockercmd)
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
			print("wait more or less 5 minutes for complete closure of ports 9701 .. 9705")
			print("stay checking with netstat")
			time.sleep(60)

			stdin, stdout, stderr = SSH.exec_command('sudo -S netstat -antp')
			stdin.write('ubu20w' + '\n')
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
		SSH.close()
		print('SSH is closed')
