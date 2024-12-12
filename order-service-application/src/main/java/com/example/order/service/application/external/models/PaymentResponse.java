package com.example.order.service.application.external.models;

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
    private String paymentMode;
    private LocalDateTime paymentDate;
    private String paymentStatus;
    private Long amount;
}
