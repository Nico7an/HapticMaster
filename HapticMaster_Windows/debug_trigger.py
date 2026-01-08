import keyboard
import time

print("="*60)
print("TEST DU DECLENCHEUR HAPTIQUE (Alt + F12)")
print("="*60)
print("Ce script va simuler le raccourci Alt+F12 toutes les 3 secondes.")
print("Assurez-vous que Logi Options+ est configuré et que l'action est active.")
print("Appuyez sur Ctrl+C pour arrêter.")
print("\nDébut du test dans 2 secondes...")
time.sleep(2)

try:
    count = 1
    while True:
        print(f"\n[{count}] Envoi de Alt+F12...", end="", flush=True)
        
        # Essai 1 : send standard
        keyboard.send('alt+f12')
        print(" Envoyé (méthode standard)")
        
        time.sleep(3)
        count += 1
        
        print(f"[{count}] Envoi de Alt+F12 (avec délai)...", end="", flush=True)
        # Essai 2 : press/release manuel avec délai
        keyboard.press('alt')
        time.sleep(0.05)
        keyboard.press('f12')
        time.sleep(0.1)
        keyboard.release('f12')
        time.sleep(0.05)
        keyboard.release('alt')
        print(" Envoyé (méthode lente)")
        
        time.sleep(3)
        count += 1
        
except KeyboardInterrupt:
    print("\nTest arrêté.")
