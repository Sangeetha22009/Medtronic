from enum import Enum
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class FhirAuthorization(BaseModel):
    access_token: str
    token_type: str
    scope: str
    subject: str


class HookDataRequest(BaseModel):
    hookInstance: str
    hook: str
    fhirServer: str
    context: dict
    fhirAuthorization: FhirAuthorization
    prefetch: dict

    class Config:
        schema_extra = {"hookInstance": "Gfa77owlmQmCncYQxTXYdNpseEjPLwLKlw4FjPDBNE1dPKWdmg6bRG9DPKhTxwHj",
                        "hook": "patient-view",
                        "fhirServer": "https://api.logicahealth.org/PISsystem/data",
                        "context": {"userId": "Practitioner/practitioner01", "patientId": "patient02"},
                        "fhirAuthorization": {"access_token": "sample_jwt_token", "token_type": "Bearer",
                                              "scope": "patient/*.read user/*.read", "subject": "patient-view"},
                        "prefetch": {"patient": {"resourceType": "Patient", "id": "patient02",
                                                 "meta": {"versionId": "1",
                                                          "lastUpdated": "2023-05-30T12:10:46.000+00:00",
                                                          "source": "#h5OwFlWs2krkDXb6", "profile": [
                                                         "http://fhir.de/StructureDefinition/patient-de-basis/0.2"]},
                                                 "text": {"status": "generated",
                                                          "div": "<div xmlns=\"http://www.w3.org/1999/xhtml\"><div class=\"hapiHeaderText\">Sophie <b>EICHEL </b></div><table class=\"hapiPropertyTable\"><tbody><tr><td>Identifier</td><td>G632949382</td></tr><tr><td>Address</td><td><span>Jenaer Strasse 65 </span><br/><span>Mülheim an der Ruhr </span><span>DE-NW </span><span>DEU </span></td></tr><tr><td>Date of birth</td><td><span>23 July 1975</span></td></tr></tbody></table></div>"},
                                                 "identifier": [{"system": "http://fhir.de/NamingSystem/gkv/kvid-10",
                                                                 "value": "G632949382"}], "active": True,
                                                 "name": [{"use": "official", "family": "Eichel", "given": ["Sophie"]}],
                                                 "gender": "female", "birthDate": "1975-07-23", "address": [
                                {"use": "home", "line": ["Jenaer Strasse 65"], "city": "Mülheim an der Ruhr",
                                 "state": "DE-NW", "postalCode": "45470", "country": "DEU"}]}}}




class InputesController(Enum):
    inprogress: str = "InProgress"
    running: str = "Running"
    aborted: str = "Aborted"
    cancelled: str = "Cancelled"
    completed: str = "Completed"


class OutputesController(BaseModel):
    id: int = 0
    status: str = ""
    comment: str = ""


class Output(BaseModel):
    data: list[OutputesController] = []


class UpdateController(BaseModel):
    id: int = 0
    status: str = ""

class DeleteController(BaseModel):

    status: str = ""
    message: str = ""

