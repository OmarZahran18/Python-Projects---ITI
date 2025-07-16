class person:
    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "Happy"
        elif hours < 7:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthrate = "100%"
        elif meals == 2:
            self.healthrate = "75%"
        elif meals == 1:
            self.healthrate = "50%"

    def buy(self, items):
        self.money -= items * 10


class car:
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.velocity = velocity

    def run(self, distance, velocity):
        self.fuelRate -= distance * 0.1
        self.velocity = velocity
        if self.fuelRate <= 0:
            self.fuelRate = 0
        self.stop()

    def stop(self):
        self.velocity = 0
        print(f"{self.name} has stopped")


class employee(person):
    def __init__(self, name, money, mood, healthrate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, healthrate)
        self.id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "Happy"
        elif hours > 8:
            self.mood = "Tired"
        else:
            self.mood = "Lazy"

    def drive(self, distance, velocity):
        self.distance = distance
        if velocity == 0:
            print("🚫 Error: Cannot drive with 0 velocity.")
            return
        time = distance / velocity
        print(f"You Will Arrive in {time} Hours")
        self.car.run(distance, velocity)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        if self.car.fuelRate > 100:
            self.car.fuelRate = 100
        print("Car Refueled")


class office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)
        office.employeesNum += 1

    def fire(self, emp_id):
        emp = self.get_employee(emp_id)
        if emp:
            self.employees.remove(emp)
            office.employeesNum -= 1
            print(f"{emp.name} has been fired")
        else:
            print("No employee found")

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary = max(0, emp.salary - deduction)
            print(f"Deducted {deduction} from {emp.name}'s salary")
        else:
            print(f"Employee ID {emp_id} Not Found")

    def reward(self, emp_id, reward):
        emp = self.get_employee(emp_id)
        if emp:
            emp.salary += reward
            print(f"Rewarded {emp.name} with {reward}")
        else:
            print(f"Employee ID {emp_id} Not Found")

    def check_lateness(self, emp_id, moveHour):
        emp = self.get_employee(emp_id)
        if emp:
            targetHour = 9
            is_late = office.calculate_lateness(
                targetHour,
                moveHour,
                emp.distance_to_work,
                emp.car.velocity
            )
            if is_late:
                self.deduct(emp_id, 10)
                print(f"{emp.name} is late. Deducted.")
            else:
                self.reward(emp_id, 10)
                print(f"{emp.name} is on time. Rewarded.")
        else:
            print("Employee not found.")

    @staticmethod
    def calculate_lateness(targetHour, moveHour, distance, velocity):
        if velocity == 0:
            print("Can't calculate lateness — car velocity is 0.")
            return True
        arrival_time = moveHour + (distance / velocity)
        return arrival_time > targetHour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNum = num


#------- Testing on Samy  

# >>>>> Car
samy_car = car(name="Fiat 128", fuelRate=100, velocity=60)

# >>>>> Employee
samy = employee(
    name="Samy",
    money=7000,
    mood="Neutral",
    healthrate="70%",
    emp_id=1,
    car=samy_car,
    email="Samy645@iti.com",
    salary=9000,
    distance_to_work=30
)

# >>>>> Office
iti_office = office(name="ITI Smart Village")
iti_office.hire(samy)

# >>>>> Samy's Actions
samy.sleep(6)
samy.eat(2)
samy.buy(3)
samy.work(8)
samy.drive(30, 70)     
samy.refuel(35)

iti_office.check_lateness(emp_id=1, moveHour=7)

# >>>>> Samy Info :-
print("\n----- Samy Info After Actions -----")
print(f"Name: {samy.name}")
print(f"Money: {samy.money} L.E")
print(f"Mood: {samy.mood}")
print(f"Health Rate: {samy.healthrate}")
print(f"Salary: {samy.salary} L.E")
print(f"Email: {samy.email}")
print(f"Car Fuel: {samy.car.fuelRate}%")
print(f"Car Velocity: {samy.car.velocity} km/h")
print(f"Distance To Work: {samy.distance_to_work} km")
