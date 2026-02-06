[13:03, 06/02/2026] hedayahkamis96: import sqlite3

def run_test():
    # 1. Setup temporary database in memory
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    
    # 2. Build the table using our schema logic
    cursor.execute('''CREATE TABLE Expenses (ID INTEGER PRIMARY KEY, Amount REAL)''')
    
    # 3. Insert a test expense
    cursor.execute("INSERT INTO Expenses (Amount) VALUES (15.50)")
    
    # 4. Check if the math works
    cursor.execute("SELECT SUM(Amount) FROM Expenses")
    total = cursor.fetchone()[0]
    
    if total == 15.50:
        print("✅ TEST PASSED: Database logic is solid!")
    else:
        raise ValueError(f"❌ TEST FAILED: Expected 15.50 but got {total}")

if _name_ == "_main_":
    run_test()
[13:09, 06/02/2026] hedayahkamis96: 
