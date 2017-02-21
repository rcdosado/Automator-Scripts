import csv
from employees.factories import UserFactory, EmployeeFactory, CampusFactory, RankFactory, DepartmentFactory, UnitFactory
from employees.models import Unit, Department, Campus, Rank
from datetime import datetime

with open(r'..\..\database\campuses.txt','r') as campusfile:
	campuses = campusfile.readlines()


for c in campuses:
	_campus = CampusFactory(name=c.strip())
	_campus.save()


with open(r'..\..\database\Ranks.txt','r') as ranksfile:
	ranks= ranksfile.readlines()

for r in ranks:
	_rank = RankFactory(name=r.strip())
	_rank.save()

with open(r'..\..\database\Departments.txt','r') as departmentfile:
	departments = departmentfile.readlines()

for d in departments:
	_department = DepartmentFactory(title=d.strip())
	_department.save()


with open(r'..\..\database\Units.txt','r') as unitfile:
	units = unitfile.readlines()

for u in units:
	line = u.split(',')
	_unit = UnitFactory(name=line[0].strip(), description=line[1].strip())
	_unit.save()
