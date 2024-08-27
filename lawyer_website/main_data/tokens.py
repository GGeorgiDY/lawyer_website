from django.contrib.auth.tokens import PasswordResetTokenGenerator
# No need to import six; Python 3 handles string conversions natively.


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return f"{user.pk}{timestamp}{user.is_active}"


account_activation_token = AccountActivationTokenGenerator()

