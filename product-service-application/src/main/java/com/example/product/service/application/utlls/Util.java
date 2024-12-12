package com.example.product.service.application.utlls;

import com.example.product.service.application.entities.ProductEntity;
import com.example.product.service.application.models.Product;
import lombok.AccessLevel;
import lombok.NoArgsConstructor;
import org.springframework.beans.BeanUtils;

import java.util.List;

@NoArgsConstructor(access = AccessLevel.PRIVATE)
public class Util {
    public static List<Product> convertEntitiesToModels(List<ProductEntity> productEntities) {
        return productEntities.stream().map(productEntity -> {
            Product product = new Product();
            BeanUtils.copyProperties(productEntity, product);
            return product;
        }).toList();
    }

    public static Product convertEntityToModel(ProductEntity productEntity) {
        Product product = new Product();
        BeanUtils.copyProperties(productEntity, product);
        return product;
    }

    public static ProductEntity convertModelToEntity(Product product) {
        ProductEntity productEntity = new ProductEntity();
        BeanUtils.copyProperties(product, productEntity);
        return productEntity;
    }
}
