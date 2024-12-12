package com.example.product.service.application.controller;

import com.example.product.service.application.models.Product;
import com.example.product.service.application.services.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/v1/product")
public class ProductController {

    @Qualifier("productServiceImpl")
    @Autowired
    private ProductService productService;

    @PostMapping
    public Product addProduct(@RequestBody Product product) {
        return this.productService.addProduct(product);
    }

    @GetMapping("/all")
    public List<Product> getAllProducts() {
        return this.productService.getAllProducts();
    }

    @GetMapping("/{productId}")
    public Product getProductById(@PathVariable("productId") String productId) {
        return this.productService.getProductById(productId);
    }

    @GetMapping
    public List<Product> getProductByName(@RequestParam("productName") String productName) {
        return this.productService.getProductByName(productName);
    }

    @GetMapping("/sort")
    public List<Product> getProductByNameAndSort(@RequestParam("productName") String productName,
                                                 @RequestParam(name = "sortBy", required = false, defaultValue = "price") String sortBy) {
        return this.productService.getProductByNameLikeSort(productName, sortBy);
    }

    @PutMapping("/{productId}")
    public ResponseEntity<Product> updateProductQuantity(@PathVariable("productId") String productId,
                                                     @RequestParam("quantity") Integer quantity) {
        Product product = productService.updateOrderQuantity(productId, quantity);
        return new ResponseEntity<>(product, HttpStatus.OK);
    }

}
