def run():
    try:
        import qrcode
    except ImportError:
        print("❌ qrcode non installé!")
        print("Installe avec: pip install qrcode[pil]")
        return
    
    while True:
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
        qr.print_ascii(invert=True)
        print()


if __name__ == "__main__":
    run()
