from binance.client import Client



class Connection:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def connection(self):
        api_key = 'ZdALDrmOIrO8udP9eohld8iiW7wCWUVvE4giKOfc7uVO0OevAmBG3aEUM3n8w35N'
        api_secret = 'BgDuuRchRE7cubNZ9yPGIsL6cW1dyySPeLfNo3BYlUGOvCmRmIDDXTVx3C3CnxMa'
        try:
         connect = Client(api_key, api_secret)
         print(connect, "This is")
         return connect
        except:
           return None