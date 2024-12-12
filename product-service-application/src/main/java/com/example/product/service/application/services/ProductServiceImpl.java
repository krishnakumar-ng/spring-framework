package com.example.product.service.application.services;

import com.example.product.service.application.entities.ProductEntity;
import com.example.product.service.application.exceptions.ProductNotFoundException;
import com.example.product.service.application.models.Product;
import com.example.product.service.application.repositories.ProductRepository;
import com.example.product.service.application.utlls.Util;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Sort;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.concurrent.atomic.AtomicReference;


@Service
public class ProductServiceImpl implements ProductService {

    @Autowired
    private ProductRepository productRepository;

    @Override
    public Product addProduct(Product product) {
        if (product.getProductId() == null || product.getProductId().isEmpty()) {
            product.setProductId(UUID.randomUUID().toString());
        }
        productRepository.save(Util.convertModelToEntity(product));
        return product;
    }

    @Override
    public List<Product> getAllProducts() {
        return Util.convertEntitiesToModels(productRepository.findAll());
    }

    @Override
    public Product getProductById(String productId) {
        Optional<ProductEntity> productEntity = productRepository.findById(productId);
        if (productEntity.isPresent())
            return Util.convertEntityToModel(productEntity.get());
        else
            throw new ProductNotFoundException("No product exists with product id - " + productId);
    }

    @Override
    public List<Product> getProductByName(String productName) {
        return Util.convertEntitiesToModels(productRepository.findByProductName(productName));
    }

    @Override
    public List<Product> getProductByNameLike(String productName) {
        return Util.convertEntitiesToModels(productRepository.findByProductNameLike(productName));
    }


    @Override
    public List<Product> getProductByNameLikeSort(String productName, String sortByField) {
        return Util.convertEntitiesToModels(productRepository.getProductByNameLikeWithSort(productName, Sort.by(sortByField)));
    }

    @Override
    public Product updateOrderQuantity(String productId, Integer quantity) {
        Product product = getProductById(productId);
        ProductEntity productEntity = Util.convertModelToEntity(product);
        productEntity.setQuantity(quantity);
        productRepository.save(productEntity);
        return Util.convertEntityToModel(productEntity);
    }
}
