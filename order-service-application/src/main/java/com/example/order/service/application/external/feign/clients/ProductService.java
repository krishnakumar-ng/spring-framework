package com.example.order.service.application.external.feign.clients;

import com.example.order.service.application.models.Product;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestParam;

@FeignClient(name = "product-service-application/v1/product", url = "http://localhost:8080")
public interface ProductService {
    @GetMapping("/v1/product/{productId}")
    public ResponseEntity<Product> getProductById(@PathVariable("productId") String productId);

    @PutMapping("/v1/product/{productId}")
    public ResponseEntity<Product> updateProductQuantity(@PathVariable("productId") String productId, @RequestParam("quantity") Integer quantity);

}
