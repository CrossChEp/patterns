package generating.factory_method;

public class Main {
    public static void main(String[] args) {
        NotificationFactory notificationFactory = new NotificationFactory();
        Notification notification = notificationFactory.createNotification("email");
        System.out.println(notification.notifyUser());
    }
}
