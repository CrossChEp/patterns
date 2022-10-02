package generating.factory_method;

public class EmailNotification implements Notification {
    @Override
    public String notifyUser() {
        return "it's an email notification";
    }
}
