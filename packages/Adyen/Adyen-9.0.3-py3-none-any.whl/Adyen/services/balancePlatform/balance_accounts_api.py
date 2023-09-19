from ..base import AdyenServiceBase


class BalanceAccountsApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(BalanceAccountsApi, self).__init__(client=client)
        self.service = "balancePlatform"
        self.baseUrl = "https://balanceplatform-api-test.adyen.com/bcl/v2"

    def delete_sweep(self, balanceAccountId, sweepId, idempotency_key=None, **kwargs):
        """
        Delete a sweep
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"
        method = "DELETE"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_sweeps_for_balance_account(self, balanceAccountId, idempotency_key=None, **kwargs):
        """
        Get all sweeps for a balance account
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{balanceAccountId}/sweeps"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_sweep(self, balanceAccountId, sweepId, idempotency_key=None, **kwargs):
        """
        Get a sweep
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_balance_account(self, id, idempotency_key=None, **kwargs):
        """
        Get a balance account
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_all_payment_instruments_for_balance_account(self, id, idempotency_key=None, **kwargs):
        """
        Get all payment instruments for a balance account
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{id}/paymentInstruments"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_sweep(self, request, balanceAccountId, sweepId, idempotency_key=None, **kwargs):
        """
        Update a sweep
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{balanceAccountId}/sweeps/{sweepId}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def update_balance_account(self, request, id, idempotency_key=None, **kwargs):
        """
        Update a balance account
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{id}"
        method = "PATCH"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_balance_account(self, request, idempotency_key=None, **kwargs):
        """
        Create a balance account
        """
        endpoint = self.baseUrl + f"/balanceAccounts"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def create_sweep(self, request, balanceAccountId, idempotency_key=None, **kwargs):
        """
        Create a sweep
        """
        endpoint = self.baseUrl + f"/balanceAccounts/{balanceAccountId}/sweeps"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

