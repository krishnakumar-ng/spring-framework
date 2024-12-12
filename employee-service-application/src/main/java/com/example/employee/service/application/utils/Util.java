package com.example.employee.service.application.utils;

import com.example.employee.service.application.entities.EmployeeEntity;
import com.example.employee.service.application.model.Employee;
import org.springframework.beans.BeanUtils;

import java.util.List;

public class Util {

    public static EmployeeEntity convertModelToEntity(Employee employee) {
        EmployeeEntity employeeEntity = new EmployeeEntity();
        BeanUtils.copyProperties(employee, employeeEntity);
        return employeeEntity;
    }

    public static Employee convertEntityToModel(EmployeeEntity employeeEntity) {
        Employee employee = new Employee();
        BeanUtils.copyProperties(employeeEntity, employee);
        return employee;
    }

    public static List<Employee> convertEntitiesToModels(List<EmployeeEntity> employeeEntities) {
        return employeeEntities.stream()
                .map(employeeEntity -> {
                    Employee employee = new Employee();
                    BeanUtils.copyProperties(employeeEntity, employee);
                    return employee;
                }).toList();
    }
}
