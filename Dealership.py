class Dealership:
    def __init__(self, revenue):
        self.employee_list = []
        self.car_list = []
        self.revenue = revenue

    def get_revenue():
        return self.revenue
    
    def sell_car(model_number, used, employee_who_sold):
        for x in self.car_list:
            if x.model == model_number:
                self.car_list.remove(x) 
            if x.used == used:
                x.value = value * 1/2
        for x in employee_list:
            if x.employee == employee_who_sold:
                x.cars_sold += 1

    def add_car(model_number, used):
        for x in self.car_list:
            if x.model == model_number:
                self.car_list.append(x)

    def get_cars():
        return self.car_list
    
    def in_stock(model_number, used):
        for x in self.car_list:
            if x.model == model_number:
                if x.used == used:
                    return true
        return false

    def add_employee(name, position):
        self.employee_list.append(name)

    def fire(name):
        for x in self.employee_list:
            if x.name == name
        self.employee_list.remove()
    

# note: code above is probably wrong   
