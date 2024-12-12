package com.example.product.service.application.entities;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

@Entity
@Table(name = "products")
@Data
public class ProductEntity {
    @Id
    private String productId;
    private String productName;
    private Long price;
    private Integer quantity;
}
