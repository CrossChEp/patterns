package generating.factory_method;

public class PhoneNotification implements Notification {
    @Override
    public String notifyUser() {
        return "it's a phone notification";
    }
}
