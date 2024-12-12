package com.example.employee.service.application.repositories;

import com.example.employee.service.application.entities.EmployeeEntity;
import org.springframework.data.domain.Sort;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface EmployeeRepository extends JpaRepository<EmployeeEntity, String> {

    public List<EmployeeEntity> findByEmployeeName(String employeeName);

    @Query("SELECT e from EmployeeEntity e where employeeName like %:employeeName%")
    public List<EmployeeEntity> findByEmployeeNameLike(String employeeName);

    @Query("SELECT e from EmployeeEntity e where employeeName like %:employeeName%")
    public List<EmployeeEntity> findByEmployeeNameLikeOrderByField(String employeeName, Sort sort);
}
