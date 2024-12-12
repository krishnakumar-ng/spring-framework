package com.example.order.service.application.external.feign.error;

import com.example.order.service.application.exceptions.ExternalServiceException;
import com.example.order.service.application.models.ErrorMessage;
import com.fasterxml.jackson.databind.ObjectMapper;
import feign.Response;
import feign.codec.ErrorDecoder;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
@Slf4j
public class CustomErrorDecoder implements ErrorDecoder {
    @Override
    public Exception decode(String s, Response response) {
        ObjectMapper objectMapper = new ObjectMapper();

        try {
            log.info("input: {}", response.body().asInputStream());
            ErrorMessage errorMessage = objectMapper.readValue(response.body().asInputStream(), ErrorMessage.class);
            return new ExternalServiceException(errorMessage.getErrorCode(), errorMessage.getErrorStatus(), errorMessage.getErrorDescription());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
