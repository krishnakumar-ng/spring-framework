package com.example.employee.service.application.services;

import com.example.employee.service.application.model.Employee;
import com.example.employee.service.application.exceptions.EmployeeNotFoundException;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class EmployeeServiceImpl implements EmployeeService {

    List<Employee> employees = new ArrayList<>();

    @Override
    public Employee addEmployee(Employee employee) {
        if (employee.getEmployeeId() == null)
            employee.setEmployeeId(UUID.randomUUID().toString());
        this.employees.add(employee);
        return employee;
    }

    @Override
    public List<Employee> getAllEmployees() {
        return this.employees;
    }

    @Override
    public Employee getEmployeeUsingId(String employeeId) {
        return this.employees
                .stream()
                .filter(employee -> employee.getEmployeeId().equals(employeeId))
                .findFirst()
                .orElseThrow(() -> new EmployeeNotFoundException("Employee - " + employeeId + " is not exist"));
    }

    @Override
    public List<Employee> getEmployeeByName(String employeeName) {
        return List.of(this.employees
                .stream()
                .filter(employee -> employee.getEmployeeName().equals(employeeName))
                .findFirst()
                .orElseThrow(() -> new EmployeeNotFoundException("Employee - " + employeeName + " is not exist")));
    }

    @Override
    public String deleteEmployeeById(String employeeId) {
        Optional<Employee> employee = this.employees
                .stream()
                .filter(emp -> emp.getEmployeeId().equals(employeeId))
                .findFirst();

        if(employee.isPresent()) {
            this.employees.remove(employee.get());
            return employeeId + " deleted successfully";
        }else{
            return employeeId + " is not exists";
        }
    }
}
