# Natsume/棗

## Introduction

Natsume is a toolkit for Japanese text frontend processing. It is based on the open source project [Open Jtalk](https://open-jtalk.sourceforge.net/) and has the following
features:

- Doesn't use full-context labels for simplicity and accuracy.
- Supports morphological analysis using [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic).

## Platforms

- Mac OS
- Linux

## Dependencies

- CMake
- C/C++ compilers
- Cython
- [MeCab](https://taku910.github.io/mecab/)
- [fugashi](https://github.com/polm/fugashi)

## Installation

```bash
pip install natsume
```

## Usage

### Grapheme-to-Phoneme

```python
from natsume import Natsume

nat = Natsume()

text = "天気がいいから、散歩しましょう。"
```

```python
# romaji
phonemes = nat.g2p(text, phoneme_mode="romaji", token_mode="phrase")
# ipa
phonemes = nat.g2p(text, phoneme_mode="ipa", token_mode="phrase")
# romaji with accent
phonemes = nat.g2p(text, phoneme_mode="romaji", token_mode="phrase", with_accent=True)

print(" ".join(phonemes))
```

```bash
# romaji
teNkiga iikara , saNpo shimasho: .
# ipa
teNkiga iikaɾa , saNpo ɕimaɕo: .
# romaji with accent
teꜜNkiga iꜜikara , saꜛNpo shiꜛmashoꜜ: .
```

### Tokenization

```python
# word
tokens = nat.tokenize(text, mode="word")
# (accent) phrase
tokens = nat.tokenize(text, mode="phrase")

tokens = [token.surface() for token in tokens]
print(" ".join(tokens))
```

```bash
# word
天気 が いい から 、 散歩 し ましょ う 。
# (accent) phrase
天気が いいから 、 散歩 しましょう 。
```

### Intermediate Features

**MeCab**
```python
mecab_features = nat.get_mecab_features(text)

for mecab_feature in mecab_features:
    surface = mecab_feature["surface"]
    feature_string = ",".join(list(mecab_feature.values())[1:])
    print("{}\t{}".format(surface, feature_string))
```

```bash
天気	名詞,一般,*,*,*,*,天気,テンキ,テンキ,1/3,C1
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ,0/1,名詞%F1
いい	形容詞,自立,*,*,形容詞・アウオ段,基本形,いい,イイ,イイ,1/2,*
から	助詞,接続助詞,*,*,*,*,から,カラ,カラ,2/2,動詞%F2@0/形容詞%F2@0
、	記号,読点,*,*,*,*,、,、,、,*/*,*
散歩	名詞,サ変接続,*,*,*,*,散歩,サンポ,サンポ,0/3,C2
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ,0/1,*
ましょ	助動詞,*,*,*,特殊・マス,未然ウ接続,ます,マショ,マショ,2/2,動詞%F4@2/助詞%F2@2
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ウ,0/1,動詞%F1/特殊助動詞%F2@0
。	記号,句点,*,*,*,*,。,。,。,*/*,*
```

**NJD**

```python
njd_features = nat.get_njd_features(text)

for njd_feature in njd_features:
    surface = njd_feature["string"]
    feats = [str(feat) for feat in list(njd_feature.values())[1:]]
    feature_string = ",".join(feats)
    print("{}\t{}".format(surface, feature_string))
```

```bash
天気	名詞,一般,*,*,*,*,天気,テンキ,テンキ,1,3,C1,-1
が	助詞,格助詞,一般,*,*,*,が,ガ,ガ,0,1,名詞%F1,1
いい	形容詞,自立,*,*,形容詞・アウオ段,基本形,いい,イイ,イイ,1,2,*,0
から	助詞,接続助詞,*,*,*,*,から,カラ,カラ,2,2,動詞%F2@0/形容詞%F2@0,1
、	記号,読点,*,*,*,*,、,、,、,0,0,*,0
散歩	名詞,サ変接続,*,*,*,*,散歩,サンポ,サンポ,0,3,C2,0
し	動詞,自立,*,*,サ変・スル,連用形,する,シ,シ,3,1,*,0
ましょ	助動詞,*,*,*,特殊・マス,未然ウ接続,ます,マショ,マショ,2,2,動詞%F4@2/助詞%F2@2,1
う	助動詞,*,*,*,不変化型,基本形,う,ウ,ー,0,1,動詞%F1/特殊助動詞%F2@0,1
。	記号,句点,*,*,*,*,。,。,。,0,0,*,0
```

## Demos

### Text-to-speech

- [四季夏目语音合成v2](https://www.bilibili.com/video/BV1Zw411U7Yf/)

## LICENSE

- natsume: [Apache 2.0 license](https://github.com/faruzan0820/natsume/blob/main/LICENSE)
- fugashi: [MIT license](https://github.com/polm/fugashi/blob/master/LICENSE)
- pyopenjtalk: [MIT license](https://github.com/r9y9/pyopenjtalk/blob/master/LICENSE.md)
- OpenJTalk: [Modified BSD license](https://github.com/r9y9/open_jtalk/blob/1.10/src/COPYING)
- marine: [Apache 2.0 license](https://github.com/6gsn/marine/blob/main/LICENSE)


## References

- [OpenJTalk](https://open-jtalk.sourceforge.net/)
- [pyopenjtalk](https://github.com/r9y9/pyopenjtalk)
- [fugashi](https://github.com/polm/fugashi)
- [tdmelodic](https://github.com/PKSHATechnology-Research/tdmelodic)
- [tdmelodic_openjtalk](https://github.com/sarulab-speech/tdmelodic_openjtalk)
- [単語の追加方法](https://github.com/sarulab-speech/tdmelodic_openjtalk)
- [marine](https://github.com/6gsn/marine)
- [OpenJTalkの解析資料](https://www.negi.moe/negitalk/openjtalk.html)
- [Wikipedia: Hiragana](https://en.wikipedia.org/wiki/Hiragana)
- [新旧字体対照表](https://hagitaka.work/wp-content/uploads/2021/07/%E6%96%B0%E6%97%A7%E5%AD%97%E4%BD%93%E5%AF%BE%E7%85%A7%E8%A1%A8-1.pdf)
