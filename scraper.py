import twint
import os
import glob
import pandas as pd

username = [
  "Recode", "TechCrunch", "VentureBeat", "GVteam", "Accel", "FastCompany", "Entrepreneur", "Inc", "SocialWiz", "cactussky",
  "FastCoDesign", "TechstarsMTL", "motivational", "mindshiftkqed", "biz_motivation", "smartinsights", "thinkproductive", "evernote",
  "gptw_uk", "killerstartups", "alltopstartups", "StartUpMindset", "pickthebrain", "remezsasson", "addictd2success", "officevibe",
  "TLNT_com", "wrike", "sagegroupplc", "aloproductivity", "gtdtimes", "askmikewilliams", "gtdintheuk", "asianefficiency", "productivityist",
  "todoist", "99u", "nesta_uk", "ceoblognation", "startupnation", "startupideabot", "StartupNewsIND", "smallbiztrends", "ducttape", "moo",
  "workwiseuk", "wazokuhq", "positivenewsuk", "markmcguinness", "crowdfunderuk", "teamcrunch", "vistageuk", "gingkoapp", "prowesshq",
  "watc_updates", "WorqIQ", "go_on_uk", "alexkjerulf", "happinessindex", "mindhacksblog", "lifehacker", "wisebread", "fruitfuloffice",
  "superofficeuk", "EdSurge", "Getting_Smart"
]

def ai(user):
  c = twint.Config()
  c.Username = user
  c.Custom["tweet"] = ["tweet"]
  c.Store_csv = True
  c.Output = f'tweets/{user}.csv'
  c.Limit = 10000
  c.Hide_output = True
  print(user)
  twint.run.Search(c)

for users in username:
  ai(users)
extension = 'csv'
all_filenames = [i for i in glob.glob('tweets/*.{}'.format(extension))]

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])

# export to csv
combined_csv.to_csv( "tweets/tweetstmp.csv", index=False, encoding='utf-8-sig')