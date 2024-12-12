package com.example.order.service.application.exceptions;

public class OrderServiceException extends RuntimeException {
    public OrderServiceException(String message) {
        super(message);
    }
}
