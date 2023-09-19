from ..base import AdyenServiceBase


class HostedOnboardingApi(AdyenServiceBase):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, client=None):
        super(HostedOnboardingApi, self).__init__(client=client)
        self.service = "legalEntityManagement"
        self.baseUrl = "https://kyc-test.adyen.com/lem/v3"

    def list_hosted_onboarding_page_themes(self, idempotency_key=None, **kwargs):
        """
        Get a list of hosted onboarding page themes
        """
        endpoint = self.baseUrl + f"/themes"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_onboarding_link_theme(self, id, idempotency_key=None, **kwargs):
        """
        Get an onboarding link theme
        """
        endpoint = self.baseUrl + f"/themes/{id}"
        method = "GET"
        return self.client.call_adyen_api(None, self.service, method, endpoint, idempotency_key, **kwargs)

    def get_link_to_adyenhosted_onboarding_page(self, request, id, idempotency_key=None, **kwargs):
        """
        Get a link to an Adyen-hosted onboarding page
        """
        endpoint = self.baseUrl + f"/legalEntities/{id}/onboardingLinks"
        method = "POST"
        return self.client.call_adyen_api(request, self.service, method, endpoint, idempotency_key, **kwargs)

