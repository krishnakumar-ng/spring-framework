package com.example.employee.service.application.controller;

import com.example.employee.service.application.model.User;
import org.springframework.web.bind.annotation.*;

@RestController
public class HomeController {

    @GetMapping("/user")
    public User user(){
        User user = new User();
        user.setUserId(1);
        user.setUserName("Krishna");
        return user;
    }

    @RequestMapping(value = "/user/{id}/{name}", method = RequestMethod.GET)
    public String user(@PathVariable("id") Integer id, @PathVariable("name") String username){
        User user = new User();
        user.setUserId(id);
        user.setUserName(username);
        return "User name is : "+user.getUserName() + "user id is : "+ user.getUserId();
    }

    @GetMapping("/requestParams")
    public String queryParams(@RequestParam(name = "name") String username,
                            @RequestParam(name = "id", required = false, defaultValue = "100") Integer userId){
        return "User name is : "+username + "user id is : "+ userId;
    }


}
