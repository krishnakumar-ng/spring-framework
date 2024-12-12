package com.example.springapplication.payment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class DependencyByConstructor {
    private IPayment iPayment;

    @Autowired
    public DependencyByConstructor(IPayment iPayment){
        this.iPayment = iPayment;
    }

    public void getBillDetails() {
        System.out.println("Getting the payment details via " + this.iPayment);
        this.iPayment.makePayment();
        this.iPayment.getPaymentDetails();

    }
}
