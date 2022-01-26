import gpt_2_simple as gpt2
from dotenv import dotenv_values
from discord_webhook import DiscordWebhook
import requests
import json

DISCORD_URL = dotenv_values('.env')['DISCORD_URL']
LINKEDIN_ORG_ID = dotenv_values('.env')['LINKEDIN_ORG_ID']
LINKEDIN_TOKEN = dotenv_values('.env')['LINKEDIN_TOKEN']

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

response = gpt2.generate(sess, temperature=1.2, return_as_list=True)[0]

response_list = response.split('\n')
truncate_response = response_list[:15]
str_response = ' \n'.join([str(elem).lstrip('<|startoftext|>').rstrip('<|endoftext|>') for elem in truncate_response if elem])
message_of_the_day = max(truncate_response, key=len).lstrip('<|startoftext|>').rstrip('<|endoftext|>')

data = {
  "content": {
      "contentEntities": [
          {
              "entityLocation": "https://www.ubeshi.com"
          }
      ]
  },
  "distribution": {
      "linkedInDistributionTarget": {}
  },
  "owner": "urn:li:organization:{}".format(LINKEDIN_ORG_ID),
  "subject": "{}".format(message_of_the_day),
  "text": {
      "text": "{} \n#ubeshi #gpt2".format(message_of_the_day)
  }
}

json_data = json.dumps(data)

linkedin_resp = requests.post(
  'https://api.linkedin.com/v2/shares',
  data = json_data,
  headers = {
    'Authorization': 'Bearer {}'.format(LINKEDIN_TOKEN),
    'Content-Type': 'application/json',
  }
)
webhook = DiscordWebhook(url=DISCORD_URL, content='Good morning! Here\'s our post for today 😗: \n```' + message_of_the_day + '```\n')
response = webhook.execute()

webhook = DiscordWebhook(url=DISCORD_URL, content='And here\'s the content that didn\'t make the cut: \n```' + str_response + '```\n')
response = webhook.execute()
