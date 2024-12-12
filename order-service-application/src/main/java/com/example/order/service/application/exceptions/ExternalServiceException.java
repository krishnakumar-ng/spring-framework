package com.example.order.service.application.exceptions;

import lombok.Data;
import lombok.EqualsAndHashCode;
import org.springframework.http.HttpStatus;

@EqualsAndHashCode(callSuper = true)
@Data
public class ExternalServiceException extends RuntimeException {
    private Integer errorCode;
    private HttpStatus errorStatus;

    public ExternalServiceException(Integer errorCode, HttpStatus errorStatus, String message) {
        super(message);
        this.errorCode = errorCode;
        this.errorStatus = errorStatus;
    }
}
