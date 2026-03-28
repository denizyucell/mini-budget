"""
mini-budget V1 
Ogrenci: Deniz Yücel Uzunay (251478081)

--- V1 GÖREV LİSTESİ (TASKS) ---
1. Görev 1: `list` komutunu `while` döngüsü kullanarak implemente et (Dosyadan satır satır okuma).
2. Görev 2: SPEC dosyasına eklenen "Negatif tutar girilemez" kuralını `add` komutuna kod olarak ekle.
3. Görev 3: Projeye README.md dosyası ekleyerek V0 -> V1 farkını açıkla.
--------------------------------
"""
import sys
import os

def initialize():
    """minibudget dizini ve bos transactions.dat dosyasini olusturur."""
    if os.path.exists(".minibudget"):
        return "Already initialized"
    
    os.mkdir(".minibudget")
    f = open(".minibudget/transactions.dat", "w")
    f.close()
    return "Initialized empty minibudget in .minibudget/"

def add_transaction(t_type, amount, description):
    """Yeni gelir(INCOME) veya gider(EXPENSE) ekler."""
    if not os.path.exists(".minibudget"):
        return "Not initialized. Run: python minibudget.py init"
    
    # Görev 2: Negatif tutar kontrolü (SPEC dosyasına eklediğimiz kural)
    if int(amount) < 0:
        return "Error: Amount must be positive."
    
    f = open(".minibudget/transactions.dat", "r")
    content = f.read()
    f.close()
    
    transaction_id = content.count("\n") + 1
    
    f = open(".minibudget/transactions.dat", "a")
    record = str(transaction_id) + "|" + t_type + "|" + str(amount) + "|" + description + "|2026-03-16\n"
    f.write(record)
    f.close()
    
    return "Added transaction #" + str(transaction_id) + ": " + t_type + " " + str(amount)

def list_transactions():
    """
    Görev 1: Kaydedilen işlemleri liste ([] kullanmadan) while döngüsü ile satır satır okuyup yazdırır.
    """
    if not os.path.exists(".minibudget/transactions.dat"):
        return "Not initialized. Run: python minibudget.py init"
    
    f = open(".minibudget/transactions.dat", "r")
    
    # Dosya boş mu kontrolü
    first_char = f.read(1)
    if not first_char:
        f.close()
        return "No transactions found."
    
    # Okuma imlecini tekrar başa alıyoruz
    f.seek(0)
    
    result = ""
    line = f.readline() # İlk satırı oku
    
    # while döngüsü ile satır satır okuma işlemi
    while line != "":
        # Henüz listeler(split) öğrenilmediği için | işaretini boşlukla değiştirerek gösteriyoruz
        clean_line = line.replace("|", " - ")
        result = result + clean_line
        line = f.readline() # Sonraki satıra geç
        
    f.close()
    return result.strip()

def show_not_implemented(command_name):
    return "Command '" + command_name + "' will be implemented in future weeks."

# --- Ana Program ---
if len(sys.argv) < 2:
    print("Usage: python minibudget.py <command> [args]")
elif sys.argv[1] == "init":
    print(initialize())
elif sys.argv[1] == "add":
    if len(sys.argv) < 5:
        print("Usage: python minibudget.py add <TYPE> <amount> <description>")
    else:
        print(add_transaction(sys.argv[2], sys.argv[3], sys.argv[4]))
elif sys.argv[1] == "list":
    print(list_transactions())
elif sys.argv[1] == "balance":
    print(show_not_implemented("balance"))
elif sys.argv[1] == "delete":
    print(show_not_implemented("delete"))
else:
    print("Unknown command: " + sys.argv[1])