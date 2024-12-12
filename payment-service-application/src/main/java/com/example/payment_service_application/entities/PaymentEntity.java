package com.example.payment_service_application.entities;

import com.example.payment_service_application.enums.PaymentMode;
import com.example.payment_service_application.enums.PaymentStatus;
import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Entity
@Table(name="payment_details")
public class PaymentEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String paymentId;
    private String orderId;
    private PaymentMode paymentMode;
    private LocalDateTime paymentDate;
    private PaymentStatus paymentStatus;
    private Long amountRequired;
    private Long amount;
}
