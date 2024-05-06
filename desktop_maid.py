import os
import shutil

desktop_path = os.path.join(os.path.expanduser('~'),  'Documents')
documents_path = os.path.join(os.path.expanduser('~'), 'Documents')

desktop_parser_path = os.path.join(documents_path, 'DesktopParser')
directories_path = os.path.join(desktop_parser_path, 'Directories')
images_path = os.path.join(desktop_parser_path, 'Images')
pdfs_path = os.path.join(desktop_parser_path, 'Pdfs')


# Create Desktop Parser and its subfolders if they don't exist
for path in [desktop_parser_path, directories_path, images_path, pdfs_path]:
    if not os.path.exists(path):
        os.makedirs(path)

# Move files and folders on the desktop
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)
    if os.path.isfile(item_path):
        if item.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Move images to the Images folder
            shutil.move(item_path, os.path.join(images_path, item))
        elif item.lower().endswith('.pdf'):
            # Move PDFs to the pdfs folder
            shutil.move(item_path, os.path.join(pdfs_path, item))
        elif not item.lower().endswith('.py'):  # Exclude .py files
            # Move other files to Desktop Parser
            shutil.move(item_path, desktop_parser_path)
    elif os.path.isdir(item_path) and not item == ".git":  # Exclude .git directory
        # Move directories to the Directories folder
        shutil.move(item_path, os.path.join(directories_path, item))

# Remove all remaining directories on the desktop
for item in os.listdir(desktop_path):
    item_path = os.path.join(desktop_path, item)
    if os.path.isdir(item_path):
        # Use shutil.rmtree() to remove the directory and its contents
        try:
            shutil.rmtree(item_path)
        except Exception as e:
            print(f"Error removing directory {item}: {e}")