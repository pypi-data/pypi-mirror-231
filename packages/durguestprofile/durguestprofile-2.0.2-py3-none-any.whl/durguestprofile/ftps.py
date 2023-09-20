

import pysftp
import os
from durguestprofile import properties_score

# Replace with your FTP server details
ftp_server = '82.147.196.78'
ftp_user = 'opera'
ftp_password = 'OpConn@2023#'
remote_directory = '/Opera/Guest_Data'
files_path = fr'C:\Users\muham\Desktop\Dur\data'  # Where you want to save the downloaded files


cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Download the missing files only, the SFTP connection is automatically closed when exiting the "with" block
with pysftp.Connection(host=ftp_server, username=ftp_user, password=ftp_password, cnopts=cnopts) as sftp:
    # Change to the remote directory
    sftp.chdir(remote_directory)

    # List files in the remote directory
    file_list = sftp.listdir()

    # Download each file to the local directory
    for file_name in file_list:
        if file_name not in os.listdir(files_path):
            remote_file_path = f'{remote_directory}/{file_name}'
            local_file_path = f'{files_path}/{file_name}'
            sftp.get(remote_file_path, local_file_path)

# Define the directory where the text or xml files are located,
# the same folder should contain criteria_mapper.xlsx file
data_source = properties_score(
    files_folder=files_path,
    criteria_file=os.path.join(files_path, "criteria_mapper.xlsx")
    )
print(data_source)