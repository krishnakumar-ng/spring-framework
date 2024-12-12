package com.example.springapplication.payment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class DependencyByField {

    @Autowired
    private IPayment paymentMode;

    public void getBillDetails() {
        System.out.println("Getting the payment details via " + this.paymentMode);
        this.paymentMode.makePayment();
        this.paymentMode.getPaymentDetails();

    }
}
