package com.example.payment_service_application.services;

import com.example.payment_service_application.entities.PaymentEntity;
import com.example.payment_service_application.enums.PaymentStatus;
import com.example.payment_service_application.exceptions.PaymentFailedException;
import com.example.payment_service_application.models.PaymentRequest;
import com.example.payment_service_application.models.PaymentResponse;
import com.example.payment_service_application.repositories.PaymentRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.Optional;

@Service
public class PaymentServiceImpl implements PaymentService {
    @Autowired
    private PaymentRepository paymentRepository;

    @Override
    public PaymentResponse makePayment(PaymentRequest paymentRequest) {
        PaymentStatus paymentStatus = paymentRequest.getAmount() < paymentRequest.getAmountRequired()
                ? PaymentStatus.FAILED : PaymentStatus.SUCCESSFUL;

        PaymentEntity paymentEntity = PaymentEntity.builder()
                .orderId(paymentRequest.getOrderId())
                .paymentDate(LocalDateTime.now())
                .paymentMode(paymentRequest.getPaymentMode())
                .paymentStatus(paymentStatus)
                .amountRequired(paymentRequest.getAmountRequired())
                .amount(paymentRequest.getAmount())
                .build();


        paymentRepository.save(paymentEntity);
        if (paymentStatus == PaymentStatus.FAILED)
            throw new PaymentFailedException("Payment is failed for paymentId - " + paymentEntity.getPaymentId() +
                    "\n Total amount required is: " + paymentRequest.getAmountRequired() +
                    "\n Provided amount required is: " + paymentRequest.getAmount());

        return PaymentResponse.builder()
                .paymentId(paymentEntity.getPaymentId())
                .orderId(paymentEntity.getOrderId())
                .paymentDate(paymentEntity.getPaymentDate())
                .paymentMode(paymentEntity.getPaymentMode())
                .paymentStatus(paymentEntity.getPaymentStatus())
                .amount(paymentEntity.getAmount())
                .build();
    }

    public PaymentResponse getPaymentDetailsById(String paymentId) {
        Optional<PaymentEntity> entity = paymentRepository.findById(paymentId);
        if (entity.isPresent()) {
            PaymentEntity paymentEntity = entity.get();
            return PaymentResponse.builder()
                    .paymentId(paymentEntity.getPaymentId())
                    .orderId(paymentEntity.getOrderId())
                    .paymentDate(paymentEntity.getPaymentDate())
                    .paymentMode(paymentEntity.getPaymentMode())
                    .paymentStatus(paymentEntity.getPaymentStatus())
                    .amount(paymentEntity.getAmount())
                    .build();
        } else {
            throw new RuntimeException("Payment details not found for payment id - " + paymentId);
        }
    }
}
