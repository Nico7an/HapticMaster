"""
Haptic Master for Windows
Immersive Haptic Feedback for Logitech MX Master Users
"""

import sys
import tkinter as tk
from tkinter import ttk, messagebox
import threading
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
import time
from datetime import datetime

# Vérification des dépendances
try:
    import keyboard
    import pystray
    from PIL import Image, ImageDraw
except ImportError as e:
    missing = str(e).split("'")[1] if "'" in str(e) else "unknown"
    print("\n" + "="*60)
    print(f"ERREUR : Module '{missing}' manquant")
    print("="*60)
    print("\nVeuillez installer les dépendances :")
    print("  pip install -r requirements.txt")
    print("\nOu installez manuellement :")
    print("  pip install keyboard pystray Pillow")
    print("\n" + "="*60)
    input("\nAppuyez sur Entrée pour quitter...")
    sys.exit(1)


class HapticEngine:
    """Gère les patterns haptiques via Logi Options+"""
    
    # Raccourci clavier configuré dans Logi Options+ : Ctrl+Shift+Alt+U
    TRIGGER_KEY = 'ctrl+shift+alt+u'
    
    PATTERNS = {
        'single': 'Single',
        'double': 'Double',
        'pulse': 'Pulse',
        'heartbeat': 'Heartbeat',
        'triple': 'Triple',
        'long': 'Long',
        'sos': 'SOS',
        'engine_start': 'Engine Start',
        'blaster': 'Blaster',
        'gallop': 'Gallop'
    }
    
    @staticmethod
    def trigger():
        """Déclenche un retour haptique via le raccourci clavier"""
        try:
            # Envoi rapide direct
            keyboard.send('ctrl+shift+alt+u')
        except Exception as e:
            print(f"Erreur trigger: {e}")
    
    @staticmethod
    def play_pattern(pattern: str):
        """Joue un pattern haptique"""
        # print(f"Playing pattern: {pattern}") # Optimisation: supprimer print
        
        # OPTIMISATION: Exécution synchrone immédiate pour 'single'
        if pattern == 'single' or not pattern:
            HapticEngine.trigger()
            return
        
        def _execute():
            if pattern == 'double':
                HapticEngine.trigger()
                time.sleep(0.15)
                HapticEngine.trigger()
                
            elif pattern == 'pulse':
                HapticEngine.trigger()
                time.sleep(0.075)
                HapticEngine.trigger()
                time.sleep(0.075)
                HapticEngine.trigger()
                
            elif pattern == 'heartbeat':
                HapticEngine.trigger()
                time.sleep(0.12)
                HapticEngine.trigger()
                
            elif pattern == 'triple':
                HapticEngine.trigger()
                time.sleep(0.25)
                HapticEngine.trigger()
                time.sleep(0.25)
                HapticEngine.trigger()
                
            elif pattern == 'gallop':
                HapticEngine.trigger()
                time.sleep(0.08)
                HapticEngine.trigger()
                time.sleep(0.2)
                HapticEngine.trigger()
                
            elif pattern == 'long':
                for _ in range(15):
                    HapticEngine.trigger()
                    time.sleep(0.03)
                    
            elif pattern == 'sos':
                # ... --- ...
                for _ in range(3):
                    HapticEngine.trigger()
                    time.sleep(0.1)
                time.sleep(0.2)
                for _ in range(3):
                    HapticEngine.trigger()
                    time.sleep(0.3)
                time.sleep(0.2)
                for _ in range(3):
                    HapticEngine.trigger()
                    time.sleep(0.1)
                    
            elif pattern == 'engine_start':
                delays = [0.2, 0.15, 0.1, 0.08, 0.06, 0.05]
                for delay in delays:
                    HapticEngine.trigger()
                    time.sleep(delay)
                HapticEngine.trigger()
                
            elif pattern == 'blaster':
                for _ in range(6):
                    HapticEngine.trigger()
                    time.sleep(0.04)
                    
            # else:  # single traité en synchrone plus haut
        
        # Exécuter dans un thread séparé pour ne pas bloquer l'UI (pour les patterns complexes)
        threading.Thread(target=_execute, daemon=True).start()


