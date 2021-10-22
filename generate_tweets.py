import gpt_2_simple as gpt2
from dotenv import dotenv_values
from discord_webhook import DiscordWebhook

DISCORD_URL = dotenv_values('.env')['DISCORD_URL']

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

response = gpt2.generate(sess, temperature=1.0, return_as_list=True)[0]

response_list = response.split('\n')
truncate_response = response_list[:5]
str_response = ' \n'.join([str(elem).lstrip('<|startoftext|>').rstrip('<|endoftext|>') for elem in truncate_response if elem])
webhook = DiscordWebhook(url=DISCORD_URL, content='Good morning! Here\'s some content for you today 😗: \n```' + str_response + '```')
response = webhook.execute()