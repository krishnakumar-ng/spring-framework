package com.example.order.service.application.entities;

import com.example.order.service.application.enums.OrderStatus;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Table(name = "orders")
public class OrderEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.UUID)
    private String orderId;
    private String productId;
    private Integer quantity;
    private LocalDateTime orderDate;
    private OrderStatus orderStatus;
    private Long totalAmount;
}
