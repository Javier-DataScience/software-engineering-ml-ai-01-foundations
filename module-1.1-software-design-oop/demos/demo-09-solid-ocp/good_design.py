"""
===============================================================================
Module: good_design.py

Path: module-1.1-software-design-oop/demos/demo-09-solid-ocp/good_design.py

Purpose:
Demonstrate a correct implementation of the Open/Closed Principle (OCP)
using abstraction, inheritance, and polymorphism.

===============================================================================
"""

from abc import ABC, abstractmethod


class Notification(ABC):  # Force child classes to implement this method.
    """Abstract notification interface."""

    @abstractmethod
    def send(self, message):  # Common notification interface.
        """Send a notification."""


class EmailNotification(Notification):  # Notification implementation.
    """Email notification."""

    def send(self, message):  # Implements the notification contract.
        print(f"Sending EMAIL: {message}")


class SMSNotification(Notification):  # Notification implementation.
    """SMS notification."""

    def send(self, message):  # Implements the notification contract.
        print(f"Sending SMS: {message}")


class PushNotification(Notification):  # Notification implementation.
    """Push notification."""

    def send(self, message):  # Implements the notification contract.
        print(f"Sending PUSH notification: {message}")


class NotificationService:
    """Service responsible for sending notifications."""

    def send(self, notification, message):  # Works with any Notification.
        notification.send(message)  # Polymorphic call.


def main():  # Coordinates the demonstration.
    """Program entry point."""

    service = NotificationService()

    email = EmailNotification()
    sms = SMSNotification()
    push = PushNotification()

    service.send(email, "Model training completed.")
    service.send(sms, "Deployment completed.")
    service.send(push, "New model available.")


if __name__ == "__main__":  # Script entry point.
    main()
