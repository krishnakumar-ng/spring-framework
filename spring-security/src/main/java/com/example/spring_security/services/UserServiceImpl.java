package com.example.spring_security.services;

import com.example.spring_security.entities.Role;
import com.example.spring_security.entities.User;
import com.example.spring_security.models.UserRequest;
import com.example.spring_security.repositories.UserRepository;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private JwtService jwtService;
    @Autowired
    private UserRepository userRepository;

    @Override
    public List<UserRequest> getAllUsers() {
        List<User> userList = userRepository.findAll();
        return userList.stream()
                .map(user -> new UserRequest(
                        user.getId(),
                        user.getUsername(),
                        user.getPassword(),
                        user.getRoles().stream().map(Role::getRoleName).collect(Collectors.toSet())
                ))
                .toList();
    }

    @Override
    public UserRequest getUserByName(String userName) {
        Optional<User> userOptional = userRepository.findByUsername(userName);
        if (userOptional.isPresent()) {
            User user = userOptional.get();
            return new UserRequest(
                    user.getId(),
                    user.getUsername(),
                    user.getPassword(),
                    user.getRoles().stream().map(Role::getRoleName).collect(Collectors.toSet())
            );
        } else {
            throw new UsernameNotFoundException("User don't exist");
        }

    }
}
