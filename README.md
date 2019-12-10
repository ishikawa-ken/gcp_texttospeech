# gcp_texttospeech

**仮想環境に入ること**

## **アクションサーバ**

```
$ rosrun gcp_texttospeech tts_actionserver.py
```

使い方

```python
tts_pub = actionlib.SimpleActionClient('gcp_texttospeech', gcp_texttospeech.msg.TTSAction)
```


## **サービス通信**

```
$ rosrun gcp_texttospeech tts_srvserver.py
```

使い方

```python
tts_pub = rospy.ServiceProxy('/tts', TTS)
```



## その他

発話部分を直接呼び出さず関数化することをおすすめします

例：
```python
from gcp_texttospeech.srv import *

class hogehoge(object):   #クラス名をTTSにしないこと
  def __init__(self):
      self.tts_pub = rospy.ServiceProxy('/tts', TTS)

  def speak(self, sentence):
      self.tts_pub(sentence)
```
