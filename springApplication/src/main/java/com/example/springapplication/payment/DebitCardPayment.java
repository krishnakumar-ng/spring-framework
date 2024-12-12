package com.example.springapplication.payment;

import org.springframework.context.annotation.Primary;
import org.springframework.stereotype.Component;

@Component
@Primary
public class DebitCardPayment implements IPayment{
    public void makePayment() {
        System.out.println("Payment via Debit card");
    }

    public void getPaymentDetails() {
        System.out.println("Sharing the details of Debit Card Payment");
    }
}
