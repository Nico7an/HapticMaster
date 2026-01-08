# Haptic Master - Guide d'Installation Rapide

## 🎯 Qu'est-ce que c'est ?

Haptic Master ajoute des **vibrations haptiques** à votre souris Logitech MX Master lors de vos interactions web (clics, survol, etc.).

## ⚡ Installation Express

### 1. Prérequis
- Windows 10/11
- Souris **Logitech MX Master 3/3S/4**
- **Logi Options+** installé ([Télécharger ici](https://www.logitech.com/software/logi-options-plus.html))

### 2. Lancer l'Application
1. Double-cliquez sur **Haptic Master.exe**
2. Windows peut afficher un avertissement → Cliquez "Plus d'infos" puis "Exécuter quand même"
3. L'application démarre avec une icône 🔵 dans la barre des tâches (près de l'horloge)

### 3. Configurer Logi Options+
**IMPORTANT** : Cette étape est obligatoire !

1. Ouvrez **Logi Options+**
2. Allez dans **Smart Actions** → **Créer une Smart Action**
3. Configurez :
   - **Déclencheur** : Raccourci clavier → `Ctrl + Shift + Alt + U`
   - **Action** : Haptic Feedback → **Intensité Maximum**
4. Enregistrez

### 4. Tester
1. Cliquez sur l'icône 🔵 dans la barre des tâches pour afficher la fenêtre
2. Cliquez sur **"Test Haptic"**
3. Votre souris devrait vibrer 3 fois

✅ Si ça vibre = tout fonctionne !  
❌ Si rien = vérifiez l'étape 3

## 🌐 Extension Navigateur (Optionnel)

Pour les haptiques sur les sites web :

### Chrome / Edge / Brave
1. Ouvrez `chrome://extensions`
2. Activez "Mode développeur" (en haut à droite)
3. Cliquez "Charger l'extension non empaquetée"
4. Sélectionnez le dossier `extension`

### Firefox
1. Ouvrez `about:debugging`
2. Cliquez "Charger un module temporaire"
3. Sélectionnez le fichier `manifest.json` dans le dossier `extension_firefox`

L'extension devrait afficher "Connected" en vert.

## 🖱️ Utilisation

### Icône dans la Barre des Tâches
- **Double-clic** : Affiche/cache la fenêtre
- **Clic droit** → Menu :
  - Afficher
  - Masquer
  - Test Haptic
  - Quitter

### Fermer la Fenêtre
Cliquer sur ❌ **cache** l'application dans la barre des tâches (elle continue de tourner).

Pour **vraiment quitter** : Clic droit sur l'icône → "Quitter"

## ⚙️ Paramètres

Dans la fenêtre de l'application :

- **System Notifications** : Active les haptiques pour les notifications Windows (à venir)
- **Vibration Type** : Choisissez le pattern (Pulse, Double, Triple, etc.)
- **Web Browser** : Active/désactive les haptiques depuis le navigateur

## 🐛 Problèmes Courants

### La souris ne vibre pas
1. Vérifiez que **Logi Options+** est lancé
2. Vérifiez la configuration de la Smart Action (étape 3)
3. Testez le raccourci manuellement : appuyez sur `Ctrl+Shift+Alt+U`

### L'extension dit "Disconnected"
1. Vérifiez que **Haptic Master** est lancé (icône 🔵 dans la barre des tâches)
2. Vérifiez que le serveur est "Listening on Port 26290" (dans la fenêtre)
3. Rechargez l'extension navigateur

### Windows Defender bloque l'application
C'est normal pour les applications non signées :
1. Cliquez "Plus d'infos"
2. Puis "Exécuter quand même"

### Impossible de trouver l'icône
L'icône 🔵 est dans la zone de notification (en bas à droite).
Si vous ne la voyez pas, cliquez sur la flèche `^` pour afficher les icônes cachées.

## 🚀 Auto-démarrage (Optionnel)

Pour que l'application démarre automatiquement au login Windows :

1. Appuyez sur `Win + R`
2. Tapez `shell:startup` et validez
3. Créez un raccourci vers `Haptic Master.exe` dans ce dossier

## 📚 Plus d'Informations

- **Patterns disponibles** : Single, Double, Pulse, Heartbeat, Triple, Long, SOS, Engine Start, Blaster, Gallop
- **Port serveur** : 26290 (localhost)
- **Configuration** : Stockée dans `config.txt`

## 🆘 Support

Pour plus d'aide, consultez les fichiers :
- `SETUP_GUIDE.md` - Guide détaillé de configuration
- `TRAY_GUIDE.md` - Guide de la barre des tâches
- `README_WINDOWS.md` - Documentation technique complète

---

**Version** : 1.0.0  
**Plateforme** : Windows 10/11  
**License** : MIT

Profitez de vos haptiques ! 🎉
