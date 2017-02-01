#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 on 2017-02-01.
#  2017, SMART Health IT.


import os
import io
import unittest
import json
from . import eligibilityresponse
from .fhirdate import FHIRDate


class EligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EligibilityResponse", js["resourceType"])
        return eligibilityresponse.EligibilityResponse(js)
    
    def testEligibilityResponse1(self):
        inst = self.instantiate_from("eligibilityresponse-example-benefits-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse1(inst2)
    
    def implEligibilityResponse1(self, inst):
        self.assertEqual(inst.contained[0].id, "patient-1")
        self.assertEqual(inst.contained[1].id, "coverage-1")
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2502")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812342")
        self.assertTrue(inst.inforce)
        self.assertEqual(inst.insurance[0].benefitBalance[0].category.coding[0].code, "medical")
        self.assertEqual(inst.insurance[0].benefitBalance[0].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code, "USD")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.code, "USD")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.value, 3748.0)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code, "USD")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].benefitBalance[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[0].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[0].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[0].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[1].category.coding[0].code, "medical")
        self.assertEqual(inst.insurance[0].benefitBalance[1].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code, "USD")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[1].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[1].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[1].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[2].category.coding[0].code, "oral")
        self.assertEqual(inst.insurance[0].benefitBalance[2].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code, "USD")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[2].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[2].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[2].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[3].category.coding[0].code, "vision")
        self.assertEqual(inst.insurance[0].benefitBalance[3].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[3].description, "Vision products and services such as exams, glasses and contatc lenses.")
        self.assertTrue(inst.insurance[0].benefitBalance[3].excluded)
        self.assertEqual(inst.insurance[0].benefitBalance[3].name, "Vision")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.outcome.coding[0].code, "complete")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/remittance-outcome")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEligibilityResponse2(self):
        inst = self.instantiate_from("eligibilityresponse-example-benefits.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse2(inst2)
    
    def implEligibilityResponse2(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2501")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.inforce)
        self.assertEqual(inst.insurance[0].benefitBalance[0].category.coding[0].code, "medical")
        self.assertEqual(inst.insurance[0].benefitBalance[0].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value, 500000)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value, 100)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code, "copay-maximum")
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt, 20)
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code, "copay-percent")
        self.assertEqual(inst.insurance[0].benefitBalance[0].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[0].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].code, "30")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].display, "Health Benefit Plan Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[0].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[0].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[0].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[0].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[0].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[1].category.coding[0].code, "medical")
        self.assertEqual(inst.insurance[0].benefitBalance[1].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value, 15000)
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[1].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[1].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].code, "69")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].display, "Maternity")
        self.assertEqual(inst.insurance[0].benefitBalance[1].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[1].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[1].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[1].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[1].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[2].category.coding[0].code, "oral")
        self.assertEqual(inst.insurance[0].benefitBalance[2].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value, 2000)
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[2].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[2].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].code, "F3")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].display, "Dental Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[2].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[2].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[2].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[2].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[2].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[3].category.coding[0].code, "vision")
        self.assertEqual(inst.insurance[0].benefitBalance[3].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.value, 400)
        self.assertEqual(inst.insurance[0].benefitBalance[3].financial[0].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[3].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[3].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].code, "F6")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].display, "Vision Coverage")
        self.assertEqual(inst.insurance[0].benefitBalance[3].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[3].term.coding[0].code, "annual")
        self.assertEqual(inst.insurance[0].benefitBalance[3].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[3].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[3].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.insurance[0].benefitBalance[4].category.coding[0].code, "vision")
        self.assertEqual(inst.insurance[0].benefitBalance[4].category.coding[0].system, "http://hl7.org/fhir/benefit-category")
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[0].allowedString, "shared")
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[0].type.coding[0].code, "room")
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.code, "SAR")
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.system, "urn:iso:std:iso:4217")
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.value, 600)
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[1].type.coding[0].code, "benefit")
        self.assertEqual(inst.insurance[0].benefitBalance[4].network.coding[0].code, "in")
        self.assertEqual(inst.insurance[0].benefitBalance[4].network.coding[0].system, "http://hl7.org/fhir/benefit-network")
        self.assertEqual(inst.insurance[0].benefitBalance[4].subCategory.coding[0].code, "49")
        self.assertEqual(inst.insurance[0].benefitBalance[4].subCategory.coding[0].display, "Hospital Room and Board")
        self.assertEqual(inst.insurance[0].benefitBalance[4].subCategory.coding[0].system, "http://hl7.org/fhir/benefit-subcategory")
        self.assertEqual(inst.insurance[0].benefitBalance[4].term.coding[0].code, "day")
        self.assertEqual(inst.insurance[0].benefitBalance[4].term.coding[0].system, "http://hl7.org/fhir/benefit-term")
        self.assertEqual(inst.insurance[0].benefitBalance[4].unit.coding[0].code, "individual")
        self.assertEqual(inst.insurance[0].benefitBalance[4].unit.coding[0].system, "http://hl7.org/fhir/benefit-unit")
        self.assertEqual(inst.outcome.coding[0].code, "complete")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/remittance-outcome")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEligibilityResponse3(self):
        inst = self.instantiate_from("eligibilityresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse3(inst2)
    
    def implEligibilityResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(inst.disposition, "Eligibiliy request could not be processed, please address errors before submitting.")
        self.assertEqual(inst.error[0].code.coding[0].code, "a001")
        self.assertEqual(inst.error[0].code.coding[0].system, "http://hl7.org/fhir/adjudication-error")
        self.assertEqual(inst.form.coding[0].code, "ELRSP/2017/01")
        self.assertEqual(inst.form.coding[0].system, "http://national.org/form")
        self.assertEqual(inst.id, "E2503")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "8812343")
        self.assertEqual(inst.outcome.coding[0].code, "error")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/remittance-outcome")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")
    
    def testEligibilityResponse4(self):
        inst = self.instantiate_from("eligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse4(inst2)
    
    def implEligibilityResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(inst.disposition, "Policy is currently in-force.")
        self.assertEqual(inst.id, "E2500")
        self.assertEqual(inst.identifier[0].system, "http://www.BenefitsInc.com/fhir/eligibilityresponse")
        self.assertEqual(inst.identifier[0].value, "881234")
        self.assertTrue(inst.inforce)
        self.assertEqual(inst.outcome.coding[0].code, "complete")
        self.assertEqual(inst.outcome.coding[0].system, "http://hl7.org/fhir/remittance-outcome")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.div, "<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>")
        self.assertEqual(inst.text.status, "generated")

