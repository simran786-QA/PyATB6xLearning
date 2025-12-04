# -------------------------------------------------------------
# Author: Simran Shaikh
# Topic: Static Methods & Utility Classes in Test Automation
# -------------------------------------------------------------

# -------------------------------------------------------------
# Step 1: Create Excel Reader Utility
# Static method → No object needed
# -------------------------------------------------------------
class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")


# -------------------------------------------------------------
# Step 2: Create MySQL DB Reader Utility
# Static method → No object needed
# -------------------------------------------------------------
class MYSQLDBConnection:

    @staticmethod
    def readMySQLFile():
        print("Reading from MySQL")


# -------------------------------------------------------------
# Step 3: Create Test Case Classes (TC1, TC2)
# They reuse the same utility static methods
# -------------------------------------------------------------
class TC1:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("TC1 Executed")


class TC2:

    def runTC(self):
        ExcelReader.readExcelFile()
        MYSQLDBConnection.readMySQLFile()
        print("TC2 Executed")


# -------------------------------------------------------------
# Step 4: Execute Test Cases
# -------------------------------------------------------------
tc1 = TC1()
tc2 = TC2()

tc1.runTC()
tc2.runTC()

# -------------------------------------------------------------
# Hindi Explanation:
# - ExcelReader aur MYSQLDBConnection dono static utility classes hain.
# - Inke methods ko call karne ke liye object banane ki zaroorat nahi.
# - Har test case (TC1, TC2) in static methods ko reuse kar sakta hai.
#
# English Explanation:
# - ExcelReader and MYSQLDBConnection are static utility classes.
# - Their methods don’t require object creation.
# - Every test case class (TC1, TC2) can reuse these utilities easily.
# -------------------------------------------------------------

# -------------------------------------------------------------
# Summary:
# 1. Static utility classes help avoid duplicate code.
# 2. No object needed for static methods → call directly with class name.
# 3. Test cases become cleaner and easier to maintain.
# -------------------------------------------------------------
