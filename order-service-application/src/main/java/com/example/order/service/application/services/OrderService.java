package com.example.order.service.application.services;

import com.example.order.service.application.enums.OrderStatus;
import com.example.order.service.application.models.OrderRequest;
import com.example.order.service.application.models.OrderResponse;

public interface OrderService {
    OrderResponse placeOrder(OrderRequest orderRequest);

    OrderResponse updateOrderStatus(String orderId, OrderStatus orderStatus);

    OrderResponse getOrderById(String orderId);
}
