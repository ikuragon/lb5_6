from flask import Blueprint
from sqlalchemy.orm import Session

from app import db
from app.models import Employee, Position, Division, Job
from sqlalchemy.orm import sessionmaker

bp = Blueprint('bp', __name__)

@bp.route('/', methods=['GET'])
def index():

#   создание сотрудника
    employee_data = {
        "second_name": "Figurova",
        "first_name": "Elizaveta",
        "surname": "Alexandrovna",
        "address": "c.Arkh s.Urizkiy h.27 ",
        "date_of_birth": "16.08.1999",
    }
    new_employee = Employee(**employee_data)
    db.session.add(new_employee)

#   получение сотрудника
    employee = Employee.query.get(2)

#   удаление сотрудника
    db.session.delete(employee)

#   редактирование сотрудника
    employee_edit = Employee.query.get(2)
    employee_edit.surname = "Olegovna"
    db.session.add(employee_edit)




#   создание должности
    position_data = {
        "position_name": "Agent",
    }
    new_position = Position(**position_data)
    db.session.add(new_position)

#   получение сотрудника
    position = Position.query.get(1)

#   удаление сотрудника
    db.session.delete(position)


#   создание подразделения
    division_data = {
        "division_name": "3 department",
    }
    new_division = Division(**division_data)
    db.session.add(new_division)

#   получение подразделения
    division = Division.query.get(1)

#   удаление подразделения
    db.session.delete(division)

#   устройство на работу
    employee = Employee.query.get(3)
    position = Position.query.get(3)
    division = Division.query.get(3)

    job_data_employment = {
        "date_of_employment": "03.03.2001",
        "employee_id": employee.id,
        "position_id": position.id,
        "division_id": division.id
    }
    new_job_employment = Job(**job_data_employment)
    db.session.add(new_job_employment)

#   увольнение с работы
    job_dismissal = Job.query.get(1)
    job_dismissal.date_of_dismissal = "03.03.2003"
    db.session.add(job_dismissal)

#   получение списка устроенных (сортировка по дате)
    job_all = db.session.query(Job).order_by(Job.date_of_employment).all()
    for job in job_all:
        print(job, job.date_of_employment)

    db.session.commit()
    return "check"
