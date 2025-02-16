import shutil

def is_app_available(app_name):
    return shutil.which(app_name) is not None

# Example usage
app_name = "whatsapp"  # Change this to the application you want to check
if is_app_available(app_name):
    print(f"{app_name} is available in the system.")
else:
    print(f"{app_name} is NOT available in the system.")
