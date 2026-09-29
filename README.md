# Employee Salary Calculator

A lightweight, zero-dependency Python utility for calculating employee payroll, allowances, deductions, and take-home pay.

Designed to be simple, readable, and ready to plug into CLI scripts, web services (FastAPI/Flask), or payroll pipelines.

---

## Features

- **Standard Earnings & Allowances**:
  - HRA calculation based on location (50% of Basic for Metro, 40% for Non-Metro).
  - Dearness Allowance (DA at 10% of Basic).
  - Fixed allowances (Conveyance, Medical).
  - Customizable bonuses and special allowances.
- **Common Statutory Deductions**:
  - Provident Fund (PF at 12% of Basic).
  - Professional Tax (standard fixed monthly amount).
  - Estimated TDS / Income Tax withholding based on percentage bracket.
  - Health Insurance / ESI and optional custom deductions.
- **Developer-Friendly Output**:
  - Returns a clean, standard Python `dict` that serializes directly to JSON.
  - Includes a built-in terminal payslip formatter with readable currency styling.
- **Zero Dependencies**: Uses only standard Python (Python 3.8+).

---

## Quick Start

### 1. Run the Demo

Execute the script directly to see an example payslip:

```bash
python salary_calculator.py
```

**Sample Output:**

```text
==============================================
 PAYSLIP: Jane Doe (ID: EMP-1001)
==============================================

[ EARNINGS ]
  Basic Salary        : $ 50,000.00
  HRA                 : $ 25,000.00
  DA                  : $  5,000.00
  CONVEYANCE          : $  1,600.00
  MEDICAL             : $  1,250.00
  BONUS               : $  2,500.00
  OTHER               : $  3,500.00
  ------------------------------------
  GROSS PAY           : $ 88,850.00

[ DEDUCTIONS ]
  Pf                  : $  6,000.00
  Tax Tds             : $  8,885.00
  Prof Tax            : $    200.00
  Insurance           : $    500.00
  ------------------------------------
  TOTAL DEDUCTIONS    : $ 15,585.00

----------------------------------------------
  NET TAKE-HOME (Mo.) : $ 73,265.00
  Annual In-Hand      : $879,180.00
  Annual CTC          : $1,066,200.00
==============================================
```

---

## Usage Example

Import the function into your project:

```python
from salary_calculator import calculate_salary, print_payslip

# Calculate monthly breakdown
payroll_data = calculate_salary(
    basic_salary=45000,
    is_metro=False,          # 40% HRA
    bonus=1500,              # Optional bonus
    tax_rate_percent=10.0,   # Estimated tax slab
    other_deductions=0.0
)

# Access calculated values directly
print(f"Net Take-Home: ${payroll_data['net_salary']}")
print(f"Annual CTC:    ${payroll_data['annual_ctc']}")

# Or render a pretty terminal payslip
print_payslip(name="Alex Smith", emp_id="EMP-204", data=payroll_data, currency="$")
```

---

## Output Data Structure

The `calculate_salary` function returns a dictionary with the following schema:

```json
{
  "basic": 50000.0,
  "allowances": {
    "hra": 25000.0,
    "da": 5000.0,
    "conveyance": 1600.0,
    "medical": 1250.0,
    "bonus": 2500.0,
    "other": 3500.0
  },
  "gross_salary": 88850.0,
  "deductions": {
    "pf": 6000.0,
    "tax_tds": 8885.0,
    "prof_tax": 200.0,
    "insurance": 500.0,
    "other": 0.0
  },
  "total_deductions": 15585.0,
  "net_salary": 73265.0,
  "annual_ctc": 1066200.0,
  "annual_take_home": 879180.0
}
```

---

## Formula Reference

$$\text{Gross Salary} = \text{Basic} + \text{HRA} + \text{DA} + \text{Conveyance} + \text{Medical} + \text{Bonus} + \text{Other Allowances}$$

$$\text{Total Deductions} = \text{PF} + \text{Income Tax (TDS)} + \text{Professional Tax} + \text{Insurance} + \text{Other Deductions}$$

$$\text{Net Salary (Take-Home)} = \text{Gross Salary} - \text{Total Deductions}$$

$$\text{Annual CTC} = \text{Gross Salary} \times 12$$

---

## License

MIT License. Feel free to use and modify for personal or commercial projects.
