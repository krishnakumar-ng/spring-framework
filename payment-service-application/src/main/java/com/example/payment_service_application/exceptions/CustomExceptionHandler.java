package com.example.payment_service_application.exceptions;

import com.example.payment_service_application.models.ErrorMessage;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
public class CustomExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(PaymentFailedException.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.PAYMENT_REQUIRED)
    public ErrorMessage productNotFoundExceptionHandler(PaymentFailedException paymentFailedException) {
        return new ErrorMessage(HttpStatus.PAYMENT_REQUIRED.value(), HttpStatus.PAYMENT_REQUIRED, paymentFailedException.getMessage());
    }

    @ExceptionHandler(Exception.class)
    @ResponseBody
    @ResponseStatus(HttpStatus.INTERNAL_SERVER_ERROR)
    public ErrorMessage genericExceptionHandler(Exception exception) {
        return new ErrorMessage(HttpStatus.INTERNAL_SERVER_ERROR.value(), HttpStatus.INTERNAL_SERVER_ERROR, exception.getMessage());
    }
}
