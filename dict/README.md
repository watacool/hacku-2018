## 自分用の辞書作成

### 音素列へのコンパイル：onsoretu_yomi_compile.sh

* 手順
  1. my_dict.yomiを修正
  2. onsoretu_yomi_compile.shでコンパイル

### 構文の定義：grammar_voca_compile.sh

* 手順
  1. my_dict.grammarを修正
  2. my_dict.vocaを修正
  3. grammar_voca_compile.shでコンパイル

### 作成した辞書を指定して実行

* -gramに自分の辞書を指定する
```
$ julius -C ~/julius-4.4.2/julius-kit/dictation-kit-v4.4/am-gmm.jconf -gram ~/hacku-2018/dict/my_dict
```
