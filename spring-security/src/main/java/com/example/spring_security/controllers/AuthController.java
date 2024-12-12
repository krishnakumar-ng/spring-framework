package com.example.spring_security.controllers;

import com.example.spring_security.entities.User;
import com.example.spring_security.models.UserRequest;
import com.example.spring_security.models.Token;
import com.example.spring_security.services.AuthService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class AuthController {
    @Autowired
    private AuthService authService;

    @PostMapping("/register")
    public ResponseEntity<String> register(@RequestBody UserRequest userRequest) {
        return authService.register(userRequest);
    }

    @PostMapping("/login")
    public ResponseEntity<Token> login(@RequestBody User user) {

        Token token = authService.login(user);
        return new ResponseEntity<>(token, HttpStatus.OK);

    }

}
