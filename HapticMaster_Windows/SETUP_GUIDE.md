# Configuration Logi Options+ - Guide Rapide

## ⚙️ Configuration en 4 Étapes

### Étape 1 : Ouvrir Logi Options+
- Lancez l'application **Logi Options+** depuis Windows
- Assurez-vous que votre souris MX Master est connectée

### Étape 2 : Accéder aux Smart Actions
- Dans le menu de gauche, cliquez sur votre souris
- Allez dans l'onglet **"Smart Actions"**
- Cliquez sur **"Créer une Smart Action"** ou **"Create Smart Action"**

### Étape 3 : Configurer le Déclencheur
- **Type** : Sélectionnez "Raccourci clavier" / "Keyboard Shortcut"
- **Raccourci** : Appuyez sur `Ctrl + Shift + Alt + U` ensemble
- L'interface devrait afficher : `Ctrl+Shift+Alt+U`

### Étape 4 : Configurer l'Action
- **Action** : Sélectionnez "Haptic Feedback" / "Retour haptique"
- **Intensité** : Réglez sur **Maximum** (Important!)
- Cliquez sur **"Enregistrer"** / **"Save"**

## ✅ Vérification

1. Lancez **Haptic Master** (`.\test.bat` ou `python haptic_master.py`)
2. Cliquez sur le bouton **"Test Haptic"** dans l'interface
3. Votre souris devrait vibrer 3 fois rapidement (pattern "pulse")

## 🐛 Si ça ne fonctionne pas

### La souris ne vibre pas :
- ✅ Vérifiez que Logi Options+ est bien lancé
- ✅ Vérifiez que le raccourci est bien `Ctrl+Shift+Alt+U`
- ✅ Testez le raccourci manuellement (appuyez sur les 4 touches ensemble)
- ✅ Vérifiez que l'intensité haptique est au maximum
- ✅ Redémarrez Logi Options+ si nécessaire

### Le serveur ne démarre pas :
- ✅ Vérifiez que le port 26290 est libre
- ✅ Vérifiez les dépendances : `pip install -r requirements.txt`
- ✅ Lancez en administrateur si nécessaire

### L'application ne se lance pas :
- ✅ Vérifiez que Python 3.8+ est installé
- ✅ Installez les dépendances : `pip install keyboard`
- ✅ Vérifiez la console pour les messages d'erreur

## 📝 Notes Importantes

- **Conflit potentiel** : Le raccourci `Ctrl+Shift+Alt+U` peut entrer en conflit avec d'autres applications. Si c'est le cas, vous pouvez modifier le raccourci dans `haptic_master.py` (ligne 35, variable `TRIGGER_KEY`)

- **Performance** : Les haptiques fonctionnent mieux avec Logi Options+ en cours d'exécution. Si vous fermez Logi Options+, les haptiques ne fonctionneront plus.

- **Souris supportées** :
  - Logitech MX Master 3
  - Logitech MX Master 3S
  - Logitech MX Master 4
  
  (D'autres modèles MX peuvent fonctionner mais ne sont pas officiellement testés)

## 🎮 Patterns Disponibles

Quand vous testez depuis l'application, vous pouvez essayer différents patterns :
- **Single** : Une vibration simple
- **Double** : Deux vibrations courtes
- **Pulse** : Trois vibrations rapides (défaut)
- **Heartbeat** : Double battement
- **Triple** : Triple vibration espacée
- **Long** : Vibration continue (buzz)
- **SOS** : Pattern morse SOS
- **Engine Start** : Accélération progressive
- **Blaster** : Rafale rapide
- **Gallop** : Pattern galop

---

**Besoin d'aide ?** Consultez le [README_WINDOWS.md](README_WINDOWS.md) pour plus de détails.
