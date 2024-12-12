package com.example.payment_service_application.services;

import com.example.payment_service_application.models.PaymentRequest;
import com.example.payment_service_application.models.PaymentResponse;

public interface PaymentService {
    PaymentResponse makePayment(PaymentRequest paymentRequest);
    PaymentResponse getPaymentDetailsById(String paymentId);
}
