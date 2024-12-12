package com.example.springbootapp.component;

import com.example.springbootapp.ConfigProperties;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;

@Component
public class HelloWorldComponent {
    @Value("${property.msg}")
    private String message;

    @Value("${custom.yaml.msg}")
    private String yamlMessage;

    @Autowired
    private ConfigProperties configProperties;

    public String sayGoodMorning() {
        return "Good Morning all\n" + message+"\n"+ configProperties.getName()+"-"+ configProperties.getTutor();
    }

    public String sayGoodMorningYaml() {
        return "Good Morning all\n" + yamlMessage;
    }
}
