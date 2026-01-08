# System Tray - Guide d'Utilisation

## 🎯 Fonctionnement

Haptic Master tourne maintenant **en arrière-plan** avec une icône dans la **barre des tâches** (system tray).

## 📍 Où Trouver l'Icône

L'icône apparaît dans la **zone de notification** (en bas à droite de l'écran Windows, près de l'horloge).

**Icône** : Cercle bleu 🔵 représentant une souris

> **Note** : Si vous ne voyez pas l'icône immédiatement, cliquez sur la flèche `^` pour afficher les icônes cachées.

## 🖱️ Actions Disponibles

### Double-clic sur l'icône
Affiche/masque la fenêtre principale

### Clic droit sur l'icône
Ouvre un menu avec :

- **Afficher** : Restaure et affiche la fenêtre principale
- **Masquer** : Cache la fenêtre dans le tray
- **Test Haptic** : Lance un test rapide (pattern "pulse")
- **Quitter** : Ferme complètement l'application

## ❌ Fermer la Fenêtre

Quand vous cliquez sur le bouton **X** de la fenêtre :
- ✅ La fenêtre se **cache** dans le tray
- ❌ L'application **ne se ferme PAS**
- ✅ Le serveur web **continue de tourner**
- ✅ Les haptiques web **continuent de fonctionner**

**Pour vraiment quitter** : Clic droit sur l'icône → "Quitter"

## 🚀 Démarrage en Arrière-Plan

Si vous voulez que l'application démarre **directement cachée** (sans afficher la fenêtre) :

1. Ouvrez `haptic_master.py`
2. Trouvez la ligne `self._create_ui()` (ligne ~207)
3. Ajoutez juste après :
   ```python
   self.root.withdraw()  # Démarre caché
   ```

Ou créez un raccourci avec cette option (voir section "Auto-démarrage" ci-dessous).

## 🔄 Auto-démarrage au Login Windows

### Méthode 1 : Via le Dossier de Démarrage

1. Créez l'exécutable avec `.\build.bat`
2. Appuyez sur `Win + R` et tapez : `shell:startup`
3. Créez un raccourci vers `Haptic Master.exe` dans ce dossier

### Méthode 2 : Via le Registre (Avancé)

Créez un fichier `autostart.bat` :

```batch
@echo off
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v "HapticMaster" /t REG_SZ /d "%CD%\dist\Haptic Master.exe" /f
echo Auto-demarrage configure !
pause
```

Exécutez-le en tant qu'administrateur.

## 🎨 Personnaliser l'Icône

L'icône par défaut est un **cercle bleu**. Pour la personnaliser :

1. Ouvrez `haptic_master.py`
2. Trouvez la fonction `_create_tray_icon()` (ligne ~212)
3. Modifiez les couleurs ou remplacez par votre propre image :

```python
def _create_tray_icon(self):
    """Charge une icône personnalisée"""
    return Image.open('mon_icone.png')  # Votre fichier .png
```

## 💡 Astuces

### Notification au Démarrage
L'icône apparaît dès le lancement de l'application. Si Logi Options+ n'est pas configuré, un message s'affichera automatiquement.

### Vérifier que l'App Tourne
Survolez l'icône avec la souris : un tooltip "Haptic Master" s'affiche.

### Test Rapide
Clic droit → "Test Haptic" pour vérifier que tout fonctionne sans ouvrir la fenêtre.

### Serveur Web
Le serveur web (port 26290) tourne **même quand la fenêtre est cachée**. Les haptiques depuis le navigateur fonctionnent normalement.

## 🐛 Dépannage

### L'icône n'apparaît pas
- Vérifiez que `pystray` et `Pillow` sont installés : `pip install pystray Pillow`
- Relancez l'application
- Vérifiez la console pour les erreurs

### Impossible de quitter
- Clic droit sur l'icône → "Quitter"
- Si bloqué : Gestionnaire des tâches → Arrêter "python.exe" ou "Haptic Master.exe"

### Plusieurs icônes apparaissent
- Vous avez lancé l'application plusieurs fois
- Faites clic droit → "Quitter" sur chaque icône

### L'icône disparaît
- L'application s'est fermée (crash ou erreur)
- Vérifiez les logs dans la console
- Relancez l'application

## 📚 Architecture Technique

```python
# Flux de création du tray :
__init__()
  └─ _create_ui()         # Crée l'interface
  └─ _setup_tray()        # Configure le tray
      ├─ _create_tray_icon()   # Génère l'icône
      ├─ pystray.Menu()        # Crée le menu
      └─ tray_icon.run()       # Lance dans un thread

# Gestion de la fenêtre :
WM_DELETE_WINDOW → _hide_window()  # Masque au lieu de fermer
Menu "Quitter" → on_close()         # Ferme vraiment
```

---

**Documentation complète** : [README_WINDOWS.md](README_WINDOWS.md)
