import datetime
import json
import uuid

import jwt
import requests
from typing import Annotated
from fastapi import FastAPI, APIRouter, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

from schema import HookDataRequest
from samples import cds_hook_sample
from cds_services.fastapi.fastapi_basic import basic

description = """
TEST CDS HOOK and FASTAPI basic. 🚀

## AUTH

You can **create token**.

## CDS HOOK

You will be able to:
configure the following
* **CDS service** 
* **CDS hooks** .

## Basic FASTAPI CRUD methods
* **Read api**
    * **HTTP: GET**
* **create api**
    * **HTTP: POST**
* **update api**
    * **HTTP: PUT**
    * **HTTP: PATCH**
* **delete api**
    * **HTTP: DELETE**
"""

app = FastAPI(title="CDS HOOK TEST", version="1.0.0", contact={
    "name": "Kavilakshmi",
    "url": "http://www.github.com/kavilakshmi",
    "email": "kavilakshmi.kalidas@ideas2it.com"
},
              description=description,
              )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

auth_token = APIRouter()
cds_hook = APIRouter()


@auth_token.get('/generate_token')
def generate_token():
    # TODO: specify private key path which shared over mail
    private_key = open('../sandbox_test_app/privatekey.pem', 'r').read()
    # TODO: specify client id of your app (client id or non production client id)
    client_id = '4eed3e4d-0692-470e-bae6-cca2a8452429'
    url = "https://fhir.epic.com/interconnect-fhir-oauth/oauth2/token"
    alg = 'RS256'

    headers = {
        'alg': alg,
        'typ': 'JWT'
    }

    payload = {
        'iss': client_id,
        'sub': client_id,
        'aud': url,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
        'jti': str(uuid.uuid4())
    }

    token = jwt.encode(payload, private_key, algorithm=alg, headers=headers)

    payload = f'grant_type=client_credentials&' \
              f'client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type' \
              f'%3Ajwt-bearer&client_assertion={token}'
    headers = {
        'Epic-Client-ID': client_id,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json(), 200


@cds_hook.get('/cds-services')
def cds_services():
    return {
        "services": [
            {
                "hook": "patient-view",
                "title": "Heart disease Service",
                "description": "An example of a CDS Service that returns a static set of cards",
                "id": "heart-patient-greeter",
                "prefetch": {
                    "patientToGreet": "Patient/{{context.patientId}}"
                }
            },
            {
                "hook": "patient-view",
                "title": "PIS Service",
                "description": "An example of a CDS Service that returns a static set of cards",
                "id": "static-patient-greeter",
                "prefetch": {
                    "patient": "Patient/{{context.patientId}}"
                }
            },
            {
                "hook": "medication-prescribe",
                "title": "Medication Echo CDS Service",
                "description": "An example of a CDS Service that simply echos the medication being prescribed",
                "id": "medication-echo",
                "prefetch": {
                    "patient": "Patient/{{context.patientId}}",
                    "medications": "MedicationRequest?patient={{context.patientId}}"
                }
            }
        ]
    }


@cds_hook.post('/cds-services/medication-echo')
def medication_prescribe(hookrequest: Annotated[HookDataRequest, Body(
    example=cds_hook_sample
)]):
    hook_data = json.loads(hookrequest.json())
    print(hook_data)
    return {
        "cards": [
            #     {
            #         "summary": "Example Card",
            #         "indicator": "info",
            #         "detail": "This is an example card.",
            #         "source": {
            #             "label": "Static CDS Service Example",
            #             "url": "https://example.com",
            #             "icon": "https://example.com/img/icon-100px.png"
            #         },
            #         "links": [
            #             {
            #                 "label": "Google",
            #                 "url": "https://google.com",
            #                 "type": "absolute"
            #             },
            #             {
            #                 "label": "Github",
            #                 "url": "https://github.com",
            #                 "type": "absolute"
            #             },
            #             {
            #                 "label": "SMART Example App",
            #                 "url": "https://smart.example.com/launch",
            #                 "type": "smart",
            #                 "appContext": "{\"session\":3456356,\"settings\":{\"module\":4235}}"
            #             }
            #         ]
            #     },
            #     {
            #         "summary": "Another card",
            #         "indicator": "warning",
            #         "source": {
            #             "label": "Static CDS Service Example"
            #         }
            #     }
        ]
    }
    # return { "cards": [ { "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60", "summary": f"Now seeing: Test CDS for
    # Patient - {' '.join(hook_data['prefetch']['patient']['name'][0]['given'])}", "source": { "label": "TEST CDS
    # SERVICES" }, "indicator": "warning", "detail": "Patient has a history of test", "suggestions": [ { "label":
    # "test suggestion", 'uuid': "3333eabe-e5a6-4942-8b01-eadf3f660a6f", "actions": [ { 'type': 'delete',
    # "description": "Test", "resource": { "resourceType": "MedicationRequest" } }]
    #
    #                 }
    #             ]
    #         },
    #         {
    #             "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a61",
    #             "summary": "Now seeing: Test CDS",
    #             "source": {
    #                 "label": "TEST CDS SERVICES"
    #             },
    #             "indicator": "critical",
    #             "detail": "Patient has a history of test",
    #             "links": [
    #                 {
    #                     "label": "test link",
    #                     'url': "https://ideas2it.com",
    #                     "type": 'absolute'
    #                 },
    #                 {
    #                     "label": "test link2",
    #                     'url': "https://example.com/launch",
    #                     "type": 'smart'
    #                 }
    #
    #             ]
    #         }
    #     ]
    # }
    #


@cds_hook.post('/cds-services/static-patient-greeter')
def patient_view2(hookrequest: Annotated[HookDataRequest, Body(
    example=cds_hook_sample
)]):
    hook_data = json.loads(hookrequest.json())
    return {
        "cards": [
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60",
                "summary": f"Now seeing: Test CDS for Patient - "
                           f"{' '.join(hook_data['prefetch']['patient']['name'][0]['given'])}",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "warning",
                "detail": "Patient has a history of test",
                "suggestions": [
                    {
                        "label": "test suggestion",
                        'uuid': "3333eabe-e5a6-4942-8b01-eadf3f660a6f",
                        "actions": [
                            {
                                'type': 'delete',
                                "description": "Test",
                                "resource": {
                                    "resourceType": "MedicationRequest"
                                }
                            }]

                    }
                ]
            },
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a61",
                "summary": "Now seeing: Test CDS",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "critical",
                "detail": "Patient has a history of test",
                "links": [
                    {
                        "label": "test link",
                        'url': "https://ideas2it.com",
                        "type": 'absolute'
                    },
                    {
                        "label": "test link2",
                        'url': "https://example.com/launch",
                        "type": 'smart'
                    }

                ]
            }
        ]
    }


