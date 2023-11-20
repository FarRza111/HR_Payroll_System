from abc import  ABC,abstractmethod


class PayrollSystem:

    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("--------------------")

        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"-Chech Amount: {employee.calculate_payroll()}")





        
