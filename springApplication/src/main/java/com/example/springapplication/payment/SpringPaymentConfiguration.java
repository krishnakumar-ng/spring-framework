package com.example.springapplication.payment;

import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.Primary;

@Configuration
@ComponentScan(basePackages = "com.example.springapplication.payment")
public class SpringPaymentConfiguration {
//    @Bean
//    @Primary
//    public IPayment creditCard(){
//        return new CreditCardPayment();
//    }
//
//    @Bean
//    public IPayment debitCard(){
//        return new DebitCardPayment();
//    }
//
//    @Bean
//    public PaymentService paymentService(@Qualifier("debitCard") IPayment payment){
//        return new PaymentService(payment);
//    }
}
