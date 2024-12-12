package com.example.order.service.application.controllers;

import com.example.order.service.application.enums.OrderStatus;
import com.example.order.service.application.models.OrderRequest;
import com.example.order.service.application.models.OrderResponse;
import com.example.order.service.application.services.OrderService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/v1/order")
public class OrderController {
    @Autowired
    private OrderService orderService;

    @PostMapping
    public ResponseEntity<OrderResponse> placeOrder(@RequestBody OrderRequest orderRequest) {
        OrderResponse orderResponse = orderService.placeOrder(orderRequest);
        return new ResponseEntity<>(orderResponse, HttpStatus.CREATED);
    }

    @PutMapping("/{orderId}")
    public ResponseEntity<OrderResponse> updateOrderStatus(@PathVariable("orderId") String orderId,
                                                           @RequestParam("orderStatus") OrderStatus orderStatus) {
        OrderResponse orderResponse = orderService.updateOrderStatus(orderId, orderStatus);
        return new ResponseEntity<>(orderResponse, HttpStatus.OK);
    }

    @GetMapping("{orderId}")
    public ResponseEntity<OrderResponse> getOrderById(@PathVariable("orderId") String orderId){
        OrderResponse orderResponse = orderService.getOrderById(orderId);
        return new ResponseEntity<>(orderResponse, HttpStatus.OK);
    }
}
