package com.example.payment_service_application.models;

import com.example.payment_service_application.enums.PaymentMode;
import com.example.payment_service_application.enums.PaymentStatus;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PaymentResponse {
    private String paymentId;
    private String orderId;
    private PaymentMode paymentMode;
    private LocalDateTime paymentDate;
    private PaymentStatus paymentStatus;
    private Long amount;
}
