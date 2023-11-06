import pywinrm #Connection with WinRM (Windows Remote Management).

remote_computer_name = 'http://your_remote_computer:5985/wsman'
username = 'admin'
password = 'Password!'

session = pywinrm.Session(remote_computer_name, auth=(username, password))

# Command for the distant bat-file
script = 'C:\Documentation\Compile.bat'
command = f'start /b {script}'
result = session.run_ps(command)

# Results
print("Exit status:", result.status_code)
print("Output:", result.std_out)
print("Error:", result.std_err)