from socketserver import ThreadingMixIn

class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    """Serveur HTTP multi-thread"""
    pass

class WebServerHandler(BaseHTTPRequestHandler):
    """Gestionnaire des requêtes HTTP depuis l'extension navigateur"""
    
    protocol_version = "HTTP/1.1"  # Enable Keep-Alive
    last_trigger_time = 0
    
    def log_message(self, format, *args):
        """Réduit le logging"""
        pass
    
    def do_GET(self):
        """Traite les requêtes GET (check de connexion)"""
        try:
            # Réponse simple pour vérifier que le serveur est en ligne
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Length', str(len(b'Haptic Master Server Running')))
            self.end_headers()
            self.wfile.write(b'Haptic Master Server Running')
        except Exception as e:
            print(f"Erreur GET: {e}")
            self.send_error(500, str(e))
    
    def do_POST(self):
        """Traite les requêtes POST de l'extension"""
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            # Anti-rebond côté serveur (Debounce)
            current_time = time.time() * 1000  # ms
            # Réduit à 30ms pour plus de réactivité (évite le spam mais permet le rapide)
            if current_time - WebServerHandler.last_trigger_time < 30: 
                # Ignorer les requêtes trop rapprochées
                msg = b'ignored-debounce'
                self.send_response(200)
                self.send_header('Access-Control-Allow-Origin', '*')
                self.send_header('Content-Length', str(len(msg)))
                self.end_headers()
                self.wfile.write(msg)
                return
            
            WebServerHandler.last_trigger_time = current_time
            
            # Parse JSON
            data = json.loads(body)
            pattern = data.get('pattern', 'single')
            
            # Joue le pattern si les haptiques web sont activées
            if hasattr(self.server, 'app') and self.server.app.allow_web_haptics.get():
                HapticEngine.play_pattern(pattern)
                # Met à jour l'UI
                if hasattr(self.server, 'app'):
                    self.server.app.update_last_signal()
            
            # Réponse
            msg = b'ok'
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Content-Length', str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)
            
        except Exception as e:
            print(f"Erreur POST: {e}")
            self.send_error(500, str(e))
    
    def do_OPTIONS(self):
        """Gère les requêtes CORS preflight"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Length', '0')
        self.end_headers()


class HapticMasterApp:
    """Application principale avec interface graphique"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Haptic Master")
        self.root.geometry("340x480")
        self.root.resizable(False, False)
        
        # Configuration
        self.system_notifications_enabled = tk.BooleanVar(value=True)
        self.notification_pattern = tk.StringVar(value='pulse')
        self.allow_web_haptics = tk.BooleanVar(value=True)
        
        # État du serveur
        self.server_status = tk.StringVar(value="Initializing...")
        self.is_connected = tk.BooleanVar(value=False)
        self.last_signal = tk.StringVar(value="")
        
        # Serveur Web
        self.server = None
        self.server_thread = None
        
        # System Tray
        self.tray_icon = None
        self.tray_thread = None
        
        self._create_ui()
        self._setup_tray()
        self._start_server()
        
        # Démarrer caché dans le tray (pas de fenêtre ni popup)
        self.root.withdraw()
        
        # Ne pas afficher le message d'aide automatiquement
        # L'utilisateur peut l'afficher manuellement via le menu si besoin
    
    def _create_tray_icon(self):
        """Crée une icône simple pour le system tray"""
        # Créer une image 64x64 avec un cercle (représentant une souris)
        image = Image.new('RGB', (64, 64), color='white')
        draw = ImageDraw.Draw(image)
        
        # Dessiner un cercle bleu (souris)
        draw.ellipse([8, 8, 56, 56], fill='#2196F3', outline='#1976D2', width=3)
        # Petit cercle blanc au centre (bouton de souris)
        draw.ellipse([26, 26, 38, 38], fill='white')
        
        return image
    
    def _setup_tray(self):
        """Configure l'icône du system tray"""
        def show_window(icon=None, item=None):
            """Affiche la fenêtre principale"""
            self.root.after(0, self._show_window)
        
        def hide_window(icon=None, item=None):
            """Cache la fenêtre principale"""
            self.root.after(0, self._hide_window)
        
        def show_help(icon=None, item=None):
            """Affiche l'aide de configuration"""
            self.root.after(0, self._show_setup_help)
        
        def quit_app(icon=None, item=None):
            """Quitte l'application"""
            self.root.after(0, self.on_close)
        
        # Menu du tray
        menu = pystray.Menu(
            pystray.MenuItem("Afficher", show_window, default=True),
            pystray.MenuItem("Masquer", hide_window),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Test Haptic", lambda: HapticEngine.play_pattern('pulse')),
            pystray.MenuItem("Aide", show_help),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Quitter", quit_app)
        )
        
        # Créer l'icône du tray
        icon_image = self._create_tray_icon()
        self.tray_icon = pystray.Icon(
            "HapticMaster",
            icon_image,
            "Haptic Master",
            menu
        )
        
        # Lancer le tray dans un thread séparé
        def run_tray():
            self.tray_icon.run()
        
        self.tray_thread = threading.Thread(target=run_tray, daemon=True)
        self.tray_thread.start()
        
        # Gérer la fermeture de la fenêtre (minimiser dans le tray au lieu de quitter)
        self.root.protocol("WM_DELETE_WINDOW", self._hide_window)
    
    def _show_window(self):
        """Affiche la fenêtre principale"""
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
    
    def _hide_window(self):
        """Cache la fenêtre dans le system tray"""
        self.root.withdraw()
    
    def _show_setup_help(self):
        """Affiche les instructions de configuration"""
        msg = """IMPORTANT : Configuration Logi Options+

Pour que les haptiques fonctionnent, vous devez configurer
une Smart Action dans Logi Options+ :

1. Ouvrir Logi Options+
2. Aller dans Smart Actions → Créer une Smart Action
3. Déclencheur : Raccourci clavier
   Ctrl + Shift + Alt + U
4. Action : Haptic Feedback (Intensité Max)

Cliquez sur "Test Haptic" pour vérifier le fonctionnement.
Si ça ne vibre pas, vérifiez votre configuration."""
        
        # Afficher le message directement (accessible via menu Aide)
        messagebox.showinfo("Configuration Logi Options+", msg, parent=self.root)
    
    
    def _create_ui(self):
        """Crée l'interface graphique"""
        
        # Style
        style = ttk.Style()
        style.theme_use('vista')
        
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Header
        header = ttk.Frame(main_frame)
        header.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header, text="🖱 Haptic Master", 
                 font=('Segoe UI', 16, 'bold')).pack(anchor=tk.W)
        
        # Section 1: System Notifications
        notif_frame = ttk.LabelFrame(main_frame, text="  🔔 System Notifications  ", padding="10")
        notif_frame.pack(fill=tk.X, pady=(0, 15))
        
        toggle_frame = ttk.Frame(notif_frame)
        toggle_frame.pack(fill=tk.X)
        
        ttk.Checkbutton(toggle_frame, text="Enable", 
                       variable=self.system_notifications_enabled).pack(side=tk.LEFT)
        
        pattern_frame = ttk.Frame(notif_frame)
        pattern_frame.pack(fill=tk.X, pady=(10, 0))
        
        ttk.Label(pattern_frame, text="Vibration Type:").pack(side=tk.LEFT)
        
        pattern_combo = ttk.Combobox(pattern_frame, 
                                     textvariable=self.notification_pattern,
                                     values=list(HapticEngine.PATTERNS.values()),
                                     state='readonly',
                                     width=15)
        pattern_combo.pack(side=tk.RIGHT)
        pattern_combo.set(HapticEngine.PATTERNS[self.notification_pattern.get()])
        
        # Bind pour tester le pattern à la sélection
        def on_pattern_change(event):
            selected_name = self.notification_pattern.get()
            # Trouve la clé correspondante
            for key, name in HapticEngine.PATTERNS.items():
                if name == selected_name:
                    HapticEngine.play_pattern(key)
                    break
        
        pattern_combo.bind('<<ComboboxSelected>>', on_pattern_change)
        
        # Section 2: Web Browser
        web_frame = ttk.LabelFrame(main_frame, text="  🌐 Web Browser  ", padding="10")
        web_frame.pack(fill=tk.X, pady=(0, 15))
        
        ttk.Checkbutton(web_frame, text="Enable Web Haptics", 
                       variable=self.allow_web_haptics).pack(anchor=tk.W)
        
        # Status
        status_frame = ttk.Frame(web_frame)
        status_frame.pack(fill=tk.X, pady=(10, 0))
        
        self.status_indicator = tk.Canvas(status_frame, width=10, height=10, 
                                         highlightthickness=0)
        self.status_indicator.pack(side=tk.LEFT, padx=(0, 5))
        self.status_circle = self.status_indicator.create_oval(2, 2, 10, 10, fill='red')
        
        ttk.Label(status_frame, textvariable=self.server_status, 
                 font=('Segoe UI', 8)).pack(side=tk.LEFT)
        
        # Last signal
        signal_frame = ttk.Frame(web_frame)
        signal_frame.pack(fill=tk.X, pady=(5, 0))
        
        ttk.Label(signal_frame, textvariable=self.last_signal, 
                 font=('Segoe UI', 8), foreground='gray').pack(anchor=tk.W)
        
        # Info
        info_label = ttk.Label(web_frame, 
                              text="Customize patterns in your browser extension.",
                              font=('Segoe UI', 8),
                              foreground='gray')
        info_label.pack(pady=(10, 0))
        
        # Footer
        footer = ttk.Frame(main_frame)
        footer.pack(side=tk.BOTTOM, fill=tk.X, pady=(10, 0))
        
        ttk.Label(footer, text="Haptic Master for Windows", 
                 font=('Segoe UI', 8), foreground='gray').pack()
        
        # Bouton Test
        test_btn = ttk.Button(main_frame, text="Test Haptic", 
                             command=lambda: HapticEngine.play_pattern('pulse'))
        test_btn.pack(pady=10)
    
    def _start_server(self):
        """Démarre le serveur web sur le port 26290"""
        def run_server():
            try:
                self.server = ThreadingHTTPServer(('localhost', 26290), WebServerHandler)
                self.server.app = self  # Référence à l'app
                
                self.update_server_status("Listening on Port 26290", True)
                print("Server started on port 26290")
                
                self.server.serve_forever()
            except Exception as e:
                self.update_server_status(f"Error: {str(e)}", False)
                print(f"Server error: {e}")
        
        self.server_thread = threading.Thread(target=run_server, daemon=True)
        self.server_thread.start()
    
    def update_server_status(self, status: str, connected: bool):
        """Met à jour le statut du serveur (thread-safe)"""
        def _update():
            self.server_status.set(status)
            self.is_connected.set(connected)
            
            # Met à jour la couleur de l'indicateur
            color = 'green' if connected else 'red'
            self.status_indicator.itemconfig(self.status_circle, fill=color)
        
        # Exécuter dans le thread principal
        self.root.after(0, _update)
    
    def update_last_signal(self):
        """Met à jour l'heure du dernier signal (thread-safe)"""
        def _update():
            now = datetime.now().strftime("%H:%M:%S")
            self.last_signal.set(f"Last signal: {now}")
        
        # Exécuter dans le thread principal
        self.root.after(0, _update)
    
    def run(self):
        """Lance l'application"""
        # Le protocol WM_DELETE_WINDOW est déjà géré dans _setup_tray()
        self.root.mainloop()
    
    def on_close(self):
        """Ferme proprement l'application"""
        # Arrêter le serveur
        if self.server:
            self.server.shutdown()
        
        # Arrêter l'icône du tray
        if self.tray_icon:
            self.tray_icon.stop()
        
        # Fermer la fenêtre
        self.root.destroy()


if __name__ == '__main__':
    app = HapticMasterApp()
    app.run()
