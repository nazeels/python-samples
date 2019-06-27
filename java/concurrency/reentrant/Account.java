package com.company;

import java.util.concurrent.locks.ReentrantLock;

public class Account {
    private ReentrantLock implicitLock= new ReentrantLock();
    private String name;
    private Integer balance=10000;
    public ReentrantLock getImplicitLock() {
        return implicitLock;
    }
    public String getName() {
        return name;
    }
    public void setName(String name) {
        this.name = name;
    }
    public Integer getBalance() {
        return balance;
    }
    public void setBalance(Integer blance) {
        this.balance = blance;
    }
    public boolean debit(Integer amount)
    {
        if(amount > balance)
        {
            System.out.println(Thread.currentThread().getName() + " :: " +name + " says ::"+ amount + " grater than current balance" );
            return false;
        }
        balance = balance -amount;
        System.out.println(Thread.currentThread().getName() + " :: " + name + " says ::"+ amount + " Debited Success Fully" );
        return true;
    }
    public void credit(Integer amount)
    {
        balance = balance +amount;
        System.out.println(Thread.currentThread().getName() + " :: " + name + " says ::"+ amount + " Credited Success Fully" );
    }
}

