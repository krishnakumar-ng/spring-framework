package com.example.springapplication.payment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class DependencyByMethod {
    private IPayment iPayment;

    @Autowired
    public void setIPayment(IPayment iPayment){
        this.iPayment = iPayment;
    }

    public void getBillDetails() {
        System.out.println("Getting the payment details via " + this.iPayment);
        this.iPayment.makePayment();
        this.iPayment.getPaymentDetails();

    }
}
