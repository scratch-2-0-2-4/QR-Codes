def qr_code_generator():
    """Génère un code QR en ASCII"""
    print("\n=== QR CODE GENERATOR ===")
    
    try:
        import qrcode
    except ImportError:
        print("❌ qrcode non installé!")
        print("Installe avec: pip install qrcode[pil]")
        return
    
    url = input("URL ou texte: ")
    
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.print_ascii(invert=True)
    print()


if __name__ == "__main__":
    qr_code_generator()
