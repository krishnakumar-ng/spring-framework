package com.example.spring_security.services;

import com.example.spring_security.entities.User;
import com.example.spring_security.models.UserRequest;
import com.example.spring_security.models.Token;
import org.springframework.http.ResponseEntity;

public interface AuthService {
    ResponseEntity<String> register(UserRequest userRequest);

    Token login(User user);
}
