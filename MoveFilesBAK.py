import shutil

# Source file path
source_file = r'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\Settlements.bak'

# Destination folder path
destination_folder = r'C:\Users\dimas\OneDrive\Desktop\Programming\Data Analyst\BAK Files'

# Transfer the file
shutil.move(source_file, destination_folder)