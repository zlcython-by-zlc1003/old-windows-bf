public abstract class BankAccount {
    private double money;
    private boolean isSet;

    public BankAccount(double money) {
        if (!isSet) {
            this.money = money;
            isSet = true;
        }
    }

    public double getMoney() {
        return money;
    }
    public void setMoney(double money){
        this.money=money;
    }

    public void saveMoney(double money) {
        this.money += money;
    }

    public abstract void takeMoney(double money);
};