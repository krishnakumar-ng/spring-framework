package com.example.employee.service.application.services;

import com.example.employee.service.application.model.Employee;

import java.util.List;

public interface EmployeeService {
    Employee addEmployee(Employee employee);
    List<Employee> getAllEmployees();
    Employee getEmployeeUsingId(String employeeId);
    List<Employee> getEmployeeByName(String employeeName);
    String deleteEmployeeById(String employeeId);
}
