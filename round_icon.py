from PIL import Image, ImageDraw

def add_rounded_corners(input_path, output_path, radius=30):
    """Ajoute des bords arrondis à une image"""
    # Ouvrir l'image
    img = Image.open(input_path).convert("RGBA")
    
    # Créer un masque avec des coins arrondis
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([(0, 0), img.size], radius, fill=255)
    
    # Appliquer le masque
    output = Image.new('RGBA', img.size, (0, 0, 0, 0))
    output.paste(img, (0, 0))
    output.putalpha(mask)
    
    # Sauvegarder
    output.save(output_path, 'PNG')
    print(f"✓ Icône arrondie créée : {output_path}")

# Traiter les icônes des extensions
add_rounded_corners(
    'C:/Users/nico7/.gemini/antigravity/brain/240ab048-f365-4623-afce-848d2784fd12/uploaded_image_1767878074425.png',
    'extension/icon.png',
    radius=30
)

add_rounded_corners(
    'C:/Users/nico7/.gemini/antigravity/brain/240ab048-f365-4623-afce-848d2784fd12/uploaded_image_1767878074425.png',
    'extension_firefox/icon.png',
    radius=30
)

print("\n✓ Toutes les icônes ont été mises à jour avec des bords arrondis !")
