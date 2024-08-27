import os
import tkinter as tk
from tkinter import filedialog, messagebox

# Initialize Tkinter root window
root = tk.Tk()
root.withdraw()  # Hide root window

# Open dialog to select folder
parent_folder_path = filedialog.askdirectory(title="Select the parent folder")

# Check user selected a folder path
if not parent_folder_path:
    print("No folder selected. Exiting the script.")
else:
    # Walk through all files and directories within the parent folder
    for dirpath, dirnames, filenames in os.walk(parent_folder_path):
        # Iterate over all files in current directory
        for filename in filenames:
            # Check if file has a .txt extension
            if filename.endswith('.txt'):
                # Define full path to current .txt file
                txt_file_path = os.path.join(dirpath, filename)
                # Define new file path with a .py extension
                py_file_path = os.path.join(dirpath, filename[:-4] + '.py')
                # Rename file from .txt to .py
                os.rename(txt_file_path, py_file_path)

    # Display message box to confirm operation complete
    messagebox.showinfo("Operation Completed", "All .txt files have been renamed to .py")

print("All .txt files in the selected folder and its subdirectories have been renamed to .py")


