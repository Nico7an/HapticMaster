import keyboard
import time

print("="*60)
print("TEST DU DECLENCHEUR HAPTIQUE (Alt + K)")
print("="*60)
print("Ce script va simuler le raccourci Alt+k toutes les 3 secondes.")
print("Assurez-vous que Logi Options+ est configuré et que l'action est active.")
print("Appuyez sur Ctrl+C pour arrêter.")
print("\nDébut du test dans 2 secondes...")
time.sleep(2)

try:
    count = 1
    while True:
        print(f"\n[{count}] Envoi de Alt+k...", end="", flush=True)
        keyboard.send('alt+k')
        print("Envoyé (méthode standard)")
        time.sleep(3)
        count += 1
        
except KeyboardInterrupt:
    print("\nTest arrêté.")
