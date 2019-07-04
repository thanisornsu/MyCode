import requests


url = "https://chat-public.one.th:8034/api/v1/push_message"

payload = "{\n    \"to\" : \"U4aad93bda1605f489caf5ca87b129e64\",\n \
   \"bot_id\" : \"B54c5474b368b5eba88bc9559c083ada2\",\n    \"type\" : \"text\",\n    \"message\" : \"Hello world!!\"\n  }"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Bearer A31e127557d215875b9af0638989acc8e5b643c3162ea4ad3b2ed903b05b53c7003b4e78672594eeebda5529d09a2c55d",
    'Postman-Token': "bc59b6a3-a9b0-4d06-8cab-27c640cb034d,bd68125d-0b83-46bb-a3eb-adb489d6ee86",
    'Host': "chat-public.one.th:8034",
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)

if "status" in response.text:
    print("i see ")