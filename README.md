# Honey, I'm home!

Always too drunk to text your girlfriend that you got home safe?

This tool will send a message via telegram, once your mobile phone is detected in your wifi network after a couple of hours.

# Setup

## General

- Install Python 3.7 or higher.
- Run ``pip install -r <PROJECT_ROOT>/requirements.txt`` on a command line.
- You need to find out the MAC address of your phone (or any other device). At usual, this device should be in the same network as the host which runs this application.

## Telegram bot

- Use Telegram's bot ``BotFather`` to create a bot: https://t.me/botfather
- Follow the instructions given by ``BotFather`` and copy the created bot token to a safe place.
- Send the message ``\help`` to ``BotFather`` to check which possibilities of configuration you have.
- Enable the setting ``\setjoingroups``.
- Create a private Telegram group and add your new bot to the group. Important step!
- Find out what's your chat id of the Telegram group. A helper script is placed under ``tools``:
    ```bash
    python tools/get_chat_id.py -t <YOUR_TOKEN> -g <YOUR_GROUP_NAME>
    ```
- As a last step, create a config file in folder ``notification`` named ``config.json``:
    ```json
    {
      "bot_token": "place your token here.",
      "bot_chat_id": "place your chat id here."
    }
    ```

## Device detection script

Run ``python <PROJECT_ROOT>/phone_detection.py`` on a command line. You have the following command line options:

|Argument|Description|Required|Default|
|---|---|---|---|
|-d / --device|The mac address of the device.|Yes|None|
|-a / --absence|Send a message when a device is detected that was last seen x minutes ago.|No|60|
|-s / --scan-interval|Interval in minutes that indicates how often a device search is performed.|No|1|
