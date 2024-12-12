package com.example.order.service.application.external.feign.clients;

import com.example.order.service.application.external.models.PaymentRequest;
import com.example.order.service.application.external.models.PaymentResponse;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;

@FeignClient(name="payment-service-application", url = "http://localhost:8082")
public interface PaymentService {
    @PostMapping("/v1/payment")
    public ResponseEntity<PaymentResponse> makePayment(PaymentRequest paymentRequest);
}
