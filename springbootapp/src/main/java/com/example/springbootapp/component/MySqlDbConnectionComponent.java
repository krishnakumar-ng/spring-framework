package com.example.springbootapp.component;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Component
@Profile("qa")
public class MySqlDbConnectionComponent implements DbConnection {
    @Override
    public String dbOperation() {
        return "MySQL from qa";
    }
}
