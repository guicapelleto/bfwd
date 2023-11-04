import sys
import urllib3
import os
import random
import base64
from colorama import Fore, Style

sys.tracebacklimit = 0

color = {
    '1': Fore.GREEN,
    '2': Fore.BLUE,
    '3': Fore.RED,
    '4': Fore.LIGHTGREEN_EX,
    '5': Fore.LIGHTBLUE_EX,
    '6': Fore.LIGHTRED_EX
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def printer(text):
    r = random.randint(1, 6)
    print(color[str(r)] + text, Style.RESET_ALL)

class webchecker():

    user_agent = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47"}
    http_pool = urllib3.PoolManager()

    def __init__(self, wordlist, domain):
        self.wordlist = open(wordlist).read().split()
        self.domain = domain

    def check_web_folder(self, folder):
        self.current_folder = self.domain + '/' + folder
        return self.http_pool.request('GET', self.current_folder, headers= self.user_agent).status

    def brute_force(self):
        for folder in self.wordlist:
            if self.check_web_folder(folder) == 200:
                printer(self.current_folder)


def decode_b64(code):
    enc_msg = base64.b64decode(code)
    msg = enc_msg.decode('ascii')
    return msg


def call_banner():
    banner = b'ICAgICAgICAgICAgICAgICAgICAgICAgIAogX19fX18gX19fX18gXyBfIF8gX19fXyAgCnwgX18gIHwgICBfX3wgfCB8IHwgICAgXCAKfCBfXyAtfCAgIF9ffCB8IHwgfCAgfCAgfAp8X19fX198X198ICB8X19fX198X19fXy8gCiAgICAgICAgICAgICAgICAgICAgICAgICA='
    banner = decode_b64(banner)
    printer(banner)
    printer('Bruteforce Web dir, by: guicapelleto\n\n')
    usage = '\nUsage:\npython bfwd.py path/to/wordlist domain_to_bruteforce.com\n'
    help = '\nBruteforce Web Dir works with an authentic user agent (Windows 10, edge), bypassing many requests filters.\n\n'
    if '--help' in sys.argv:
        sys.exit(help)
    try:
        wordlist = sys.argv[1]
    except:
        help = '\nNo wordlist in args\n'
        sys.exit(help + usage)
    try:
        domain = sys.argv[2]
    except:
        help = '\nNo domain in args\n'
        sys.exit(help + usage)

    return wordlist, domain

def main():
    clear_terminal()
    wordlist, domain = call_banner()
    checker = webchecker(wordlist, domain)
    checker.brute_force()
    printer('')


main()