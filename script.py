def run():
    try:
        import qrcode
    except ImportError:
        print("❌ qrcode non installé!")
        print("Installe avec: pip3 install \"qrcode[pil]\"")
        return
    
    while True:
        url = input("URL ou texte >>> ")
        
        if not url.strip():
            print("❌ Entrée vide!")
            continue
        
        if url.lower() == "exit":
            print("Au revoir !")
            break
        
        # Couleurs personnalisables
        fill_color = input("Couleur du QR (noir/bleu/rouge) [défaut: noir] >>> ") or "black"
        back_color = input("Couleur du fond (blanc/jaune/vert) [défaut: blanc] >>> ") or "white"
        
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4,
            fill_color=fill_color,  # Couleur du QR
            back_color=back_color   # Couleur du fond
        )
        qr.add_data(url)
        qr.make(fit=True)
        qr.print_ascii(invert=True)
        print()


if __name__ == "__main__":
    run()
