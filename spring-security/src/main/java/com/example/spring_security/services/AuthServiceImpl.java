package com.example.spring_security.services;

import com.example.spring_security.entities.Role;
import com.example.spring_security.entities.User;
import com.example.spring_security.models.Token;
import com.example.spring_security.models.UserRequest;
import com.example.spring_security.repositories.RoleRepository;
import com.example.spring_security.repositories.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.HashSet;
import java.util.Set;

@Service
public class AuthServiceImpl implements AuthService {
    @Autowired
    private AuthenticationManager authenticationManager;
    @Autowired
    private JwtService jwtService;
    @Autowired
    private UserRepository userRepository;
    @Autowired
    private RoleRepository roleRepository;
    @Autowired
    private PasswordEncoder passwordEncoder;


    @Override
    public ResponseEntity<String> register(UserRequest userRequest) {
        if (userRepository.findByUsername(userRequest.getUsername()).isPresent()) {
            return ResponseEntity.badRequest().body("Username already taken");
        }

        User newUser = new User();
        newUser.setUsername(userRequest.getUsername());

        String encodePassword = passwordEncoder.encode(userRequest.getPassword());
        newUser.setPassword(encodePassword);

        //convert role names to role entities and assign to user
        Set<Role> roles = new HashSet<>();

        for (String roleName : userRequest.getRoles()) {
            Role role = roleRepository.findByRoleName(roleName)
                    .orElseThrow(() -> new RuntimeException("Role not found" + roleName));
            roles.add(role);
        }
        newUser.setRoles(roles);
        userRepository.save(newUser);
        return ResponseEntity.ok("User Registered Successfully");
    }

    @Override
    public Token login(User user) {
        try {
            authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(user.getUsername(), user.getPassword()));
        } catch (AuthenticationException e) {
            throw new RuntimeException(e);
        }

        String tokenString = jwtService.generateToken(user.getUsername());
        return new Token(tokenString, jwtService.getExpirationTime(), "Bearer");
    }
}
