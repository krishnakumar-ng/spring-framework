package com.example.spring_security.models;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Token {
    @JsonProperty("access_token")
    private String accessToken;
    @JsonProperty("expires_in")
    private int expirationTime;
    @JsonProperty("token_type")
    private String tokenType;

    public Token(String accessToken, int expirationTime, String tokenType) {
        this.accessToken = accessToken;
        this.expirationTime = expirationTime;
        this.tokenType = tokenType;
    }

    public String getAccessToken() {
        return accessToken;
    }

    public void setAccessToken(String accessToken) {
        this.accessToken = accessToken;
    }

    public int getExpirationTime() {
        return expirationTime;
    }

    public void setExpirationTime(int expirationTime) {
        this.expirationTime = expirationTime;
    }

    public String getTokenType() {
        return tokenType;
    }

    public void setTokenType(String tokenType) {
        this.tokenType = tokenType;
    }
}
