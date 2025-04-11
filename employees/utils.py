def build_employee_tree(employee):
    return {
        "id": employee.id,
        "name": f"{employee.first_name} {employee.last_name}",
        "role": employee.role.title if employee.role else None,
        "photo_url": employee.contact_info.email if employee.contact_info else None,
        "children": [
            build_employee_tree(child) for child in employee.subordinates.all()
        ]
    }