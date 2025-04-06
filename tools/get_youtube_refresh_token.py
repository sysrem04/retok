from google_auth_oauthlib.flow import InstalledAppFlow
import os

def get_refresh_token():
    client_secret_file = 'tools/client_secret.json'
    scopes = ["https://www.googleapis.com/auth/youtube.upload"]

    flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, scopes=scopes)
    creds = flow.run_local_server(port=8080, open_browser=False)

    with open("refresh_token.txt", "w") as token_file:
        token_file.write(creds.refresh_token)

    print("Refresh token saved to refresh_token.txt")

if __name__ == "__main__":
    get_refresh_token()
