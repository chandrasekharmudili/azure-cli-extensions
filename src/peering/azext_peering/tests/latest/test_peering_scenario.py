# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=line-too-long

import os
import unittest

from azure_devtools.scenario_tests import AllowLargeResponse
from azure.cli.testsdk import ScenarioTest
from .. import try_manual
from azure.cli.testsdk import ResourceGroupPreparer


TEST_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__), '..'))


@try_manual
def setup(test, rg):
    pass


# EXAMPLE: /PeerAsns/put/Create a peer ASN
@try_manual
def step__peerasns_put_create_a_peer_asn(test, rg):
    test.cmd('az asn create '
             '--peer-asn 65000 '
             '--peer-contact-detail email="noc@contoso.com" phone="+1 (234) 567-8999" role="Noc" '
             '--peer-contact-detail email="abc@contoso.com" phone="+1 (234) 567-8900" role="Policy" '
             '--peer-contact-detail email="xyz@contoso.com" phone="+1 (234) 567-8900" role="Technical" '
             '--peer-name "Contoso" '
             '--peer-asn-name "{PeerAsns_2}"',
             checks=[])


# EXAMPLE: /LegacyPeerings/get/List legacy peerings
@try_manual
def step__legacypeerings_get_list_legacy_peerings(test, rg):
    test.cmd('az asn list '
             '--kind "Exchange" '
             '--peering-location "peeringLocation0"',
             checks=[])


# EXAMPLE: /PeerAsns/get/Get a peer ASN
@try_manual
def step__peerasns_get_get_a_peer_asn(test, rg):
    test.cmd('az asn show '
             '--peer-asn-name "{PeerAsns_2}"',
             checks=[])


