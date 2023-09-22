import requests

class RevoltBots(object):
    def __init__(self, servers: int, *, ApiKey: str, botId: str = None, userId: str = None):
        self.servers = servers
        self.ApiKey = ApiKey
        self.botId = botId
        self.userId = userId

    def postStats(self):
        try:
            headers = {
                'authorization': self.ApiKey,
                'server_count': self.servers
            }
            path = 'https://revoltbots.org/api/v1/bots/stats'
            response = requests.post(path, timeout=10, headers=headers)

            if response.status_code == 200:
                 return (response.json())
            else:
                return response.json()
        except requests.Timeout:
            return ("No such endpoint exists or the API is down!")
        
    def getStats(self):
        try:
            path = ('https://revoltbots.org/api/v1/bots/{}', self.botId)
            response = requests.get(path, timeout=10)
            if response.status_code == 200:
                 return (response.json())
            else:
                return response.json()
        except requests.Timeout:
            return ("No such endpoint exists or the API is down!")
        
    def checkVoter(self):
        try:
            path = ('https://revoltbots.org/api/v1/bots/{}/votes?user={}', (self.botId, self.userId))
            response = requests.get(path, timeout=10)
            if response.status_code == 200:
                 return (response.json())
            else:
                return response.json()
        except requests.Timeout:
            return ("No such endpoint exists or the API is down!")

    def checkVotes(self):
        try:
            path = ('https://revoltbots.org/api/v1/bots/{}/votes', self.botId)
            response = requests.get(path, timeout=10)
            if response.status_code == 200:
                 return (response.json())
            else:
                return response.json()
        except requests.Timeout:
            return ("No such endpoint exists or the API is down!")