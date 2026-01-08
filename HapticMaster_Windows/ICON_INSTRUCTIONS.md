# Instructions pour créer l'icône

Pour builder l'exécutable avec une icône, vous avez deux options :

## Option 1 : Utiliser une icône existante
1. Trouvez un fichier `.ico` (icône de souris par exemple)
2. Renommez-le en `icon.ico`
3. Placez-le dans ce dossier

## Option 2 : Builder sans icône
Modifiez `build.bat` en retirant `--icon=icon.ico` de la ligne PyInstaller.

## Option 3 : Créer une icône depuis une image
Si vous avez une image PNG/JPG :
```bash
pip install Pillow
python -c "from PIL import Image; img = Image.open('image.png'); img.save('icon.ico', format='ICO', sizes=[(256, 256)])"
```

Note : Le build fonctionnera même sans icône, l'exécutable utilisera simplement l'icône Python par défaut.
