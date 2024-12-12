package com.example.springbootapp.controller;

import com.example.springbootapp.component.DbConnection;
import com.example.springbootapp.component.HelloWorldComponent;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloWorldController {
    @Autowired
    private HelloWorldComponent helloWorldComponent;

    @Autowired
    private DbConnection dbConnection;

    @GetMapping("/db")
    public String dbOperation() {
        return dbConnection.dbOperation();
    }

    @GetMapping("/yaml")
    public String yaml() {
        return helloWorldComponent.sayGoodMorningYaml();
    }

    @GetMapping("/properties")
    public String properties() {
        return helloWorldComponent.sayGoodMorning();
    }

    @GetMapping
    public String sayGoodMorning(){
        return "Good Morning All";
    }
}
