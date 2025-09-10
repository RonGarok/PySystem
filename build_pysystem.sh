#!/bin/bash

echo "🚀 Initialisation de PySystem..."

# 1. Cloner Buildroot si pas déjà présent
if [ ! -d "buildroot" ]; then
    echo "📦 Clonage de Buildroot..."
    git clone https://github.com/buildroot/buildroot.git
fi

cd buildroot

# 2. Créer le fichier de configuration minimal
echo "🛠️ Création du fichier de config personnalisé..."
cat <<EOF > ../my_defconfig
BR2_x86_64=y
BR2_PACKAGE_PYTHON3=y
BR2_ROOTFS_OVERLAY="../overlay"
EOF

# 3. Appliquer la config
make O=output my_defconfig

# 4. Créer l'overlay avec boot.py et le script init
echo "📁 Création de l'overlay..."
mkdir -p ../overlay/etc/init.d
cat <<EOF > ../overlay/boot.py
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
            print("\\n".join(os.listdir()))
        else:
            print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
EOF

cat <<EOF > ../overlay/etc/init.d/S99boot
#!/bin/sh
echo "Launching PySystem..."
exec python3 /boot.py
EOF

chmod +x ../overlay/etc/init.d/S99boot

# 5. Lancer la compilation
echo "🔨 Compilation de l'image..."
make O=output

echo "✅ Compilation terminée. Tu peux maintenant lancer PySystem avec QEMU :"
echo "qemu-system-x86_64 -kernel output/images/bzImage -initrd output/images/rootfs.cpio.gz -nographic"