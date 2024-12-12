package com.example.employee.service.application.services;

import com.example.employee.service.application.entities.EmployeeEntity;
import com.example.employee.service.application.exceptions.EmployeeNotFoundException;
import com.example.employee.service.application.model.Employee;
import com.example.employee.service.application.repositories.EmployeeRepository;
import com.example.employee.service.application.utils.Util;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@Service
public class EmployeeServiceV2Impl implements EmployeeService {

    @Autowired
    private EmployeeRepository employeeRepository;

    @Override
    public Employee addEmployee(Employee employee) {
        if (employee.getEmployeeId() == null)
            employee.setEmployeeId(UUID.randomUUID().toString());

        employeeRepository.save(Util.convertModelToEntity(employee));
        return employee;
    }

    @Override
    public List<Employee> getAllEmployees() {

        Page<EmployeeEntity> employeeEntityPage = employeeRepository.findAll(Pageable.ofSize(2));
        System.out.println("page: "+employeeEntityPage);

        return Util.convertEntitiesToModels(employeeRepository.findAll());
    }

    @Override
    public Employee getEmployeeUsingId(String employeeId) {
        Optional<EmployeeEntity> employeeEntity = employeeRepository.findById(employeeId);
        if (employeeEntity.isPresent())
            return Util.convertEntityToModel(employeeEntity.get());
        else
            throw new EmployeeNotFoundException("Employee with id - " + employeeId + " is not exist.");
    }

    @Override
    public List<Employee> getEmployeeByName(String employeeName) {
        return Util.convertEntitiesToModels(employeeRepository.findByEmployeeName(employeeName));
    }

    @Override
    public String deleteEmployeeById(String employeeId) {
        Optional<EmployeeEntity> employeeEntity = employeeRepository.findById(employeeId);
        if (employeeEntity.isPresent()) {
            employeeRepository.delete(employeeEntity.get());
            return employeeId + " is deleted from the DB";
        }
        else {
            return "Employee with id - " + employeeId + " is not exist.";
        }
    }
}
