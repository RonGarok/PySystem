import time
import subprocess

def boot_animation():
    for i in range(10):
        print(f"🌀 Booting PySystem... [{i+1}/10]")
        time.sleep(1)

def launch_dpck():
    subprocess.run(["python3", "/DPCK.py"])

if __name__ == "__main__":
    boot_animation()
    launch_dpck()