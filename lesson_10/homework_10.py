"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest


def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
    return log_message

class TestLogEvent(unittest.TestCase):
    def test_success_logs_info(self):
        with self.assertLogs("log_event", level="INFO") as cm:
            log_message = log_event("user1", "success")
        self.assertIn(f"INFO:log_event:{log_message}", cm.output)

    def test_expired_logs_warning(self):
        with self.assertLogs("log_event", level="WARNING") as cm:
            log_message = log_event("bob", "expired")
        self.assertIn(f"WARNING:log_event:{log_message}", cm.output)

    def test_failed_logs_error(self):
        with self.assertLogs("log_event", level="ERROR") as cm:
            log_message = log_event("charlie", "failed")
        self.assertIn(f"ERROR:log_event:{log_message}", cm.output)

    def test_unknown_status_logs_error(self):
        with self.assertLogs("log_event", level="ERROR") as cm:
            log_message = log_event("david", "unknown_status")
        self.assertIn(f"ERROR:log_event:{log_message}", cm.output)


if __name__ == "__main__":
    unittest.main()