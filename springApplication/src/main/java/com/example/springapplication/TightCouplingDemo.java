package com.example.springapplication;

import com.example.springapplication.payment.CreditCardPayment;
import com.example.springapplication.payment.PaymentService;

public class TightCouplingDemo {

    public static void main(String[] args) {
        // creating object for credit card payment
        var creditCardPayment = new CreditCardPayment();
        var paymentService = new PaymentService(creditCardPayment);
        paymentService.getBillDetails();
    }
}
