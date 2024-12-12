package com.example.springapplication;

import com.example.springapplication.model.Employee;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class FirstSpringApplication {
    public static void main(String[] args) {
        var context = new AnnotationConfigApplicationContext(SpringBeanConfiguration.class);

        System.out.println(context.getBean("firstName"));
        System.out.println(context.getBean("employeeNumber"));


//        System.out.println(context.getBean("employee")); //calling by bean name
        System.out.println(context.getBean("emp")); //calling by bean name
        System.out.println(context.getBean(Employee.class)); // calling a bean by its class name
        System.out.println(context.getBean("company"));
    }
}
