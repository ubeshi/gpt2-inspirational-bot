@ECHO OFF 
TITLE Execute python script on anaconda environment
ECHO Please Wait...
:: Section 1: Activate the environment.
ECHO ============================
ECHO Conda Activate
ECHO ============================
@CALL "C:\Users\DevUser\anaconda3\Scripts\activate.bat" tf-gpu2
:: Section 2: Execute python script.
ECHO ============================
ECHO Python generate_tweets.py
ECHO ============================
python C:\Users\DevUser\Documents\GitHub\gpt2-inspirational-bot\generate_tweets.py

ECHO ============================
ECHO End
ECHO ============================

PAUSE
