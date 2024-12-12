package com.example.spring_security.controllers;

import com.example.spring_security.entities.Role;
import com.example.spring_security.repositories.RoleRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/auth")
public class RoleController {

    @Autowired
    private RoleRepository roleRepository;

    @PostMapping("/add/roles")
    public ResponseEntity<Role> addRole(@RequestBody Role role){
        return new ResponseEntity<>(roleRepository.save(role), HttpStatus.CREATED);
    }

}
