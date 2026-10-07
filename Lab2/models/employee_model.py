# models/employee_model.py

employees = [
  {"id": 1, "name": "Andi", "position": "Staff",
   "salary": 5000000},
  {"id": 2, "name": "Budi", "position": "Manager",
   "salary": 9000000},
  {"id": 3, "name": "Citra", "position": "VP",
    "salary": 12000000},
]
def update_employee(id, name, position, salary):
    for e in employees:
        if e["id"] == id:
            e["name"] = name
            e["position"] = position
            e["salary"] = salary
            return True
    return False


def delete_employee(id):
    for e in employees:
        if e["id"] == id:
            employees.remove(e)
            return True
    return False