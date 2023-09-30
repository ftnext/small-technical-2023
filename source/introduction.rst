:og:description: XP祭り2023「小さなテクニカルプラクティスのワークショップ」はじめに

==============================
ようこそ！
==============================

*小さいは、正義！*

`プロポーザル <https://confengine.com/conferences/xp2023/proposal/18830>`__ より

    本ワークショップでは、この（引用注: サークルオブライフの）うちのテクニカルプラクティス（特にテスト駆動開発とリファクタリング）にフォーカスします。

    キーワードは「小さい」です。
    達人のテスト駆動開発やリファクタリングは小さいステップをたくさん実行します。

小さなテクニカルプラクティスを体験して行ってください！
ワークショップ中はお気軽にちょっとしたことでもぜひアウトプットください（私の講義というよりも、 **みんなで学ぶ場** にしましょう！）

* 参加者自己紹介

  * 読んでほしいお名前（+名札）
  * 普段使っている言語

* 簡単なチェックイン（今の気持ち）

==============================
環境構築
==============================

前提：Pythonの環境が構築されている

VS Code 拡張
==============================

* `Python <https://marketplace.visualstudio.com/items?itemName=ms-python.python>`__
* `Black Formatter <https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter>`__

拡張を設定する :file:`settings.json` はこのワークショップのリポジトリにコミット済みです。  
（🐛リポジトリをcloneした場合はsettings.jsonを参照して動くと思いますが、Codespacesではsettings.jsonを参照する形で動かせていません）

ワークショップ中にCodespaceの環境に入るために

* `Live Share <https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare>`__

Pythonのテスト環境
==============================

.. code-block:: shell

    $ cd examples
    $ # codespacesでない場合は、ここで仮想環境を作ってください（以下コマンド例）
    $ # python3 -m venv venv --upgrade-deps
    $ # source venv/bin/activate
    $ pip install -r requirements.in

インストールされるライブラリ

* `pytest <https://docs.pytest.org/en/latest/>`__

  * テストライブラリ
  * Pythonの標準ライブラリにもテストライブラリはありますが、デファクトスタンダード感のあるpytestを採用しました

* `pytest-randomly <https://pypi.org/project/pytest-randomly/>`__

  * インストールするだけで :command:`pytest` で実行するテストの順番をランダムにします

* `pytest-watch <https://pypi.org/project/pytest-watch/>`__

  * ファイルの変更が保存されたときにpytestが流れるようにできます（都度コマンド叩かなくてよくて捗る！）
