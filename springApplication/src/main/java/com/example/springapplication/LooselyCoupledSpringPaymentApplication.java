package com.example.springapplication;

import com.example.springapplication.payment.*;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class LooselyCoupledSpringPaymentApplication {
    public static void main(String[] args) {
        var context = new AnnotationConfigApplicationContext(SpringPaymentConfiguration.class);

//        PaymentService paymentService = context.getBean(PaymentService.class);
//        paymentService.getBillDetails();
//
//        PaymentService creditCard = context.getBean(PaymentService.class);
//        creditCard.getBillDetails();
//
//        PaymentService debitCard = context.getBean(PaymentService.class);
//        debitCard.getBillDetails();

//        var iPayment = context.getBean(DependencyByField.class);
//        iPayment.getBillDetails();

//        var iPayment = context.getBean(DependencyByMethod.class);
//        iPayment.getBillDetails();
//
        var iPayment = context.getBean(DependencyByConstructor.class);
        iPayment.getBillDetails();
    }
}
