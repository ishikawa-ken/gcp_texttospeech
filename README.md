# gcp_texttospeech
---

**仮想環境に入ること**

## **アクションサーバ**
---

```
$ rosrun gcp_texttospeech tts_actionserver.py
```

使い方

```[python:actionserver]
tts_pub = actionlib.SimpleActionClient('gcp_texttospeech', gcp_texttospeech.msg.TTSAction)
```


## **サービス通信**
---

```
$ rosrun gcp_texttospeech tts_stdserver.py
```

使い方

```[python:stdserver]
tts_pub = rospy.ServiceProxy('/tts', TTS)
```



## 説明
---

発話部分を直接呼び出さず関数化することをおすすめします
```[python:srvの例]
from gcp_texttospeech.srv import *

class hogehoge(object):   #クラス名をTTSにしないこと
  def __init__(self):
      self.tts_pub = rospy.ServiceProxy('/tts', TTS)

  def speak(self, sentence):
      self.tts_pub(sentence)
```
