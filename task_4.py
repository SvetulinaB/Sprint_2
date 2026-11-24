# 1. Создаем класс EmployeeSalary с переменной hourly_payment.
class EmployeeSalary:
    hourly_payment = 400
# 2. Инициализируем атрибуты через конструктор.
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
# 3. Добавили метод класса get_hours.
    @classmethod
    def get_hours(cls, name, hours, rest_days, email):
        if hours is None:
           hours = (7 - rest_days) * 8 
        
        return cls(name, hours, rest_days, email)
# 4. Добавили метод класса get_email.
    @classmethod
    def get_email(cls, name, hours, rest_days, email):
        if email is None:
            email = f"{name}@email.com"

        return cls(name, hours, rest_days, email)
# 5. Добавили метод класса set_hourly_payment.
    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment
# 6. Добавили метод расчета з/п.
    def salary(self):
        return self.hours * self.hourly_payment

#самопроверка (нет в задании)
# employee = EmployeeSalary('Маша', 40, 2, None)
# print(employee.salary())

# EmployeeSalary.set_hourly_payment(500)
# print(f"Зарплата после изменения ставки {employee.salary()}")