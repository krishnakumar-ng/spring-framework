package com.example.springapplication;

import com.example.springapplication.payment.CreditCardPayment;
import com.example.springapplication.payment.DebitCardPayment;
import com.example.springapplication.payment.PaymentService;

public class LooseCouplingDemo {
    public static void main(String[] args) {
        var creditCardPayment = new CreditCardPayment();
        var paymentService = new PaymentService(creditCardPayment);
        paymentService.getBillDetails();

        var debitCardPayment = new DebitCardPayment();
        paymentService = new PaymentService(debitCardPayment);
        paymentService.getBillDetails();
    }
}
