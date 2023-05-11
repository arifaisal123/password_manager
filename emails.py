from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
subject = "from the Python SDK!"
sender = {"name":"Sendinblue","email":"contact@sendinblue.com"}
replyTo = {"name":"Sendinblue","email":"contact@sendinblue.com"}
html_content = "<html><body><h1>Checking mail </h1></body></html>"
to = [{"email":"arifaisal123@gmail.com","name":"Jane Doe"}]
params = {"parameter":"My param value","subject":"New Subject"}
send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)

try:
    api_response = api_instance.send_transac_email(send_smtp_email)
    print(api_response)
except ApiException as e:
    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)