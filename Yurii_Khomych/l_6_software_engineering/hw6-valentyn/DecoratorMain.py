class Notification:
    def sendSth(self) -> str:
        pass


class EmailNotification(Notification):
    def sendSth(self) -> str:
        return "Send notification via Email."


class Decorator(Notification):
    _notification = None

    def __init__(self, notification) -> None:
        self._notification = notification

    @property
    def notification(self) -> str:
        return self._notification

    def sendSth(self) -> str:
        self._notification.sendSth()


class SendViaSMS(Decorator):
    def sendSth(self) -> str:
        return f"Send via SMS and ({self.notification.sendSth()})"


class SendViaWatsApp(Decorator):
    def sendSth(self) -> str:
        return f"Send via WatsApp and ({self.notification.sendSth()})"


def client_code(notification: Notification) -> None:
    print(f"RESULT: {notification.sendSth()}", end="")


if __name__ == "__main__":
    email = EmailNotification()
    print("Sending only via Email:")
    client_code(email)
    print("\n")

    email_sms = SendViaSMS(email)
    email_sms_watsapp = SendViaWatsApp(email_sms)
    print("Client: Now I've got a decorated Notification:")
    client_code(email_sms_watsapp)
