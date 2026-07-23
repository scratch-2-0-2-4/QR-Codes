import re

def run():
    try:
        import qrcode
    except ImportError:
        print("❌ qrcode non installé!")
        print("Installe avec: pip3 install \"qrcode[pil]\" (MacOS / Linux) ou pip install \"qrcode[pil]\" windows.")
        return
    
    couleurs = ["black", "white", "red", "green", "blue", "yellow", "cyan", "magenta"]
    
    while True:
        print(" QR Codes -- [v. 2.1.1]")
        print("Choisis :")
        print("1. ASCII")
        print("2. Image (PNG)")
        choice = input("Choix (1/2) >>> ")
        
        if choice not in ["1", "2"]:
            print("❌ Choix invalide!")
            continue
        
        url = input("URL ou texte >>> ")
        
        if not url.strip():
            print("❌ Entrée vide!")
            continue
        
        if url.lower() == "exit":
            print("Au revoir !")
            break
        
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(url)
        qr.make(fit=True)
        
        if choice == "1":
            # ASCII
            qr.print_ascii(invert=True)
        else:
            # Image PNG
            print(f"Couleurs disponibles: {', '.join(couleurs)}")
            
            while True:
                fill_color = input("Couleur du QR [défaut: black] >>> ") or "black"
                if fill_color in couleurs or fill_color.startswith("#"):
                    break
                print(f"❌ Couleur invalide! Choisis parmi: {', '.join(couleurs)}")
            
            while True:
                back_color = input("Couleur du fond [défaut: white] >>> ") or "white"
                if back_color in couleurs or back_color.startswith("#"):
                    break
                print(f"❌ Couleur invalide! Choisis parmi: {', '.join(couleurs)}")
            
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            
            # --- MODIFICATION ICI ---
            # 1. Remplace tous les caractères non valides pour un fichier par "_"
            safe_name = re.sub(r'[^\w\-.]', '_', url)
            
            # 2. Raccourcit le nom si l'URL est très longue (max 30 caractères)
            if len(safe_name) > 30:
                safe_name = safe_name[:30]
                
            filename = f"{safe_name}.png"
            # ------------------------
            
            img.save(filename)
            print(f"✅ QR Code sauvegardé en : {filename}")
        
        print()


if __name__ == "__main__":
    run()
