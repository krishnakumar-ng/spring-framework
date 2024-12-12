package com.example.payment_service_application.models;

import com.example.payment_service_application.enums.PaymentMode;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class PaymentRequest {
    private String orderId;
    private PaymentMode paymentMode;
    private Long amountRequired;
    private Long amount;
}
