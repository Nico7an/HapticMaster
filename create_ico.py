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
    
    return output

# Créer l'icône pour l'exe Windows
print("Création de l'icône .ico pour Windows...")

# Charger et arrondir l'image
rounded_img = add_rounded_corners(
    'C:/Users/nico7/.gemini/antigravity/brain/240ab048-f365-4623-afce-848d2784fd12/uploaded_image_1767878074425.png',
    None,
    radius=50
)

# Redimensionner pour les différentes tailles d'icône Windows
sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
icons = []
for size in sizes:
    resized = rounded_img.resize(size, Image.Resampling.LANCZOS)
    icons.append(resized)

# Sauvegarder en .ico
rounded_img.save(
    'HapticMaster_Windows/icon.ico',
    format='ICO',
    sizes=sizes
)

print("✓ Icône icon.ico créée avec succès dans HapticMaster_Windows/")
print("  Tailles incluses:", sizes)
