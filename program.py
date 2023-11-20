import hr
import employees
import productivity

manager = employees.Manager(1, "Fariz", 1500)
secretary = employees.Secretary(1, "Nizko", 1200)
sales_guy = employees.SalesPerson(4.5, "Dima", 820, 220)
factory_worker = employees.FactoryWorker(4, "Jordan", 30, 18)

employees = [
    manager,
    secretary,
    sales_guy,
    factory_worker
    ]

productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)


# Calculating Payroll
# --------------------
# Payroll for: 1 - Fariz
# -Chech Amount: 1500
# Payroll for: 1 - Nizko
# -Chech Amount: 1200
# Payroll for: 4.5 - Dima
# -Chech Amount: 1040
# Payroll for: 4 - Jordan
# -Chech Amount: 540
