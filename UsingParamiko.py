import paramiko

# Server parameters
hostname = '26.121.251.233'
port = 22  # Port SSH
username = 'admin'
password = 'Password!'

# Path to the files on the distant server
remote_bat_path = 'C:\Documentation\doc.bat'
remote_file_path = 'C:\Documentation\directory.py'

# Create SSH-client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # Connection establishment
    ssh_client.connect(hostname, port, username, password)

    # Command for the distant python-file
    command = f'python {remote_file_path}'

    # Command for the distant bat-file
    command = f'cmd /c {remote_bat_path}'

    # Execute the command
    stdin, stdout, stderr = ssh_client.exec_command(command)

    # Results
    print("stdout:", stdout.read().decode('utf-8'))
    print("stderr:", stderr.read().decode('utf-8')) if stderr.read() else print("stderr: Executed with no errors")           

except Exception as e:
    print("Connection or executiong error:", str(e))
finally:
    # Close SSH=connection
    ssh_client.close()