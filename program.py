import hr

salary_employee = hr.SalaryEmployee(1, "Fariz", 1500)
hourly_employee = hr.HourlyEmployee(1, "Nizko", 40, 15)
commission_employee = hr.CommissionEmployee(4.5, "Dima", 820, 220)


payroll_system  = hr.PayrollSystem()
payroll_system.calculate_payroll(
    [
        salary_employee,
        hourly_employee,
        commission_employee

    ]

)


# Calculating Payroll
# --------------------
# Payroll for: 1 - Fariz
# -Chech Amount: 1500
# Payroll for: 1 - Nizko
# -Chech Amount: 600
# Payroll for: 4.5 - Dima
# -Chech Amount: 1040

# Process finished with exit code 0
