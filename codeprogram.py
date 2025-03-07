def hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_keanggotaan):
    
    biaya = 10000
    
    
    if berat > 5:
        biaya += 5000
    
    
    if jarak > 10:
        biaya += 8000
    
    
    if jenis_pengiriman.lower() == "express":
        biaya += 20000
    
    
    if status_keanggotaan.lower() == "member":
        biaya *= 0.9  
    
    return int(biaya)

def main():
    
    berat = float(input("Masukkan berat paket (kg): "))
    jarak = float(input("Masukkan jarak pengiriman (km): "))
    jenis_pengiriman = input("Masukkan jenis pengiriman (biasa/express): ")
    status_keanggotaan = input("Apakah Anda member? (member/non-member): ")
    
    
    biaya_total = hitung_biaya_pengiriman(berat, jarak, jenis_pengiriman, status_keanggotaan)
    
    
    print(f"Total biaya pengiriman: Rp{biaya_total:,.0f}".replace(",", "."))

if __name__ == "__main__":
    main()
