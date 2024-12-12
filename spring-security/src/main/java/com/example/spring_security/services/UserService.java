package com.example.spring_security.services;

import com.example.spring_security.models.UserRequest;

import java.util.List;

public interface UserService {
    List<UserRequest> getAllUsers();

    UserRequest getUserByName(String userName);
}
