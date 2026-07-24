from abc import ABC, abstractmethod


class Notification(ABC):
    """
    Abstract notification interface.
    """

    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


class PushNotification(Notification):
    def send(self, message):
        print(f"Sending PUSH notification: {message}")


class NotificationService:
    """
    This class follows OCP.
    It does not need to change
    when new notification types are added.
    """

    def send(self, notification, message):
        notification.send(message)


def main():

    service = NotificationService()

    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()

    service.send(
        email,
        "Model training completed."
    )

    service.send(
        sms,
        "Deployment completed."
    )

    service.send(
        push,
        "New model available."
    )


if __name__ == "__main__":
    main()