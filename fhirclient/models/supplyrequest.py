#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.9.0.10959 (http://hl7.org/fhir/StructureDefinition/SupplyRequest) on 2017-02-01.
#  2017, SMART Health IT.


from . import domainresource

class SupplyRequest(domainresource.DomainResource):
    """ Request for a medication, substance or device.
    
    A record of a request for a medication, substance or device used in the
    healthcare setting.
    """
    
    resource_type = "SupplyRequest"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.date = None
        """ When the request was made.
        Type `FHIRDate` (represented as `str` in JSON). """
        
        self.from_fhir = None
        """ The origin of the supply.
        Type `FHIRReference` referencing `Organization, Location` (represented as `dict` in JSON). """
        
        self.identifier = None
        """ Unique identifier.
        Type `Identifier` (represented as `dict` in JSON). """
        
        self.kind = None
        """ The kind of supply (central, non-stock, etc.).
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderedItemCodeableConcept = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.orderedItemReference = None
        """ Medication, Substance, or Device requested to be supplied.
        Type `FHIRReference` referencing `Medication, Substance, Device` (represented as `dict` in JSON). """
        
        self.patient = None
        """ Patient for whom the item is supplied.
        Type `FHIRReference` referencing `Patient` (represented as `dict` in JSON). """
        
        self.reasonCodeableConcept = None
        """ Why the supply item was requested.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.reasonReference = None
        """ Why the supply item was requested.
        Type `FHIRReference` referencing `Resource` (represented as `dict` in JSON). """
        
        self.source = None
        """ Who initiated this order.
        Type `FHIRReference` referencing `Practitioner, Organization, Patient` (represented as `dict` in JSON). """
        
        self.status = None
        """ requested | completed | failed | cancelled | entered-in-error.
        Type `str`. """
        
        self.supplier = None
        """ Who is intended to fulfill the request.
        List of `FHIRReference` items referencing `Organization` (represented as `dict` in JSON). """
        
        self.to = None
        """ The destination of the supply.
        Type `FHIRReference` referencing `Organization, Location, Patient` (represented as `dict` in JSON). """
        
        self.when = None
        """ When the request should be fulfilled.
        Type `SupplyRequestWhen` (represented as `dict` in JSON). """
        
        super(SupplyRequest, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequest, self).elementProperties()
        js.extend([
            ("date", "date", fhirdate.FHIRDate, False, None, False),
            ("from_fhir", "from", fhirreference.FHIRReference, False, None, False),
            ("identifier", "identifier", identifier.Identifier, False, None, False),
            ("kind", "kind", codeableconcept.CodeableConcept, False, None, False),
            ("orderedItemCodeableConcept", "orderedItemCodeableConcept", codeableconcept.CodeableConcept, False, "orderedItem", False),
            ("orderedItemReference", "orderedItemReference", fhirreference.FHIRReference, False, "orderedItem", False),
            ("patient", "patient", fhirreference.FHIRReference, False, None, False),
            ("reasonCodeableConcept", "reasonCodeableConcept", codeableconcept.CodeableConcept, False, "reason", False),
            ("reasonReference", "reasonReference", fhirreference.FHIRReference, False, "reason", False),
            ("source", "source", fhirreference.FHIRReference, False, None, False),
            ("status", "status", str, False, None, False),
            ("supplier", "supplier", fhirreference.FHIRReference, True, None, False),
            ("to", "to", fhirreference.FHIRReference, False, None, False),
            ("when", "when", SupplyRequestWhen, False, None, False),
        ])
        return js


from . import backboneelement

class SupplyRequestWhen(backboneelement.BackboneElement):
    """ When the request should be fulfilled.
    """
    
    resource_type = "SupplyRequestWhen"
    
    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.
        
        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """
        
        self.code = None
        """ Fulfilment code.
        Type `CodeableConcept` (represented as `dict` in JSON). """
        
        self.schedule = None
        """ Formal fulfillment schedule.
        Type `Timing` (represented as `dict` in JSON). """
        
        super(SupplyRequestWhen, self).__init__(jsondict=jsondict, strict=strict)
    
    def elementProperties(self):
        js = super(SupplyRequestWhen, self).elementProperties()
        js.extend([
            ("code", "code", codeableconcept.CodeableConcept, False, None, False),
            ("schedule", "schedule", timing.Timing, False, None, False),
        ])
        return js


from . import codeableconcept
from . import fhirdate
from . import fhirreference
from . import identifier
from . import timing
