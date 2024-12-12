package com.example.employee.service.application.controller;

import com.example.employee.service.application.model.Employee;
import com.example.employee.service.application.services.EmployeeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/v2/employee")
public class EmployeeControllerV2 {

    @Qualifier("employeeServiceV2Impl")
    @Autowired
    private EmployeeService employeeService;

    @PostMapping
    public Employee addEmployee(@RequestBody Employee employee) {
        return this.employeeService.addEmployee(employee);
    }

    @GetMapping("/all")
    public List<Employee> getAllEmployees() {
        return this.employeeService.getAllEmployees();
    }

    @GetMapping("/{employeeId}")
    public Employee getEmployeeById(@PathVariable("employeeId") String employeeId) {
        return this.employeeService.getEmployeeUsingId(employeeId);
    }

    @GetMapping
    public List<Employee> getEmployeeByName(@RequestParam("employeeName") String employeeName) {
        return this.employeeService.getEmployeeByName(employeeName);
    }

    @DeleteMapping("/{id}")
    public String deleteEmployee(@PathVariable("id") String employeeId) {
        return this.employeeService.deleteEmployeeById(employeeId);
    }
}
