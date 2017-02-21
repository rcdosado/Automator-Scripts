import csv
from employees.factories import UserFactory, EmployeeFactory, CampusFactory, RankFactory, DepartmentFactory, UnitFactory
from employees.models import Unit, Department, Campus, Rank, Employee
from django.contrib.auth.models import User
from datetime import datetime, timedelta


with open(r'..\..\database\employees.csv','r') as csvfile:
	ereader = csv.DictReader(csvfile)
	#ctr = 0
	for row in ereader:
		#if ctr > 5:
		#	break
		#ctr = ctr+1
		# if no data, then go next
		if not row['NAME']:
			continue
		n = row['NAME'].split(',')
		campus = row['Campus'].strip()
		bdate = row['BDATE'].strip()
		college = row['COLLEGE'].strip()
		soa = row['SOA'].strip()
		dept = row['DEPT'].strip()
		pos = row['POSITION'].strip()
		_bdate = datetime.strptime(bdate,'%d-%b-%y').date()
		if _bdate > _bdate.today():
			_bdate = _bdate - timedelta(days=365*100)
		_unit = Unit.objects.get(name=college)
		_campus = None
		if _unit:
			_campus = Campus.objects.get(name=campus)
			_unit.campus=_campus
		_department = None
		if dept:
			_department = Department.objects.get(title=dept)
		_work_status = '0'
		if soa:
			for code in Employee.STATUS_CHOICES:
				if code[1]==soa: _work_status = code[0]
		_user = UserFactory(first_name=n[1].strip(),last_name=n[0].strip())
		emp=EmployeeFactory(user=_user)
		emp.birth_date = _bdate
		emp.unit = _unit
		emp.department=_department
		emp.work_status = _work_status
		print(emp)
		emp.save()