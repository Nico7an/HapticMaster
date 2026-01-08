# Comparaison macOS vs Windows

## Architecture

### macOS (HapticMaster/)
- **Langage**: Swift
- **UI Framework**: SwiftUI
- **Build**: Shell script + SwiftC
- **Distribution**: `.app` bundle
- **Raccourci**: `Cmd + Shift + Ctrl + Opt + U`

### Windows (HapticMaster_Windows/)
- **Langage**: Python 3.8+
- **UI Framework**: tkinter
- **Build**: PyInstaller
- **Distribution**: `.exe` standalone
- **Raccourci**: `Ctrl + Shift + Alt + U`

## Fonctionnalités

| Fonctionnalité | macOS | Windows |
|----------------|-------|---------|
| Serveur Web (port 26290) | ✅ | ✅ |
| Extension navigateur | ✅ | ✅ |
| Patterns haptiques | ✅ | ✅ |
| Interface graphique | ✅ SwiftUI | ✅ tkinter |
| Notifications système | ✅ | ⚠️ À implémenter |
| Logi Options+ requis | ✅ | ✅ |

## Patterns Disponibles

Les deux versions supportent les mêmes patterns :

- `single` : Simple vibration
- `double` : Deux vibrations courtes
- `pulse` : Trois vibrations rapides
- `heartbeat` : Double battement
- `triple` : Triple vibration espacée
- `long` : Vibration longue (buzz)
- `sos` : Pattern SOS morse (... --- ...)
- `engine_start` : Accélération progressive
- `blaster` : Rafale rapide
- `gallop` : Pattern galop

## Communication avec le navigateur

Les deux versions utilisent le même protocole :

**Endpoint**: `http://localhost:26290`
**Méthode**: `POST`
**Format**:
```json
{
  "pattern": "pulse"
}
```

**Réponse**: `200 OK` avec body `"ok"`

## Installation Logi Options+

### macOS
```
Trigger: Cmd + Shift + Ctrl + Opt + U
Action: Haptic Feedback (Max Intensity)
```

### Windows
```
Trigger: Ctrl + Shift + Alt + U
Action: Haptic Feedback (Max Intensity)
```

## Build

### macOS
```bash
cd HapticMaster
./build_with_icon.sh
```
Génère: `Haptic Master.app`

### Windows
```batch
cd HapticMaster_Windows
build.bat
```
Génère: `dist\Haptic Master.exe`

## Dépendances

### macOS
- Aucune dépendance externe
- Swift natif (fourni avec Xcode Command Line Tools)

### Windows
- Python 3.8+
- `keyboard` (pour envoyer les raccourcis)
- `pyinstaller` (pour builder l'exécutable)

## Points d'amélioration futurs

### macOS
- ✅ Interface "Liquid Glass" complète
- ✅ Monitoring des notifications système
- ⚠️ Icône dans la barre de menu

### Windows
- ✅ Interface tkinter fonctionnelle  
- ⚠️ Monitoring des notifications Windows (WinToast)
- ⚠️ Icône dans la barre des tâches (system tray)
- ⚠️ Auto-démarrage au login

## Extensions navigateur

Les extensions sont **identiques** pour macOS et Windows car elles communiquent avec le serveur local via HTTP sur le port 26290.

Dossiers :
- `extension/` : Chrome/Edge/Brave (Manifest V3)
- `extension_firefox/` : Firefox (Manifest V2)

## Licence

Les deux versions : **MIT License** © 2026 Chamuka Dilshan
