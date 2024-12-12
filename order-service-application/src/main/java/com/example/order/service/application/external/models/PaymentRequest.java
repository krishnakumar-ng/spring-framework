package com.example.order.service.application.external.models;

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
    private String paymentMode;
    private Long amountRequired;
    private Long amount;
}
