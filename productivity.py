class ProductivitySystem:

    def track(self, employees, hours):
        print("Tracing the employee")
        print("---------------------")

        for emplyee in employees:
            emplyee.work(hours)

        print("")

