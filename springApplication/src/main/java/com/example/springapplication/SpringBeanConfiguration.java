package com.example.springapplication;

import com.example.springapplication.model.Company;
import com.example.springapplication.model.Employee;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
public class SpringBeanConfiguration {

    @Bean
    public String firstName() { // firstName is the bean name
        return "Krishna";
    }

    @Bean
    public int employeeNumber() { // employeeNumber is the bean name
        return 10;
    }

    @Bean(name = "emp")
//    public Employee employee(@Qualifier("company") Company company) { // Qualifier Alternative to Primary
    public Employee employee( Company company) {
        return new Employee("Krishna", 10, company);
    }

    @Bean
    public Company company() {
        return new Company("Comcast", 127);
    }

    @Bean
//    @Primary  // To make the company2 bean as the primary when i call the company
    public Company company2() {
        return new Company("Cognizant",100);
    }
}


