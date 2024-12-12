package com.example.springapplication.payment;

import org.springframework.stereotype.Component;

@Component
public class CreditCardPayment implements IPayment{
    public void makePayment() {
        System.out.println("Payment via Credit card");
    }

    public void getPaymentDetails() {
        System.out.println("Sharing the details of  Credit Card Payment");
    }
}
