def run():
    try:
        import qrcode
    except ImportError:
        print("❌ qrcode non installé!")
        print("Installe avec: pip3 install \"qrcode[pil]\"")
        return
    
    couleurs = ["black", "white", "red", "green", "blue", "yellow", "cyan", "magenta"]
    
    while True:
        print("\n=== QR Code Generator ===")
        print("1. ASCII")
        print("2. Image (PNG)")
        choice = input("Choix (1 ou 2) >>> ")
        
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
            fill_color = input("Couleur du QR [défaut: black] >>> ") or "black"
            back_color = input("Couleur du fond [défaut: white] >>> ") or "white"
            
            img = qr.make_image(fill_color=fill_color, back_color=back_color)
            img.save("qrcode.png")
            print("✅ QR Code sauvegardé en qrcode.png")
        
        print()


if __name__ == "__main__":
    run()
