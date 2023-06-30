import requests
import jwt
import datetime
import uuid

from flask_cors import CORS, cross_origin
from flask import Flask, request

app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'


@app.route('/generate_token')
def generate_token():
    # TODO: specify private key path which shared over mail
    private_key = open('sandbox_test_app/privatekey.pem', 'r').read()
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

    payload = f'grant_type=client_credentials&client_assertion_type=urn%3Aietf%3Aparams%3Aoauth%3Aclient-assertion-type' \
              f'%3Ajwt-bearer&client_assertion={token}'
    headers = {
        'Epic-Client-ID': client_id,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.post(url, headers=headers, data=payload)

    return response.json(), 200


@app.route('/cds-services')
@cross_origin()
def cds_services():
    return {
        "services": [{
            "hook": "patient-view",
            "name": "CME-ster",
            "description": "hshv",
            "id": "cme-ster",
            "prefetch": {
                "patient": "Patient/{{context.patientId}}",
                "condition": "Condition?patient={{context.patientId}}",
                "observation": "Observation?patient={{context.patientId}}"
            }
        },
            {
                "id": "cms-price-check-lh",
                "title": "CMS Pricing Service",
                "description": "Determine if an authored prescription has a cheaper alternative to switch to and display pricing",
                "hook": "order-select"
            }

        ]
    }


@app.route('/cds-services/cme-ster', methods=['POST'])
@cross_origin()
def patient_view():
    hook_data = request.get_json()
    print(hook_data)
    return {
        "cards": [
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60",
                "summary": f"Now seeing: Test CDS for Patient - {' '.join(hook_data['prefetch']['patient']['name'][0]['given'])}",
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


@app.route('/cds-services/cms-price-check-lh', methods=['POST'])
@cross_origin()
def cms_price_check():
    hook_data = request.get_json()
    print(hook_data)
    details = ""
    if "reasonCodeableConcept" in hook_data['context']['draftOrders']['entry'][0]['resource']:
        details = f" - **Treating** - {hook_data['context']['draftOrders']['entry'][0]['resource']['reasonCodeableConcept']['text']}"

    return {
        "cards": [
            {
                "uuid": "3333eabe-e5a6-4942-8b01-eadf3f660a60",
                "summary": f"Order Select: Test CDS",
                "source": {
                    "label": "TEST CDS SERVICES- Order Select"
                },
                "indicator": "info",
                "detail": f" - An example order select hook \n\n"
                          f"** -- Details**\n - Medication Order ID --> ** {hook_data['context']['draftOrders']['entry'][0]['resource']['id']}**\n\n"
                          f"** -- Draft Orders**\n - **Status** - {hook_data['context']['draftOrders']['entry'][0]['resource']['status']}\n\n"
                          f"{details if details else ''}\n\n"
                          f" - **Date Written** - {hook_data['context']['draftOrders']['entry'][0]['resource']['dateWritten']}",
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
            }
        ]
    }


@app.route('/cds-services/cme-ster/feedback', methods=['POST'])
@cross_origin()
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
