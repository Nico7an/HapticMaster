# Haptic Master for Windows ⚡️

[![Windows](https://img.shields.io/badge/platform-Windows-blue.svg)](https://www.microsoft.com/windows/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Feel Your PC.** Immersive Haptic Feedback for Logitech MX Master Users on Windows.

Version Windows de Haptic Master. Connecte vos événements système Windows et vos interactions web directement au moteur haptique de votre souris Logitech MX Master.

## ✨ Features

*   **System Haptics**: Ressentez un battement ou une pulsation lors des notifications Windows.
*   **Web Immersion**: Retour tactile pour les clics et effets de survol dans votre navigateur.
*   **Interface Moderne**: Interface Windows native avec tkinter.
*   **Custom Patterns**: Choisissez parmi Pulse, Double, Triple, Heartbeat, et plus encore.
*   **Privacy First**: 100% local. Aucune donnée ne quitte votre PC.
*   **Open Source**: Code entièrement transparent.

## 🛠 Prérequis

*   **Windows 10/11**
*   **Logitech MX Master 3 / 3S / 4** (Souris supportée)
*   **Logi Options+** installé
*   **Python 3.8+** (pour le développement)

## 🚀 Installation

### 1. L'Application Windows

#### Option A: Utiliser l'exécutable pré-compilé
1.  Téléchargez la dernière release
2.  Lancez `Haptic Master.exe`
3.  **Important**: Windows Defender peut bloquer l'application. Cliquez sur "Plus d'infos" puis "Exécuter quand même"

#### Option B: Builder vous-même
1.  Clonez le repository
2.  Naviguez vers `HapticMaster_Windows`
3.  Lancez `build.bat`
4.  L'exécutable sera dans le dossier `dist\`

### 2. Extensions Navigateur

Les extensions sont les mêmes que pour macOS :

#### Chrome / Edge / Brave
1.  Allez sur `chrome://extensions`
2.  Activez **Mode développeur** (en haut à droite)
3.  Cliquez **Charger l'extension non empaquetée**
4.  Sélectionnez le dossier `extension` du repository

#### Firefox
1.  Allez sur `about:addons`
2.  Cliquez sur l'icône Engrenage ⚙️ → **Installer un module depuis un fichier...** (si vous avez le .xpi signé)
3.  *Ou pour les devs*: Allez sur `about:debugging`, cliquez **Charger un module temporaire**, et sélectionnez le `manifest.json` dans le dossier `extension_firefox`

### 3. Configuration Logi Options+ (CRITIQUE)

Pour que la souris vibre réellement, vous **devez** mapper le raccourci :

1.  Ouvrez **Logi Options+**
2.  Allez dans **Smart Actions** → **Créer une Smart Action**
3.  **Déclencheur**: Raccourci clavier `Ctrl + Shift + Alt + U`
4.  **Action**: **Haptic Feedback** (Sélectionnez intensité maximale)

## 💻 Développement

### Structure du projet

```
HapticMaster_Windows/
├── haptic_master.py      # Application principale
├── requirements.txt      # Dépendances Python
├── build.bat            # Script de build
├── icon.ico             # Icône de l'application
└── README_WINDOWS.md    # Cette documentation
```

### Lancer en mode développement

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application
python haptic_master.py
```

### Builder l'exécutable

```bash
# Windows
build.bat

# Ou manuellement avec PyInstaller
pyinstaller --onefile --windowed --name "Haptic Master" --icon=icon.ico haptic_master.py
```

## 🔧 Architecture

### HapticEngine
Gère les différents patterns haptiques en envoyant le raccourci clavier `Ctrl+Shift+Alt+Win+U` à Logi Options+.

**Patterns disponibles:**
- `single`: Simple vibration
- `double`: Deux vibrations courtes
- `pulse`: Trois vibrations rapides
- `heartbeat`: Double battement
- `triple`: Triple vibration espacée
- `long`: Vibration longue (buzz)
- `sos`: Pattern SOS morse (... --- ...)
- `engine_start`: Accélération progressive
- `blaster`: Rafale rapide
- `gallop`: Pattern galop

### WebServer
Serveur HTTP local sur le port **26290** qui reçoit les requêtes POST de l'extension navigateur avec le format JSON :

```json
{
  "pattern": "pulse"
}
```

### Interface GUI
Interface tkinter moderne avec :
- Toggle pour activer/désactiver les haptiques système
- Sélecteur de pattern pour les notifications
- Toggle pour activer/désactiver les haptiques web
- Indicateur de statut du serveur
- Horodatage du dernier signal reçu

## 🐛 Troubleshooting

### La souris ne vibre pas
1. Vérifiez que **Logi Options+** est bien installé et en cours d'exécution
2. Vérifiez que le raccourci `Ctrl+Shift+Alt+Win+U` est bien mappé à **Haptic Feedback**
3. Testez le raccourci manuellement en appuyant sur les touches
4. Assurez-vous que votre souris MX Master supporte les haptiques

### Le serveur ne démarre pas
1. Vérifiez que le port 26290 n'est pas utilisé par une autre application
2. Vérifiez votre pare-feu Windows
3. Lancez l'application en mode administrateur

### L'extension navigateur ne se connecte pas
1. Vérifiez que l'application Haptic Master est en cours d'exécution
2. Vérifiez que le statut du serveur est "Listening on Port 26290"
3. Rechargez l'extension navigateur
4. Consultez la console du navigateur (F12) pour les erreurs

### L'exécutable est bloqué par Windows Defender
C'est normal pour les applications non signées. Cliquez sur "Plus d'infos" puis "Exécuter quand même".

## 🤝 Contribuer

Les pull requests sont les bienvenues ! Merci d'ouvrir d'abord une issue pour discuter des changements que vous souhaitez apporter.

## 📄 License

[MIT](../LICENSE) © 2026 Chamuka Dilshan.

## 🔗 Liens

- Site web: [hapticmaster.vercel.app](https://hapticmaster.vercel.app/)
- Version macOS: [Voir dossier parent](../)
- Contact: [chamuka.is-a.dev](https://chamuka.is-a.dev)
