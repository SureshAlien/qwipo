import frappe
import json

@frappe.whitelist()
def getEmployeeList():
    "Get Employee Names. with and without filters"
    try:
        filters={}
        if frappe.request.data:
            data = json.loads(frappe.request.data)
            if data.get("no"):
                filters["no"] = data.get("no")
            if data.get("department_name"):
                filters["department_name"] = data.get("department_name")
        data = frappe.db.get_list('Employee Q',
            filters= filters,
            fields=['employee_name'],
            order_by='name asc'
        )
        return data
    except Exception:
        error = frappe.get_traceback()
        return error

@frappe.whitelist()
def getDepartmentList():
    "Get list of Department Names"
    try:
        filters={}
        data = frappe.db.get_list('Department Q',
            filters= filters,
            fields=['name'],
            order_by='name asc'
        )
        return data
    except Exception:
        error = frappe.get_traceback()
        return error

@frappe.whitelist()
def createEmployee(data):
    #  To create a new Employee
    try:
        employee = frappe.new_doc("Employee Q")
        employee.employee_name = data.get("employee_name")
        employee.no = data.get("no")
        employee.job = data.get("job")
        employee.mgr = data.get("mgr")
        employee.hire_date = data.get("hire_date")
        employee.salary = data.get("salary")
        employee.department_name = data.get("department_name")
        employee.department_no = data.get("department_no")
        employee.save(ignore_permissions=True)
        frappe.db.commit()
        return employee.name + " -Employee has been Created"
        
    except Exception:
        error = frappe.get_traceback()
        return error

@frappe.whitelist()
def createDepartment(data):
    #  To create a new Employee
    try:
        department = frappe.new_doc("Department Q")
        department.department_name = data.get("department_name")
        department.department_no = data.get("department_no")
        department.location = data.get("location")
        department.save(ignore_permissions=True)
        frappe.db.commit()
        return department.name + " -Department has been Created"
    except Exception:
        error = frappe.get_traceback()
        return error

@frappe.whitelist()
def deleteDepartment(data):
    "Delete a Department"
    if frappe.get_doc("Department Q", data.get("name")):
        filters={"name":data.get("name")}
        frappe.db.delete("Department Q", filters)
        return "Deleted"       
    else:
        return "Please give valid Department ID"

@frappe.whitelist()
def deleteEmployee(data):
    if frappe.get_doc("Employee Q", data.get("name")):
        filters={"name":data.get("name")}
        frappe.db.delete("Employee Q", filters)
        return "Deleted"       
    else:
        return "Please give valid Employee ID"