import os
import base64
import winrm

server = os.environ["WINDOWS_HOST"]
username = os.environ["WINDOWS_USER"]
password = os.environ["WINDOWS_PASSWORD"]
local_script_path = os.environ["LOCAL_SCRIPT_PATH"]
remote_script_path = os.environ["REMOTE_SCRIPT_PATH"]

with open(local_script_path, "rb") as file:
    encoded_content = base64.b64encode(file.read()).decode()

session = winrm.Session(f"http://{server}:5985/wsman", auth=(username, password), transport='ntlm')

powershell_create_script = f"""
$bytes = [System.Convert]::FromBase64String("{encoded_content}")
$path = "{remote_script_path}"
$dir = Split-Path -Path $path
if (!(Test-Path $dir)) {{ New-Item -Path $dir -ItemType Directory -Force | Out-Null }}
[System.IO.File]::WriteAllBytes($path, $bytes)
"""

create_result = session.run_ps(powershell_create_script)
print("File creation output:")
print(create_result.std_out.decode())
print(create_result.std_err.decode())

powershell_run_script = f'powershell.exe -ExecutionPolicy Bypass -File "{remote_script_path}"'
run_result = session.run_cmd(powershell_run_script)

print("Script execution output:")
print(run_result.std_out.decode())
print(run_result.std_err.decode())
