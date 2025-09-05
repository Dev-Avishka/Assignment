import os

def Restart_The_Quiz():
    print("Restarting quiz...")
    os.system("cls" if os.name == "nt" else "clear")  # Clear console (cross-platform)
    return True  # Signal to restart