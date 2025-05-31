import os
import subprocess
import sys

venv_dir = ".venv"

def create_virtualenv():
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", venv_dir])
    else:
        print("Virtual environment already exists.")

def install_requirements():
    print("Installing requirements...")
    subprocess.run(["python3", "-m", "pip", "install", "--upgrade", "-r", "requirements.txt", "-t", ".venv/lib/python3.13/site-packages"])

if __name__ == "__main__":
    create_virtualenv()
    install_requirements()
    print("\n✅ Setup complete!")
    print(f"➡️  To activate your virtual environment:\nsource {venv_dir}/bin/activate" if os.name != 'nt' else f"{venv_dir}\\Scripts\\activate.bat")