# EXAMPLE: /PeerAsns/get/List peer ASNs in a subscription
@try_manual
def step__peerasns_get_list_peer_asns_in_a_subscription(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /PeeringLocations/get/List direct peering locations
@try_manual
def step__peeringlocations_get_list_direct_peering_locations(test, rg):
    test.cmd('az asn list '
             '--kind "Direct"',
             checks=[])


# EXAMPLE: /PeeringLocations/get/List exchange peering locations
@try_manual
def step__peeringlocations_get_list_exchange_peering_locations(test, rg):
    test.cmd('az asn list '
             '--kind "Exchange"',
             checks=[])


# EXAMPLE: /PeeringServiceCountries/get/List peering service countries
@try_manual
def step__peeringservicecountries_get_list_peering_service_countries(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /PeeringServiceLocations/get/List peering service locations
@try_manual
def step__peeringservicelocations_get_list_peering_service_locations(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /PeeringServiceProviders/get/List peering service providers
@try_manual
def step__peeringserviceproviders_get_list_peering_service_providers(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /PeeringServices/put/Create a  peering service
@try_manual
def step__peeringservices_put_create_a__peering_service(test, rg):
    test.cmd('az asn create '
             '--location "eastus" '
             '--peering-service-location "state1" '
             '--peering-service-provider "serviceProvider1" '
             '--peering-service-name "{peeringServiceName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /PeeringServices/get/Get a peering service
@try_manual
def step__peeringservices_get_get_a_peering_service(test, rg):
    test.cmd('az asn show '
             '--peering-service-name "{peeringServiceName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /PeeringServices/get/List peering services in a resource group
@try_manual
def step__peeringservices_get_list_peering_services_in_a_resource_group(test, rg):
    test.cmd('az asn list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /PeeringServices/get/List peering services in a subscription
@try_manual
def step__peeringservices_get_list_peering_services_in_a_subscription(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /PeeringServices/patch/Update peering service tags
@try_manual
def step__peeringservices_patch_update_peering_service_tags(test, rg):
    test.cmd('az asn update '
             '--peering-service-name "{peeringServiceName}" '
             '--resource-group "{rg}" '
             '--tags tags={{"tag0":"value0","tag1":"value1"}}',
             checks=[])


# EXAMPLE: /Peerings/put/Create a peering with exchange route server
@try_manual
def step__peerings_put_create_a_peering_with_exchange_route_server(test, rg):
    test.cmd('az asn create '
             '--kind "Direct" '
             '--location "eastus" '
             '--direct "{{\\"connections\\":[{{\\"bandwidthInMbps\\":10000,\\"bgpSession\\":{{\\"maxPrefixesAdvertisedV'
             '4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"microsoftSessionIPv4Address\\":\\"192.168.0.123\\",\\"peer'
             'SessionIPv4Address\\":\\"192.168.0.234\\",\\"sessionPrefixV4\\":\\"192.168.0.0/24\\"}},\\"connectionIdent'
             'ifier\\":\\"5F4CB5C7-6B43-4444-9338-9ABC72606C16\\",\\"peeringDBFacilityId\\":99999,\\"sessionAddressProv'
             'ider\\":\\"Peer\\",\\"useForPeeringService\\":true}}],\\"directPeeringType\\":\\"IxRs\\",\\"peerAsn\\":{{'
             '\\"id\\":\\"/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{myAsn1}\\"}}}}" '
             '--peering-location "peeringLocation0" '
             '--sku name="Premium_Direct_Free" '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/put/Create an exchange peering
@try_manual
def step__peerings_put_create_an_exchange_peering(test, rg):
    test.cmd('az asn create '
             '--kind "Exchange" '
             '--location "eastus" '
             '--exchange "{{\\"connections\\":[{{\\"bgpSession\\":{{\\"maxPrefixesAdvertisedV4\\":1000,\\"maxPrefixesAd'
             'vertisedV6\\":100,\\"md5AuthenticationKey\\":\\"test-md5-auth-key\\",\\"peerSessionIPv4Address\\":\\"192.'
             '168.2.1\\",\\"peerSessionIPv6Address\\":\\"fd00::1\\"}},\\"connectionIdentifier\\":\\"CE495334-0E94-4E51-'
             '8164-8116D6CD284D\\",\\"peeringDBFacilityId\\":99999}},{{\\"bgpSession\\":{{\\"maxPrefixesAdvertisedV4\\"'
             ':1000,\\"maxPrefixesAdvertisedV6\\":100,\\"md5AuthenticationKey\\":\\"test-md5-auth-key\\",\\"peerSession'
             'IPv4Address\\":\\"192.168.2.2\\",\\"peerSessionIPv6Address\\":\\"fd00::2\\"}},\\"connectionIdentifier\\":'
             '\\"CDD8E673-CB07-47E6-84DE-3739F778762B\\",\\"peeringDBFacilityId\\":99999}}],\\"peerAsn\\":{{\\"id\\":\\'
             '"/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{myAsn1}\\"}}}}" '
             '--peering-location "peeringLocation0" '
             '--sku name="Basic_Exchange_Free" '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/put/Create a direct peering
@try_manual
def step__peerings_put_create_a_direct_peering(test, rg):
    test.cmd('az asn create '
             '--kind "Direct" '
             '--location "eastus" '
             '--direct "{{\\"connections\\":[{{\\"bandwidthInMbps\\":10000,\\"bgpSession\\":{{\\"maxPrefixesAdvertisedV'
             '4\\":1000,\\"maxPrefixesAdvertisedV6\\":100,\\"md5AuthenticationKey\\":\\"test-md5-auth-key\\",\\"session'
             'PrefixV4\\":\\"192.168.0.0/31\\",\\"sessionPrefixV6\\":\\"fd00::0/127\\"}},\\"connectionIdentifier\\":\\"'
             '5F4CB5C7-6B43-4444-9338-9ABC72606C16\\",\\"peeringDBFacilityId\\":99999,\\"sessionAddressProvider\\":\\"P'
             'eer\\",\\"useForPeeringService\\":false}},{{\\"bandwidthInMbps\\":10000,\\"connectionIdentifier\\":\\"8AB'
             '00818-D533-4504-A25A-03A17F61201C\\",\\"peeringDBFacilityId\\":99999,\\"sessionAddressProvider\\":\\"Micr'
             'osoft\\",\\"useForPeeringService\\":true}}],\\"directPeeringType\\":\\"Edge\\",\\"peerAsn\\":{{\\"id\\":'
             '\\"/subscriptions/{subscription_id}/providers/Microsoft.Peering/peerAsns/{myAsn1}\\"}}}}" '
             '--peering-location "peeringLocation0" '
             '--sku name="Basic_Direct_Free" '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/get/Get a peering
@try_manual
def step__peerings_get_get_a_peering(test, rg):
    test.cmd('az asn show '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/get/List peerings in a resource group
@try_manual
def step__peerings_get_list_peerings_in_a_resource_group(test, rg):
    test.cmd('az asn list '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/get/List peerings in a subscription
@try_manual
def step__peerings_get_list_peerings_in_a_subscription(test, rg):
    test.cmd('az asn list',
             checks=[])


# EXAMPLE: /Peerings/patch/Update peering tags
@try_manual
def step__peerings_patch_update_peering_tags(test, rg):
    test.cmd('az asn update '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}" '
             '--tags tags={{"tag0":"value0","tag1":"value1"}}',
             checks=[])


# EXAMPLE: /Prefixes/put/Create or update a prefix for the peering service
@try_manual
def step__prefixes_put_create_or_update_a_prefix_for_the_peering_service(test, rg):
    test.cmd('az asn create '
             '--peering-service-name "{peeringServiceName}" '
             '--peering-service-prefix-key "00000000-0000-0000-0000-000000000000" '
             '--prefix "192.168.1.0/24" '
             '--prefix-name "{peeringServicePrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Prefixes/get/Get a prefix associated with the peering service
@try_manual
def step__prefixes_get_get_a_prefix_associated_with_the_peering_service(test, rg):
    test.cmd('az asn show '
             '--peering-service-name "{peeringServiceName}" '
             '--prefix-name "{peeringServicePrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Prefixes/get/List all the prefixes associated with the peering service
@try_manual
def step__prefixes_get_list_all_the_prefixes_associated_with_the_peering_service(test, rg):
    test.cmd('az asn list '
             '--peering-service-name "{peeringServiceName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /ReceivedRoutes/get/Lists the prefixes received over the specified peering under the given subscription and resource group.
@try_manual
def step__receivedroutes_get_lists_the_prefixes_received_over_the_specified_peering_under_the_given_subscription_and_resource_group_(test,
                                                                                                                                      rg):
    test.cmd('az asn list '
             '--as-path "123 456" '
             '--origin-as-validation-state "Valid" '
             '--peering-name "{peeringName}" '
             '--prefix "1.1.1.0/24" '
             '--resource-group "{rg}" '
             '--rpki-validation-state "Valid"',
             checks=[])


# EXAMPLE: /RegisteredAsns/put/Create or update a registered ASN for the peering
@try_manual
def step__registeredasns_put_create_or_update_a_registered_asn_for_the_peering(test, rg):
    test.cmd('az asn create '
             '--peering-name "{peeringName}" '
             '--asn 65000 '
             '--registered-asn-name "{registeredAsnName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredAsns/get/Get a registered ASN associated with the peering
@try_manual
def step__registeredasns_get_get_a_registered_asn_associated_with_the_peering(test, rg):
    test.cmd('az asn show '
             '--peering-name "{peeringName}" '
             '--registered-asn-name "{RegisteredAsns_2}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredAsns/get/List all the registered ASNs associated with the peering
@try_manual
def step__registeredasns_get_list_all_the_registered_asns_associated_with_the_peering(test, rg):
    test.cmd('az asn list '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredPrefixes/put/Create or update a registered prefix for the peering
@try_manual
def step__registeredprefixes_put_create_or_update_a_registered_prefix_for_the_peering(test, rg):
    test.cmd('az asn create '
             '--peering-name "{peeringName}" '
             '--prefix "10.22.20.0/24" '
             '--registered-prefix-name "{registeredPrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredPrefixes/get/Get a registered prefix associated with the peering
@try_manual
def step__registeredprefixes_get_get_a_registered_prefix_associated_with_the_peering(test, rg):
    test.cmd('az asn show '
             '--peering-name "{peeringName}" '
             '--registered-prefix-name "{registeredPrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredPrefixes/get/List all the registered prefixes associated with the peering
@try_manual
def step__registeredprefixes_get_list_all_the_registered_prefixes_associated_with_the_peering(test, rg):
    test.cmd('az asn list '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /asn/post/Check if peering service provider is available in customer location
@try_manual
def step__asn_post_check_if_peering_service_provider_is_available_in_customer_location(test, rg):
    test.cmd('az asn check-service-provider-availability '
             '--peering-service-location "peeringServiceLocation1" '
             '--peering-service-provider "peeringServiceProvider1"',
             checks=[])


# EXAMPLE: /RegisteredAsns/delete/Deletes a registered ASN associated with the peering
@try_manual
def step__registeredasns_delete_deletes_a_registered_asn_associated_with_the_peering(test, rg):
    test.cmd('az asn delete '
             '--peering-name "{peeringName}" '
             '--registered-asn-name "{registeredAsnName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Prefixes/delete/Delete a prefix associated with the peering service
@try_manual
def step__prefixes_delete_delete_a_prefix_associated_with_the_peering_service(test, rg):
    test.cmd('az asn delete '
             '--peering-service-name "{peeringServiceName}" '
             '--prefix-name "{peeringServicePrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /RegisteredPrefixes/delete/Deletes a registered prefix associated with the peering
@try_manual
def step__registeredprefixes_delete_deletes_a_registered_prefix_associated_with_the_peering(test, rg):
    test.cmd('az asn delete '
             '--peering-name "{peeringName}" '
             '--registered-prefix-name "{registeredPrefixName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /PeeringServices/delete/Delete a peering service
@try_manual
def step__peeringservices_delete_delete_a_peering_service(test, rg):
    test.cmd('az asn delete '
             '--peering-service-name "{peeringServiceName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /Peerings/delete/Delete a peering
@try_manual
def step__peerings_delete_delete_a_peering(test, rg):
    test.cmd('az asn delete '
             '--peering-name "{peeringName}" '
             '--resource-group "{rg}"',
             checks=[])


# EXAMPLE: /PeerAsns/delete/Delete a peer ASN
@try_manual
def step__peerasns_delete_delete_a_peer_asn(test, rg):
    test.cmd('az asn delete '
             '--peer-asn-name "{PeerAsns_2}"',
             checks=[])


@try_manual
def cleanup(test, rg):
    pass


@try_manual
def call_scenario(test, rg):
    setup(test, rg)
    step__peerasns_put_create_a_peer_asn(test, rg)
    step__legacypeerings_get_list_legacy_peerings(test, rg)
    step__peerasns_get_get_a_peer_asn(test, rg)
    step__peerasns_get_list_peer_asns_in_a_subscription(test, rg)
    step__peeringlocations_get_list_direct_peering_locations(test, rg)
    step__peeringlocations_get_list_exchange_peering_locations(test, rg)
    step__peeringservicecountries_get_list_peering_service_countries(test, rg)
    step__peeringservicelocations_get_list_peering_service_locations(test, rg)
    step__peeringserviceproviders_get_list_peering_service_providers(test, rg)
    step__peeringservices_put_create_a__peering_service(test, rg)
    step__peeringservices_get_get_a_peering_service(test, rg)
    step__peeringservices_get_list_peering_services_in_a_resource_group(test, rg)
    step__peeringservices_get_list_peering_services_in_a_subscription(test, rg)
    step__peeringservices_patch_update_peering_service_tags(test, rg)
    step__peerings_put_create_a_peering_with_exchange_route_server(test, rg)
    step__peerings_put_create_an_exchange_peering(test, rg)
    step__peerings_put_create_a_direct_peering(test, rg)
    step__peerings_get_get_a_peering(test, rg)
    step__peerings_get_list_peerings_in_a_resource_group(test, rg)
    step__peerings_get_list_peerings_in_a_subscription(test, rg)
    step__peerings_patch_update_peering_tags(test, rg)
    step__prefixes_put_create_or_update_a_prefix_for_the_peering_service(test, rg)
    step__prefixes_get_get_a_prefix_associated_with_the_peering_service(test, rg)
    step__prefixes_get_list_all_the_prefixes_associated_with_the_peering_service(test, rg)
    step__receivedroutes_get_lists_the_prefixes_received_over_the_specified_peering_under_the_given_subscription_and_resource_group_(test,
                                                                                                                                      rg)
    step__registeredasns_put_create_or_update_a_registered_asn_for_the_peering(test, rg)
    step__registeredasns_get_get_a_registered_asn_associated_with_the_peering(test, rg)
    step__registeredasns_get_list_all_the_registered_asns_associated_with_the_peering(test, rg)
    step__registeredprefixes_put_create_or_update_a_registered_prefix_for_the_peering(test, rg)
    step__registeredprefixes_get_get_a_registered_prefix_associated_with_the_peering(test, rg)
    step__registeredprefixes_get_list_all_the_registered_prefixes_associated_with_the_peering(test, rg)
    step__asn_post_check_if_peering_service_provider_is_available_in_customer_location(test, rg)
    step__registeredasns_delete_deletes_a_registered_asn_associated_with_the_peering(test, rg)
    step__prefixes_delete_delete_a_prefix_associated_with_the_peering_service(test, rg)
    step__registeredprefixes_delete_deletes_a_registered_prefix_associated_with_the_peering(test, rg)
    step__peeringservices_delete_delete_a_peering_service(test, rg)
    step__peerings_delete_delete_a_peering(test, rg)
    step__peerasns_delete_delete_a_peer_asn(test, rg)
    cleanup(test, rg)


@try_manual
class PeeringManagementClientScenarioTest(ScenarioTest):

    @ResourceGroupPreparer(name_prefix='clitestpeering_rgName'[:7], key='rg', parameter_name='rg')
    def test_peering(self, rg):

        self.kwargs.update({
            'subscription_id': self.get_subscription_id()
        })

        self.kwargs.update({
            'myAsn1': 'myAsn1',
            'PeerAsns_2': 'PeerAsns_2',
            'peeringName': 'peeringName',
            'peeringServiceName': 'peeringServiceName',
            'default': 'default',
            'registeredAsnName': 'registeredAsnName',
            'RegisteredAsns_2': 'RegisteredAsns_2',
            'registeredPrefixName': 'registeredPrefixName',
            'peeringServicePrefixName': 'peeringServicePrefixName',
        })

        call_scenario(self, rg)
