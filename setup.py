'''
@Author: David Liu

@Description: Template Setup file what will:
1. Create a python virtual environment
2. Install a basic set of requirements
3. If requirements.txt file exists, install that set of requirements
3. Create the .env file
'''

import os
import subprocess
import sys

venv_dir = ".venv"

# Create the Virtual Env for where the proj packages will live
def createVirtualEnv():
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir])
    else:
        print("Virtual environment already exists.")

# Install the default packages
def installRequirements():
    print("Installing requirements...")
    
    default_packages = ["requests", "python-dotenv", "watchdog", "pip"]
    subprocess.run(["python3", "-m", "pip", "install", "--upgrade", *default_packages, "-t", ".venv/lib/python3.13/site-packages"])
    if os.path.exists("requirements.txt"):
        subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "-r", "requirements.txt", "-t", ".venv/lib/python3.13/site-packages"])
    
# Create the .env file
def createEnvFile():
    print("Checking .env file")
    env_file = ".env"
    if not os.path.exists(env_file):
        print("Creating .env file...")
        with open(env_file, "w") as file:
            file.write("## Add your environment variables below ##\n")
    else:
        print(".env file already exists!")

if __name__ == "__main__":
    createVirtualEnv()
    installRequirements()
    createEnvFile()
    print("\n✅ Setup complete!")
    print(f"➡️  To activate your virtual environment:\nsource {venv_dir}/bin/activate" if os.name != 'nt' else f"{venv_dir}\\Scripts\\activate.bat")