@cds_hook.post('/cds-services/heart-patient-greeter')
def patient_view(hookrequest: Annotated[HookDataRequest, Body(
    example=cds_hook_sample
)]):
    # load request data
    hook_data = json.loads(hookrequest.json())

    return {
        "cards": [
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60",
                "summary": f"Now seeing: Test CDS for Patient -"
                           f" {' '.join(hook_data['prefetch']['patientToGreet']['name'][0]['given'])}",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "warning",
                "detail": "Patient has a history of test",
                "suggestions": [
                    {
                        "label": "test suggestion",
                        'uuid': "3333eabe-e5a6-4942-8b01-eadf3f660a6f",
                        "actions": [
                            {
                                'type': 'delete',
                                "description": "Test",
                                "resource": {
                                    "resourceType": "MedicationRequest"
                                }
                            }]

                    }
                ]
            },
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a61",
                "summary": "Now seeing: Test CDS",
                "source": {
                    "label": "TEST CDS SERVICES"
                },
                "indicator": "critical",
                "detail": "Patient has a history of test",
                "links": [
                    {
                        "label": "test link",
                        'url': "https://ideas2it.com",
                        "type": 'absolute'
                    },
                    {
                        "label": "test link2",
                        'url': "https://example.com/launch",
                        "type": 'smart'
                    }

                ]
            }
        ]
    }


@cds_hook.post('/cds-services/cme-ster/feedback')
def feedback():
    return {"feedback": [{
        "card": "123456",
        "outcome": "overridden",
        "outcomeTimestamp": "2022-05-19T19:44:04Z",
        "overrideReasons": {
            "reason": {
                "code": "contraindicated",
                "display": "bad",
                "system": "http: //example.org/cds-services/fhir/CodeSystem/override-reasons"
            },
            "userComment": "User Entered Free Text"}}]}


@app.get('/')
def redirect_to_docs():
    return RedirectResponse('http://localhost:8000/docs')


app.include_router(basic, tags=['Basic CRUD'])
app.include_router(auth_token, prefix="/fhir", tags=["Auth"])
app.include_router(cds_hook, tags=['CDS-HOOK'])
