# reference: https://kctheservant.medium.com/demonstration-of-hyperledger-aries-cloud-agent-6e476a5426b0

import os
import socket
import paramiko
import time
import webbrowser

class StartupEnvironment:
	def setup(self, vhost):
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
			OK=1
			print('SSH is successful to device ' + vhost)

		if(OK==1):
			stdin, stdout, stderr = SSH.exec_command('sudo -S service docker start')
			stdin.write('ubu20w'+'\n')
			stdin.flush()
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
			print("wait a minute and 1/2 for connecting ledger servers .....")
			time.sleep(90)
			#for line in stdout.read().splitlines():
			#	print(line.decode('utf-8'))
			#stdin, stdout, stderr = SSH.exec_command('bash /home/ubu20w/von-network/manage build')
			#for line in stdout.read().splitlines():
			#	print(line.decode('utf-8'))
			stdin, stdout, stderr = SSH.exec_command('bash /home/ubu20w/von-network/manage up')
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
			stdin, stdout, stderr = SSH.exec_command('sudo -S netstat -antp')
			stdin.write('ubu20w'+'\n')
			stdin.flush()
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
			new=2 # open a tab in web browser
			url="http://localhost:9000"
			webbrowser.open(url,new=new)
			print("tab xx.xx.xx.xx:9000 is opened in browser")
			print("Ready to run use case Faber, ACME, Alice, and Bob")
		SSH.close()
		print('SSH is closed')


	def endup(self, vhost):
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
			#stdin, stdout, stderr = SSH.exec_command('bash /home/ubu20w/von-network/manage stop')
			#print("manage stop")
			#for line in stdout.read().splitlines():
			#	print(line.decode('utf-8'))

			stdin, stdout, stderr = SSH.exec_command('bash /home/ubu20w/von-network/manage down')
			print("manage down")
			#for line in stdout.read().splitlines():
			#	print(line.decode('utf-8'))
			print("wait more or less 5 minutes for complete closure of ports 9701 .. 9705")
			print("stay checking with netstat")
			time.sleep(60)

			stdin, stdout, stderr = SSH.exec_command('sudo -S netstat -antp')
			stdin.write('ubu20w' + '\n')
			for line in stdout.read().splitlines():
				print(line.decode('utf-8'))
		SSH.close()
		print('SSH is closed')
