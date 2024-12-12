package com.example.payment_service_application.controllers;

import com.example.payment_service_application.enums.PaymentStatus;
import com.example.payment_service_application.models.PaymentRequest;
import com.example.payment_service_application.models.PaymentResponse;
import com.example.payment_service_application.services.PaymentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/v1/payment")
public class PaymentsController {
    @Autowired
    private PaymentService paymentService;

    @PostMapping
    public ResponseEntity<PaymentResponse> makePayment(@RequestBody PaymentRequest paymentRequest) {
        PaymentResponse paymentResponse = paymentService.makePayment(paymentRequest);
        return new ResponseEntity<>(paymentResponse, HttpStatus.CREATED);
    }

    @GetMapping("/{paymentId}")
    public ResponseEntity<PaymentResponse> makePayment(@PathVariable("paymentId") String paymentId) {
        PaymentResponse paymentResponse = paymentService.getPaymentDetailsById(paymentId);
        return new ResponseEntity<>(paymentResponse, HttpStatus.OK);
    }
}
