# 🚀 Guide de Déploiement - Haptic Master.exe

## ✅ Build Réussi !

L'exécutable a été créé avec succès :
- **Emplacement** : `dist\Haptic Master.exe`
- **Taille** : ~265 Ko
- **Type** : Exécutable standalone (aucune dépendance requise)

## 📦 Distribution

### Fichiers à Distribuer

**Fichier unique** :
```
dist\Haptic Master.exe
```

C'est tout ! L'exécutable contient :
- ✅ Python embarqué
- ✅ Toutes les bibliothèques (keyboard, pystray, Pillow, tkinter)
- ✅ Le serveur web
- ✅ L'icône du system tray

### Installation pour l'Utilisateur

1. Copier `Haptic Master.exe` n'importe où (Bureau, Program Files, etc.)
2. Double-cliquer pour lancer
3. **Important** : Windows Defender peut bloquer l'application (normal pour les .exe non signés)
   - Cliquer sur "Plus d'infos"
   - Puis "Exécuter quand même"

## 🎯 Prérequis pour l'Utilisateur

- **Windows 10/11**
- **Souris Logitech MX Master 3/3S/4**
- **Logi Options+** installé et configuré avec le raccourci `Ctrl+Shift+Alt+U` → Haptic Feedback

## 🔧 Configuration Logi Options+

L'utilisateur doit configurer une Smart Action :
1. Ouvrir **Logi Options+**
2. **Smart Actions** → **Créer une Smart Action**
3. **Déclencheur** : Raccourci `Ctrl + Shift + Alt + U`
4. **Action** : **Haptic Feedback** (Intensité Max)

## 🌐 Extension Navigateur

L'extension est dans le dossier `extension/` (Chrome/Edge/Brave) ou `extension_firefox/` (Firefox).

### Installation Chrome/Edge/Brave
1. Aller sur `chrome://extensions`
2. Activer "Mode développeur"
3. "Charger l'extension non empaquetée"
4. Sélectionner le dossier `extension`

### Installation Firefox
1. Aller sur `about:debugging`
2. "Charger un module temporaire"
3. Sélectionner `manifest.json` dans `extension_firefox`

## 🎨 Améliorer l'Exécutable

### Ajouter une Icône Personnalisée

Le build actuel utilise l'icône Python par défaut. Pour ajouter une icône personnalisée :

1. **Créer/Trouver une icône** (format .ico, 256x256 recommandé)
2. **Placer le fichier** `icon.ico` dans le dossier `HapticMaster_Windows/`
3. **Rebuilder** avec `.\build.bat`

Ou manuellement :
```bash
pyinstaller --onefile --windowed --name "Haptic Master" --icon=chemin\vers\icone.ico haptic_master.py
```

### Signer l'Exécutable (Avancé)

Pour éviter l'avertissement Windows Defender, vous pouvez signer l'exécutable avec un certificat de signature de code.

**Outils** :
- SignTool.exe (Windows SDK)
- Certificat de signature de code (~200-400€/an)

**Commande** :
```bash
signtool sign /f certificat.pfx /p motdepasse /t http://timestamp.digicert.com "dist\Haptic Master.exe"
```

## 📂 Structure de Distribution Complète

Pour distribuer un package complet :

```
HapticMaster_Windows_Package/
├── Haptic Master.exe              # Application principale
├── extension/                     # Extension Chrome/Edge/Brave
│   ├── manifest.json
│   ├── background.js
│   ├── content.js
│   ├── popup.html
│   └── ...
├── extension_firefox/             # Extension Firefox
│   └── ...
├── README.md                      # Instructions
└── SETUP_GUIDE.md                # Guide de configuration
```

## 🔄 Auto-démarrage au Login

### Méthode Manuelle
1. Appuyer sur `Win + R`
2. Tapez `shell:startup`
3. Créez un raccourci vers `Haptic Master.exe` dans ce dossier

### Via Script
Créer `setup_autostart.bat` :
```batch
@echo off
set "TARGET=%~dp0Haptic Master.exe"
set "SHORTCUT=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\Haptic Master.lnk"

powershell -Command "$WS = New-Object -ComObject WScript.Shell; $SC = $WS.CreateShortcut('%SHORTCUT%'); $SC.TargetPath = '%TARGET%'; $SC.Save()"

echo Auto-demarrage configure !
pause
```

## 🐛 Dépannage

### L'exécutable ne démarre pas
- Vérifier que Windows Defender ne bloque pas
- Lancer depuis un terminal pour voir les erreurs : `"Haptic Master.exe"`
- Vérifier les logs Windows (Observateur d'événements)

### Erreur "VCRUNTIME140.dll manquant"
- Installer [Visual C++ Redistributable](https://learn.microsoft.com/cpp/windows/latest-supported-vc-redist)

### Le serveur ne démarre pas
- Vérifier que le port 26290 est libre
- Désactiver temporairement le pare-feu pour tester

## 📊 Taille de l'Exécutable

**Optimisations possibles** :

### Option 1 : UPX Compression
```bash
upx --best "dist\Haptic Master.exe"
```
Peut réduire de 30-40% mais peut déclencher certains antivirus.

### Option 2 : Exclure des modules non utilisés
Dans `build.bat`, ajouter des exclusions :
```bash
pyinstaller --onefile --windowed --exclude-module matplotlib --exclude-module numpy ...
```

## 🎉 Distribution Finale

L'exécutable est maintenant prêt à être distribué !

**Recommandations** :
- ✅ Tester sur une machine Windows propre
- ✅ Créer un README.txt simple pour les utilisateurs
- ✅ Fournir l'extension navigateur séparément
- ✅ Mentionner les prérequis (Logi Options+)

---

**Build Date** : 2026-01-08  
**Version** : 1.0.0  
**Taille** : 265 Ko  
**Plateforme** : Windows 10/11 (x64)
