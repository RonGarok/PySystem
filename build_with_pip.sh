#!/bin/bash

echo "🔧 Activation de pip dans Buildroot..."

# Active pip dans la config
make BR2_PACKAGE_PYTHON3_PIP=y

echo "📁 Vérification de l'overlay..."
OVERLAY_PATH="overlay"
if [ ! -d "$OVERLAY_PATH" ]; then
    echo "❌ Dossier overlay introuvable !"
    exit 1
fi

echo "🚀 Lancement de la compilation..."
make

if [ $? -eq 0 ]; then
    echo "✅ Compilation terminée avec succès !"
    echo "📦 Fichiers générés dans output/images/"
    echo "💻 Tu peux booter avec :"
    echo "qemu-system-x86_64 -kernel output/images/bzImage -initrd output/images/rootfs.cpio.gz"
else
    echo "❌ Erreur pendant la compilation."
    exit 1
fi