package com.company;

import java.util.function.Function;

class A
{
    public static void main(String[] args)
    {
        Function<String,String> upperCase=String::toUpperCase;
        Function<String,String> trim=String::trim;
        String string=" Hi ";
        Function<String, String> upperCaseThenTrim = upperCase.andThen(trim);
        System.out.println(upperCaseThenTrim.apply(string));
        System.out.println(trim.compose(upperCase).apply(string));
    }
}

