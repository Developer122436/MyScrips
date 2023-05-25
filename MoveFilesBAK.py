import os
import shutil

# Source file path
source_file = r'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\Settlements.bak'

# Destination folder path
destination_file = r'C:\Users\dimas\OneDrive\Desktop\Programming\Data Analyst\BAK Files\Settlements.bak'

# Copy the source file to the destination folder
shutil.copy2(source_file, destination_file)

# Replace the existing file in the destination folder
os.replace(source_file, destination_file)
