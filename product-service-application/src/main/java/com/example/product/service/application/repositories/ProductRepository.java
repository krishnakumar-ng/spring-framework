package com.example.product.service.application.repositories;

import com.example.product.service.application.entities.ProductEntity;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ProductRepository extends JpaRepository<ProductEntity,String> {

    @Query("SELECT p from ProductEntity p where productName like %:productName%")
    List<ProductEntity> getProductByNameLikeWithSort(String productName, Sort sort);

    List<ProductEntity> findByProductName(String productName);

    @Query("SELECT p from ProductEntity p where productName like %:productName%")
    List<ProductEntity> findByProductNameLike(String productName);

}
