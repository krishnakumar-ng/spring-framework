package com.example.springapplication.payment;

public class PaymentService {
    private IPayment paymentMode;

    public PaymentService(IPayment paymentMode) {
        this.paymentMode = paymentMode;
    }

    public void getBillDetails() {
        System.out.println("Getting the payment details via " + this.paymentMode);
        this.paymentMode.makePayment();
        this.paymentMode.getPaymentDetails();

    }
}
