import os

def main():
    print("🔥 Welcome User to PySystem 🔥")
    while True:
        cmd = input("PySystem> ")
        if cmd == "exit":
            print("Shutting down...")
            break
        elif cmd == "hello":
            print("Hello there!")
        elif cmd == "ls":
            print("\n".join(os.listdir()))
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
