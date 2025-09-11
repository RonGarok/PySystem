import subprocess
import sys

required_modules = ["PyQt5", "flask", "requests", "art", "ascii_art"]

def ensure_pip():
    try:
        import pip
        print("✅ pip is already installed.")
    except ImportError:
        print("📦 Installing pip...")
        subprocess.run([sys.executable, "-m", "ensurepip", "--default-pip"])

def check_and_install(package):
    try:
        __import__(package)
        print(f"✅ {package} is installed.")
    except ImportError:
        print(f"📦 Installing {package}...")
        subprocess.run([sys.executable, "-m", "pip", "install", package])

if __name__ == "__main__":
    ensure_pip()
    for module in required_modules:
        check_and_install(module)

    # Lancer le bureau graphique
    subprocess.run(["python3", "/system32.py"])