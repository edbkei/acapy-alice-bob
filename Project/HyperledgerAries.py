#!/usr/bin/env python
# coding: utf-8

# # Labs Hyperledger Aries
# 
# 
# ## 1. Get Credential Schema in Faber

# In[1]:


import requests
import json
# pip install openssh-wrapper
# pip install pexpect
# https://pexpect.readthedocs.io/en/stable/api/pxssh.html


# In[2]:


URL='http://localhost:8021/schemas/created'
r=requests.get(URL)
# Check status code for response received
# 200 - success code
print(r)
print(r.content)


# In[3]:


response_dict=json.loads(r.text)
for i in response_dict:
    print("key: ", i, "val: ", response_dict[i][0])
    
# print(r.__dict__)


# In[17]:


print(response_dict)


# In[4]:


from openssh_wrapper import SSHConnection
conn = SSHConnection('172.20.15.87',login='ubu20w')


# In[6]:


# https://mrcissp.com/2019/12/17/python-package-paramiko/
import paramiko
import socket
vhost = "172.22.250.48"
vport = 22
vusername = "ubu20w"
vpassword = "ubu20w"

# Lets create an Object SSH
SSH = paramiko.SSHClient()

# Lets override the default policy behavior
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    SSH.connect(vhost,port=vport,username=vusername,password=vpassword)
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


# In[11]:


SSH.close()


# In[10]:


stdin, stdout, stderr = SSH.exec_command('docker ps')

for line in stdout.read().splitlines():
    print(line)


# In[13]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()


# In[1]:


from ssibag.startup import StartupEnvironment
import os


# In[10]:


p1=StartupEnvironment("John", 36)
print(p1.name)
print(p1.age)


# In[ ]:




