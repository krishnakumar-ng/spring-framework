package com.example.order.service.application.exceptions;

import com.example.order.service.application.models.ErrorMessage;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
public class OrderServiceExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(OrderServiceException.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.UNPROCESSABLE_ENTITY)
    public ErrorMessage orderServiceExceptionHandler(OrderServiceException orderServiceException) {
        return ErrorMessage.builder()
                .errorCode(HttpStatus.UNPROCESSABLE_ENTITY.value())
                .errorStatus(HttpStatus.UNPROCESSABLE_ENTITY)
                .errorDescription(orderServiceException.getMessage()).build();
    }

    @ExceptionHandler(ExternalServiceException.class)
    @ResponseBody
    public ErrorMessage orderServiceExceptionHandler(ExternalServiceException externalServiceException) {
        return ErrorMessage.builder()
                .errorCode(externalServiceException.getErrorCode())
                .errorStatus(externalServiceException.getErrorStatus())
                .errorDescription(externalServiceException.getMessage()).build();
    }

    @ExceptionHandler(Exception.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorMessage genericExceptionHandler(Exception orderServiceException) {
        return ErrorMessage.builder()
                .errorCode(HttpStatus.INTERNAL_SERVER_ERROR.value())
                .errorStatus(HttpStatus.INTERNAL_SERVER_ERROR)
                .errorDescription(orderServiceException.getMessage()).build();
    }
}
