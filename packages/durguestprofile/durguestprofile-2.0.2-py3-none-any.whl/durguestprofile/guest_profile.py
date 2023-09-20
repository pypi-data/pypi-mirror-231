from durguestprofile import properties_score
import os

from ftplib import FTP

# Replace with your FTP server details
ftp_server = '82.147.196.78'
ftp_user = 'opera'
ftp_password = 'OpConn@2023#'
remote_directory = '/path/to/remote/directory'
local_directory = '/path/to/local/directory'  # Where you want to save the downloaded files

# Connect to the FTP server
ftp = FTP(ftp_server)
ftp.login(user=ftp_user, passwd=ftp_password)

# Change to the remote directory
ftp.cwd(remote_directory)

# List files in the remote directory
file_list = ftp.nlst()

# Download files to the local directory
for file_name in file_list:
    local_file_path = f'{local_directory}/{file_name}'
    with open(local_file_path, 'wb') as local_file:
        ftp.retrbinary(f'RETR {file_name}', local_file.write)

# Close the FTP connection
ftp.quit()







# Define the directory where the text or xml files are located,
# the same folder should contain criteria_mapper.xlsx file
files_path = r"C:\Users\user\Desktop\Dur\testfiles"
data_source = properties_score(
    files_folder=files_path, 
    criteria_file=os.path.join(files_path, "criteria_mapper.xlsx")
    )
print(data_source)