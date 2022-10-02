package generating.factory_method;

public class PCNotification implements Notification {
    @Override
    public String notifyUser() {
        return "it's a pc notification";
    }
}
