package com.example.order.service.application.services;

import com.example.order.service.application.entities.OrderEntity;
import com.example.order.service.application.enums.OrderStatus;
import com.example.order.service.application.exceptions.OrderServiceException;
import com.example.order.service.application.external.feign.clients.PaymentService;
import com.example.order.service.application.external.feign.clients.ProductService;
import com.example.order.service.application.external.models.PaymentRequest;
import com.example.order.service.application.external.models.PaymentResponse;
import com.example.order.service.application.models.OrderRequest;
import com.example.order.service.application.models.OrderResponse;
import com.example.order.service.application.models.Product;
import com.example.order.service.application.repositories.OrderRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

@Service
@Slf4j
public class OrderServiceImpl implements OrderService {
    @Autowired
    private OrderRepository orderRepository;
    @Autowired
    private ProductService productService;
    @Autowired
    private PaymentService paymentService;

    @Override
    public OrderResponse placeOrder(OrderRequest orderRequest) {

        Product product = productService.getProductById(orderRequest.getProductId()).getBody();

        assert product != null;
        if (product.getQuantity() < orderRequest.getQuantity()) {
            throw new OrderServiceException("Insufficient quantity of given product - " + orderRequest.getProductId());
        }
        log.info(orderRequest.getProductId() + " is exists with sufficient quantity");

        OrderEntity orderEntity = OrderEntity.builder()
                .productId(orderRequest.getProductId())
                .orderDate(LocalDateTime.now())
                .quantity(orderRequest.getQuantity())
                .orderStatus(OrderStatus.PLACED)
                .totalAmount(orderRequest.getTotalAmount())
                .build();

        long amount = orderEntity.getQuantity() * product.getPrice();

        orderRepository.save(orderEntity);

        OrderResponse orderResponse = new OrderResponse();
        BeanUtils.copyProperties(orderEntity, orderResponse);

        log.info("{}", orderResponse);

        PaymentRequest paymentRequest = PaymentRequest.builder()
                .orderId(orderResponse.getOrderId())
                .paymentMode("CREDIT_CARD")
                .amountRequired(amount)
                .amount(orderRequest.getTotalAmount())
                .build();

        PaymentResponse paymentResponse = paymentService.makePayment(paymentRequest).getBody();
        assert paymentResponse != null;

        log.info("Payment is successful.");
        log.info("Payment id: {}", paymentResponse.getPaymentId());

        productService.updateProductQuantity(orderRequest.getProductId(), product.getQuantity() - orderRequest.getQuantity());

        return updateOrderStatus(orderResponse.getOrderId(), OrderStatus.PAYMENT_COMPLETED);
    }

    @Override
    public OrderResponse updateOrderStatus(String orderId, OrderStatus orderStatus) {
        Optional<OrderEntity> entity = orderRepository.findById(orderId);
        OrderEntity orderEntity;
        if (entity.isPresent()) {
            orderEntity = entity.get();
            orderEntity.setOrderStatus(orderStatus);
            orderRepository.save(orderEntity);
        } else {
            throw new RuntimeException("Order id: " + orderId + " is not exist.");
        }

        return OrderResponse.builder()
                .orderId(orderEntity.getOrderId())
                .productId(orderEntity.getProductId())
                .orderDate(orderEntity.getOrderDate())
                .orderStatus(orderEntity.getOrderStatus())
                .quantity(orderEntity.getQuantity())
                .totalAmount(orderEntity.getTotalAmount())
                .build();
    }

    @Override
    public OrderResponse getOrderById(String orderId) {
        Optional<OrderEntity> entity = orderRepository.findById(orderId);
        OrderEntity orderEntity;
        if (entity.isPresent()) {
            orderEntity = entity.get();
            return OrderResponse.builder()
                    .orderId(orderEntity.getOrderId())
                    .productId(orderEntity.getProductId())
                    .orderDate(orderEntity.getOrderDate())
                    .orderStatus(orderEntity.getOrderStatus())
                    .quantity(orderEntity.getQuantity())
                    .totalAmount(orderEntity.getTotalAmount())
                    .build();
        } else {
            throw new RuntimeException("Order id: " + orderId + " is not exist.");
        }
    }

}
