# Our diligent maid comes equipped with the 'os' module, a powerful tool for navigating the file system.
import os  

# Alongside her trusty 'os' module, she brings the versatile 'shutil' module, aiding in file operations.
import shutil  

# The maid locates the path to the desktop, hidden amidst the user's personal documents.
desktop_path = os.path.join(os.path.expanduser('~'),  'Documents')

# With precision, she determines the path to the 'Documents' folder, her starting point.
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')

# The maid discovers the path leading to the Desktop Parser, a stronghold against desktop chaos.
desktop_parser_path = os.path.join(documents_path, 'DesktopParser')

# She identifies the path to the Directories folder within the Desktop Parser, a haven for organizing folders.
directories_path = os.path.join(desktop_parser_path, 'Directories')

# The maid unveils the path to the Images folder within the Desktop Parser, where visual treasures shall reside.
images_path = os.path.join(desktop_parser_path, 'Images')

# She reveals the path to the PDFs folder within the Desktop Parser, safeguarding knowledge and wisdom.
pdfs_path = os.path.join(desktop_parser_path, 'Pdfs')

# With determination, the maid ensures the creation of necessary folders if they do not already exist.
for path in [desktop_parser_path, directories_path, images_path, pdfs_path]:
    if not os.path.exists(path):
        os.makedirs(path)

# The maid meticulously sifts through each item on the desktop, sorting them into their rightful places.
for item in os.listdir(desktop_path):
    # The maid constructs the full path to the current item on the desktop by joining the desktop path with the item's name.
    item_path = os.path.join(desktop_path, item)
    if os.path.isfile(item_path):  # If the item is a file...
        if item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # ... and it's an image file, she carefully relocates it to the Images folder.
            shutil.move(item_path, os.path.join(images_path, item))
        elif item.lower().endswith('.pdf'):
            # ... and it's a PDF, she swiftly moves it to the PDFs folder.
            shutil.move(item_path, os.path.join(pdfs_path, item))
        elif not item.lower().endswith('.py'):  # If it's not a Python script...
            # ... she transports it to the Desktop Parser folder, maintaining order amidst the chaos.
            shutil.move(item_path, desktop_parser_path)
    elif os.path.isdir(item_path) and not item == ".git":  # If it's a directory (folder) and not a .git directory...
        # ... she guides it to the Directories folder, ensuring all folders are neatly organized.
        shutil.move(item_path, os.path.join(directories_path, item))

# With resolve, the maid returns to the desktop to confront any remaining clutter.
for item in os.listdir(desktop_path):
    # The maid constructs the full path to the current item on the desktop by joining the desktop path with the item's name.
    item_path = os.path.join(desktop_path, item)
    if os.path.isdir(item_path):  # If the item is a directory...
        try:
            # ... she invokes her power to remove it and all its contents, leaving no trace behind.
            shutil.rmtree(item_path)
        except Exception as e:
            # In case of any obstacles encountered during the cleaning process, the maid remains vigilant and reports the issue.
            print(f"Error removing directory {item}: {e}")
