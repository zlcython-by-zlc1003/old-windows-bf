public class CheqAccount extends BankAccount {

    public CheqAccount(double money) {
        super(money);
    }

    @Override
    public void takeMoney(double money) {
        setMoney((getMoney()) - money - (money * 0.0005));
    }

}
