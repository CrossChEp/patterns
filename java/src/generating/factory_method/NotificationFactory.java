package generating.factory_method;

public class NotificationFactory {
    public Notification createNotification(String notificationClass) {
        switch (notificationClass) {
            case "email" -> { return new EmailNotification(); }
            case "phone" -> { return  new PhoneNotification(); }
            case "pc" -> { return  new PCNotification(); }
            default -> { return null; }
        }
    }
}
