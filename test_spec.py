"""
mini-budget V1 test senaryolari
Ogrenci: Deniz Yücel Uzunay (251478081)
Proje: mini-budget
"""
import subprocess
import os
import shutil

# --- Yardimci Fonksiyon ---
def run_cmd(args):
    """Komutu calistir, stdout dondur."""
    result = subprocess.run(
        ["python", "minibudget.py"] + args,
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def setup_function():
    """Her testten once temiz baslangic yap."""
    if os.path.exists(".minibudget"):
        shutil.rmtree(".minibudget")

# --- init testleri ---
def test_init_creates_directory():
    output = run_cmd(["init"])
    assert os.path.exists(".minibudget"), ".minibudget dizini olusturulmali"
    assert os.path.exists(".minibudget/transactions.dat"), "transactions.dat dosyasi olusturulmali"

def test_init_already_exists():
    run_cmd(["init"])
    output = run_cmd(["init"])
    assert "Already initialized" in output

# --- add testleri ---
def test_add_income():
    run_cmd(["init"])
    output = run_cmd(["add", "INCOME", "5000", "Salary"])
    assert "Added transaction #1" in output
    assert "INCOME" in output

def test_add_expense():
    run_cmd(["init"])
    run_cmd(["add", "INCOME", "5000", "Salary"])
    output = run_cmd(["add", "EXPENSE", "150", "Groceries"])
    assert "#2" in output
    assert "EXPENSE" in output

# YENİ GÖREV 2 TESTİ: Negatif Tutar Kontrolü
def test_add_negative_amount():
    run_cmd(["init"])
    output = run_cmd(["add", "EXPENSE", "-50", "Coffee"])
    assert "Error: Amount must be positive" in output, "Negatif deger girisine izin verilmemeli"

# --- list testleri (V1 ile calisir hale geldi) ---
def test_list_empty():
    run_cmd(["init"])
    output = run_cmd(["list"])
    assert "No transactions found" in output

def test_list_shows_transactions():
    run_cmd(["init"])
    run_cmd(["add", "INCOME", "5000", "Salary"])
    output = run_cmd(["list"])
    assert "Salary" in output
    assert "5000" in output

# --- balance testleri (Ileride implemente edilecek) ---
def test_balance_empty():
    run_cmd(["init"])
    output = run_cmd(["balance"])
    assert "will be implemented" in output

# --- delete testleri (Ileride implemente edilecek) ---
def test_delete_removes_transaction():
    run_cmd(["init"])
    run_cmd(["add", "EXPENSE", "50", "Coffee"])
    output = run_cmd(["delete", "1"])
    assert "will be implemented" in output

# --- hata testleri ---
def test_command_before_init():
    output = run_cmd(["add", "INCOME", "100", "Gift"])
    assert "Not initialized" in output

def test_unknown_command():
    run_cmd(["init"])
    output = run_cmd(["invest"])
    assert "Unknown command" in output

def test_missing_arguments():
    run_cmd(["init"])
    output = run_cmd(["add", "INCOME"])
    assert "Usage: python minibudget.py add" in output