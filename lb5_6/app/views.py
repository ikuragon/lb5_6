from flask import Blueprint, request
from sqlalchemy.orm import Session

from app import db
from app.models import Employee, Position, Division, Job
from sqlalchemy.orm import sessionmaker

bp = Blueprint('bp', __name__)

# получение сотрудника
@bp.route('/employee/get', methods=['GET'])
def get_employee():
    employee_id = {
        "id": request.args.get('id')
    }
    emp = db.session.query(Employee).get(employee_id)
    print(emp.first_name, emp.second_name, emp.surname,
          emp.address, emp.date_of_birth)
    db.session.commit()
    return "check"

#получение должности
@bp.route('/position/get', methods=['GET'])
def get_position():
    position_id = {
        "id": request.args.get('id')
    }
    pos = db.session.query(Position).get(position_id)
    print(pos.position_name)
    db.session.commit()
    return "check"

# получение подразделения
@bp.route('/division/get', methods=['GET'])
def get_division():
    division_id = {
        "id": request.args.get('id')
    }
    div = db.session.query(Division).get(division_id)
    print(div.division_name)
    db.session.commit()
    return "check"

# получение списка устроенных (сортировка по дате)
@bp.route('/sort_job/get', methods=['GET'])
def get_sort_job():
    job_all = db.session.query(Job).order_by(Job.date_of_employment).all()
    for job in job_all:
        print(job, job.date_of_employment)
    db.session.commit()
    return "check"

# создание сотрудника
@bp.route('/employee/add', methods=['POST'])
def add_employee():
    employee_data = {
        "second_name": request.args.get('second_name'),
        "first_name": request.args.get("first_name"),
        "surname": request.args.get("surname"),
        "address": request.args.get("address"),
        "date_of_birth": request.args.get("date_of_birth")
    }
    new_employee = Employee(**employee_data)
    db.session.add(new_employee)
    db.session.commit()
    return "check"

#   создание должности
@bp.route('/position/add', methods=['POST'])
def add_position():
    position_data = {
        "position_name": request.args.get('position_name'),
    }
    new_position = Position(**position_data)
    db.session.add(new_position)
    db.session.commit()
    return "check"

# создание подразделения
@bp.route('/division/add', methods=['POST'])
def add_division():
    division_data = {
        "division_name": request.args.get('division_name'),
    }
    new_division = Division(**division_data)
    db.session.add(new_division)
    db.session.commit()
    return "check"

# удаление сотрудника
@bp.route('/employee/delete', methods=['DELETE'])
def delete_employee():
    employee_id = {
        "id": request.args.get('id')
    }
    emp = db.session.query(Employee).get(employee_id)
    del_emp = db.session.delete(emp)
    db.session.commit()
    return "check"

# удаление должности
@bp.route('/position/delete', methods=['DELETE'])
def delete_position():
    position_id = {
        "id": request.args.get('id')
    }
    pos = db.session.query(Position).get(position_id)
    del_pos = db.session.delete(pos)
    db.session.commit()
    return "check"

# удаление подразделения
@bp.route('/division/delete', methods=['DELETE'])
def delete_division():
    division_id = {
        "id": request.args.get('id')
    }
    div = db.session.query(Division).get(division_id)
    del_div = db.session.delete(div)
    db.session.commit()
    return "check"

# устройство сотрудника
@bp.route('/job/add', methods=['POST'])
def add_job():
    employee = Employee.query.get(5)
    position = Position.query.get(5)
    division = Division.query.get(7)
    job_add = {
        "employee_id": employee.id,
        "position_id": position.id,
        "division_id": division.id,
        "date_of_employment": request.args.get('date_of_employment'),
    }
    new_job_emp = Job(**job_add)
    db.session.add(new_job_emp)
    db.session.commit()
    return "check"

# редактирование сотрудника
@bp.route('/employee/put', methods=['PUT'])
def put_employee():
    emp = db.session.query(Employee).get(2)
    emp.second_name = request.args.get('second_name')
    emp.first_name = request.args.get('first_name')
    emp.surname = request.args.get('surname')
    emp.address = request.args.get('address')
    emp.date_of_birth = request.args.get('date_of_birth')
    db.session.add(emp)
    db.session.commit()
    return "check"

# увольнение с работы
@bp.route('/job/put', methods=['PUT'])
def put_job():
    job = Job.query.get(7)
    job.date_of_dismissal = request.args.get('date_of_dismissal')
    db.session.add(job)
    db.session.commit()
    return "check"