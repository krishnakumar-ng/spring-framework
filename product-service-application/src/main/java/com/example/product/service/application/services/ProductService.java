package com.example.product.service.application.services;

import com.example.product.service.application.models.Product;

import java.util.List;

public interface ProductService {
    Product addProduct(Product product);
    List<Product> getAllProducts();
    Product getProductById(String productId);
    List<Product> getProductByName(String productName);
    List<Product> getProductByNameLike(String productName);
    List<Product> getProductByNameLikeSort(String productName, String sortByField);
    Product updateOrderQuantity(String productId, Integer quantity);
}
