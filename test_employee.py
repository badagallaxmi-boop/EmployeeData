from employee import employee_details

def test_employee_details_Laxmi():
    result = employee_details("Laxmi", 101, "IT", 45000)

    expected_emp = (
        "Employee Name: Laxmi\n"
        "Employee Id: 101\n"
        "Department: IT\n"
        "Salary: 45000"
    )

    assert result == expected_emp