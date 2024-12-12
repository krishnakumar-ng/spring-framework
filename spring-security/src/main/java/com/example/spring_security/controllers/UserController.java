package com.example.spring_security.controllers;

import com.example.spring_security.models.UserRequest;
import com.example.spring_security.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService userService;

    @GetMapping("/{userName}")
    public ResponseEntity<UserRequest> getMyDetails(@RequestHeader("Authorization") String token,
                                                    @PathVariable("userName") String userName){
        UserRequest user = userService.getUserByName(userName);
        return new ResponseEntity<>(user,HttpStatus.OK);
    }

    @PreAuthorize("hasRole('ADMIN')")
    @GetMapping("/admin/all")
    public ResponseEntity<List<UserRequest>> getAllUsers(@RequestHeader("Authorization") String token) {
        List<UserRequest> userRequestList = userService.getAllUsers();
        return new ResponseEntity<>(userRequestList,HttpStatus.OK);
    }

    @GetMapping("/admin/one")
    public ResponseEntity<String> get(@RequestHeader("Authorization") String token) {

        return new ResponseEntity<>("ADMIN ONLY",HttpStatus.OK);
    }
}
