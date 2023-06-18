from flask import Blueprint, request

from app import db
from app.models import Employee, Position, Division, Job
from sqlalchemy.orm import sessionmaker

bp = Blueprint('bp', __name__)

# # получение сотрудника 
# @bp.route('/employee/get', methods=['GET'])
# def get_employee():
#     emp = Employee.query.get(request.args.get('id'))
#     return emp.to_dict()


# #получение должности
# @bp.route('/position/get', methods=['GET'])
# def get_position():
#     pos = Position.query.get(request.args.get('id'))
#     return pos.to_dict()


# # получение подразделения
# @bp.route('/division/get', methods=['GET'])
# def get_division():
#     div = Division.query.get(request.args.get('id'))
#     return div.to_dict()


# # создание сотрудника
# @bp.route('/employee/add', methods=['POST'])
# def add_employee():
#     new_employee = Employee(**request.args)
#     db.session.add(new_employee)
#     db.session.commit()
#     return new_employee.to_dict()


#   создание должности
# @bp.route('/position/add', methods=['POST'])
# def add_position():
#     new_position = Position(**request.args)
#     db.session.add(new_position)
#     db.session.commit()
#     return new_position.to_dict()


# # создание подразделения
# @bp.route('/division/add', methods=['POST'])
# def add_division():
#     new_division = Division(**request.args)
#     db.session.add(new_division)
#     db.session.commit()
#     return new_division.to_dict()


# удаление сотрудника
# @bp.route('/employee/delete', methods=['DELETE'])
# def delete_employee():
#     del_employee = Employee.query.get(request.args.get('id'))
#     db.session.delete(del_employee)
#     db.session.commit()
#     return del_employee.to_dict()


# удаление должности
# @bp.route('/position/delete', methods=['DELETE'])
# def delete_position():
#     del_position = Position.query.get(request.args.get('id'))
#     db.session.delete(del_position)
#     db.session.commit()
#     return del_position.to_dict()


# удаление подразделения
# @bp.route('/division/delete', methods=['DELETE'])
# def delete_division():
#     del_division = Division.query.get(request.args.get('id'))
#     db.session.delete(del_division)
#     db.session.commit()
#     return del_division.to_dict()


# устройство сотрудника
# @bp.route('/job/add', methods=['POST'])
# def add_job():
#     emp = Employee.query.get(request.args.get('employee_id'))
#     pos = Employee.query.get(request.args.get('position_id'))
#     div = Employee.query.get(request.args.get('division_id'))
#     job_add = {
#         "employee_id": emp.id,
#         "position_id": pos.id,
#         "division_id": div.id,
#         "date_of_employment": request.args.get('date_of_employment'),
#     }
#     new_job_emp = Job(**job_add)
#     db.session.add(new_job_emp)
#     db.session.commit()
#     return new_job_emp.to_dict()

# редактирование сотрудника
# @bp.route('/employee/put', methods=['PUT'])
# def put_employee():
#     emp = Employee.query.get(request.args.get('id'))
#     if request.args.get('second_name'):
#         emp.second_name = request.args.get('second_name')
#     if request.args.get('first_name'):
#         emp.first_name = request.args.get('first_name')
#     if request.args.get('surname'):
#         emp.surname = request.args.get('surname')
#     if request.args.get('address'):
#         emp.address = request.args.get('address')
#     if request.args.get('date_of_birth'):
#         emp.date_of_birth = request.args.get('date_of_birth')
#     db.session.add(emp)
#     db.session.commit()
#     return emp.to_dict()


# # увольнение с работы
# @bp.route('/job/put', methods=['PUT'])
# def put_job():
#     job = Job.query.get(request.args.get('id'))
#     job.date_of_dismissal = request.args.get('date_of_dismissal')
#     db.session.add(job)
#     db.session.commit()
#     return job.to_dict()


# получение списка устроенных
@bp.route('/sort_job', methods=['GET'])
def sort_list_get():
    #job_all = db.session.query(Job).order_by(Job.date_of_employment).all()
    job_all = Employee.query.join(Job).order_by(Job.date_of_employment)
    if request.args.get('division_id'):
        job_all = job_all.filter(Job.division_id == request.args.get('division_id'))
    elif request.args.get('sort_after_date'):
        job_all = job_all.filter(Job.date_of_employment > request.args.get('sort_after_date'))
    job_all = job_all.all()
    result = [job.to_dict() for job in job_all]
    return result


