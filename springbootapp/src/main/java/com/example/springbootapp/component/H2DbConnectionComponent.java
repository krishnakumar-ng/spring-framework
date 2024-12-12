package com.example.springbootapp.component;

import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Component
@Profile("dev")
public class H2DbConnectionComponent implements DbConnection {
    @Override
    public String dbOperation() {
        return "H2 from dev";
    }
}
