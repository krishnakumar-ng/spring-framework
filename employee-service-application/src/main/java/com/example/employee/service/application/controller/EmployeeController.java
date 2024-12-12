package com.example.employee.service.application.controller;

import com.example.employee.service.application.services.EmployeeService;
import com.example.employee.service.application.model.Employee;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.UUID;

@RestController
@RequestMapping("/v1/employee")
public class EmployeeController {

    @Qualifier("employeeServiceImpl")
    @Autowired
    private EmployeeService employeeService;

    @PostMapping
    public Employee addEmployee(@RequestBody Employee employee) {
        if(employee.getEmployeeId()==null)
            employee.setEmployeeId(UUID.randomUUID().toString());
        return this.employeeService.addEmployee(employee);
    }

    @GetMapping("/all")
    public List<Employee> getAllEmployees() {
        return this.employeeService.getAllEmployees();
    }

    @GetMapping
    public Employee getEmployeeById(@RequestParam("id") String employeeId) {
        return this.employeeService.getEmployeeUsingId(employeeId);
    }


    @DeleteMapping("/{id}")
    public String deleteEmployee(@PathVariable("id") String employeeId) {
        return this.employeeService.deleteEmployeeById(employeeId);
    }

}
