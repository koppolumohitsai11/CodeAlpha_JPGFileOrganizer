import os
import shutil

print("==========================================")
print("       JPG FILE ORGANIZER")
print("==========================================")

# Get source and destination folder paths
source_folder = input("Enter source folder path: ")
destination_folder = input("Enter destination folder path: ")

# Check whether source folder exists
if not os.path.exists(source_folder):
    print("\nSource folder does not exist.")
    exit()

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)
    print("\nDestination folder created.")

# Count moved files
moved_files = 0

# Check files in the source folder
for file_name in os.listdir(source_folder):

    # Check whether the file is a JPG file
    if file_name.lower().endswith(".jpg"):

        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Move the file
        shutil.move(source_path, destination_path)

        print(f"Moved: {file_name}")

        moved_files += 1

# Display result
print("\n==========================================")
print("             TASK COMPLETED")
print("==========================================")

if moved_files > 0:
    print(f"{moved_files} JPG file(s) moved successfully.")
else:
    print("No JPG files found in the source folder.")