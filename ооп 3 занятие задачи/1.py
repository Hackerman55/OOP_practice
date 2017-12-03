class employee:
    zp = 0
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print('Имя: ', self.name)
        print('Зарплата: ', self.zp)

    def calculate_payroll(self):
        pass

class hourlyemployee(employee):
    def __init__(self, name, hour):
        super().__init__(name)
        self.hour = hour

    def calculate_payroll(self):
        super().calculate_payroll()
        self.zp = 20.8 * 8 * self.hour

class fixed_termemployee(employee):
    def __init__(self, name, month):
        super().__init__(name)
        self.month = month

    def calculate_payroll(self):
        super().calculate_payroll()
        self.zp = self.month
a = hourlyemployee('John', 10)
a.calculate_payroll()
a.print_info()
b = fixed_termemployee('Alex', 2000)
b.calculate_payroll()
b.print_info()