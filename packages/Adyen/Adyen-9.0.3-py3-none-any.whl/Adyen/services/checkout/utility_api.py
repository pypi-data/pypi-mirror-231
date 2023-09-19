from ..base import AdyenServiceBase


class UtilityApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(UtilityApi, self).__init__(client=client)
        self.service = "checkout"
        self.baseUrl = "https://checkout-test.adyen.com/v70"

    def get_apple_pay_session(self, request, idempotency_key=None, **kwargs):
        """
        Get an Apple Pay session
        """
        endpoint = self.baseUrl + f"/applePay/sessions"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

    def origin_keys(self, request, idempotency_key=None, **kwargs):
        """
        Create originKey values for domains
        """
        endpoint = self.baseUrl + f"/originKeys"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

