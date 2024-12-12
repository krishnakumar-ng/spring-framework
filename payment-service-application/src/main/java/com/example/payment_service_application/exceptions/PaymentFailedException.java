package com.example.payment_service_application.exceptions;

public class PaymentFailedException extends RuntimeException{
    public PaymentFailedException(String message) {
        super(message);
    }
}
