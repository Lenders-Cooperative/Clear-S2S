from django.test import TestCase
from django_clear_s2s import models
from django_clear_s2s.utils.ThomsonReuters import ThomsonReuters
import pprint

class TestUtils(TestCase):

    def setUp(self):
        self.client = ThomsonReuters()
        pass

    def test_person_search(self):
        _dict = {
            'first_name':'JANE',
            'last_name':'SAMPLE-DOCUMENT',
            'dob':'1951-01-01',
            'ssn':'999-99-9990',
            'street':'240 Summit Avenue',
            'city':'Saint Paul',
            'state':'MN',
            'zip_code':'55102',
            'phone_number':'651-396-0726',
            'npi_number':'9999999999'
        }
        response1, response2 = self.client.person_search(**_dict)

        assert response1.status_code == 200
        assert 'https://' in response1.find('ns2:PersonResults').get('Uri')
        assert response2 is not None

    def test_eidv_person_search(self):
        _dict = {
            'first_name':'JANE',
            'last_name':'SAMPLE-DOCUMENT',
            'dob':'1951-01-01',
            'ssn':'999-99-9990',
            'street':'240 Summit Avenue',
            'city':'Saint Paul',
            'state':'MN',
            'zip_code':'55102',
            'phone_number':'651-396-0726',
            'npi_number':'9999999999'
        }
        response1, response2 = self.client.eidv_person_search(**_dict)
        assert response1.status_code == 200
        assert 'https://' in response1.find('ns2:EIDVPersonResults').get('Uri')
        assert response2 is not None

    def test_person_quick_analysis_search(self):
        flags = {
            'assoc_with_ofac_global_pep': True,
            'ofac': True,
            'world_check': True,
            'global_sanctions': True,
            'residential_used_as_business': True,
            'prison_address': True,
            'po_box_address': True,
            'bankruptcy': True,
            'assoc_relative_with_residential_used_as_business': True,
            'assoc_relative_with_prison_address': True,
            'assoc_relative_with_po_box_address': True,
            'criminal': True,
            'multiple_ssn': True,
            'ssn_multiple_individuals': True,
            'recorded_as_deceased': True,
            'age_younger_than_ssn': True,
            'address_reported_less_ninety_days': True,
            'ssn_format_invalid': True,
            'healthcare_sanction': True,
            'phone_number_inconsistent_address': True,
            'arrest': True,
            'real_time_incarceration_and_arrest': True,
            'associated_with_marijuana_business': True,
            'entity_id': 'P1__MTYwNzg0NTcyNzc'
        }
        response1, response2 = self.client.person_quick_analysis_search(**flags)
        assert response1.status_code == 200
        assert 'https://' in response1.find('ns2:PersonQuickAnalysisFlagResults').get('Uri')
        assert response2 is not None

    def test_business_search(self):
        _dict = {
            'business_name':'Thomson Reuters',
            'corporation_id':'C1586596',
            'fein':'061497995',
            'duns_number':'116837516',
            'first_name':'Stephane',
            'last_name':'Bello',
            'street':'3 Times Square',
            'city':'New York',
            'state':'NY',
            'zip_code':'10036',
            'phone_number':'646-223-4000'
        }
        response1, response2 = self.client.business_search(**_dict)

        assert response1.status_code == 200
        assert 'https://' in response1.find('ns2:BusinessResults').get('Uri')
        assert response2 is not None

    def test_business_quick_analysis(self):
        flags = {
            'world_check': True,
            'ofac': True,
            'global_sanctions': True,
            'business_used_as_residential': True,
            'prison_address': True,
            'po_box_address': True,
            'bankruptcy': True,
            'listing_linked_to_business_phone': True,
            'listing_linked_to_business_address': True,
            'listing_linked_to_same_fein': True,
            'key_nature_of_suit': True,
            'pending_class_action': True,
            'going_concern': True,
            'healthcare_sanction': True,
            'msb_listing': True,
            'marijuana_related_business': True,
            'entity_id': 'C1__NDc2MzE3NTU'
        }

        response1, response2 = self.client.business_quick_analysis_search(**flags)
        assert response1.status_code == 200
        assert 'https://' in response1.find('ns2:CompanyQuickAnalysisFlagResults').get('Uri')
        assert response2 is not None

    def tearDown(self):
        pass
