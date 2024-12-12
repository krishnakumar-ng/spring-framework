package com.example.order.service.application.models;

import com.example.order.service.application.enums.OrderStatus;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class OrderResponse {
    private String orderId;
    private String productId;
    private Integer quantity;
    private LocalDateTime orderDate;
    private OrderStatus orderStatus;
    private Long totalAmount;
}
