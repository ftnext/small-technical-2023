:og:description: XP祭り2023 ワークショップ、アルファベットを13字ずらすプログラムに小さいリファクタリングを繰り返し適用していきます

==============================
小さいリファクタリング
==============================

.. include:: refactoring/review.rst.txt

.. include:: refactoring/introduction.rst.txt

.. include:: refactoring/idea.rst.txt

.. include:: refactoring/examples.rst.txt

考察
==============================

* 小さい操作を続けて適用したことで、 **Greenを保ったまま** リファクタリングができた！

  * Redになっても1つ前のGreenに **すぐに戻せる**

* リファクタリングは *ルービックキューブ* （『Clean Craftsmanship』）
* 手順（や使い所）を押さえる & エディタを使った操作を覚える -> 常中（TDDのサイクルで自由に取り出せる）

参考文献
==============================

* 『`The Art of Agile Development Second edition <https://www.jamesshore.com/v2/books/aoad2>`__』
* 『`Clean Craftsmanship <https://asciidwango.jp/post/693992928727760896/clean-craftsmanship>`__』
* 『`リファクタリング（第2版） <https://www.ohmsha.co.jp/book/9784274224546/>`__』

関連アウトプット
------------------------------

* `え、待って！リファクタリングって1つ1つのステップそんなに小さく実施するの！？ （『The Art of Agile Development』読書録） <https://nikkie-ftnext.hatenablog.com/entry/art-of-agile-development-2nd-really-small-refactoring-steps>`__

  * 写経 https://github.com/ftnext/aoad2e-py/tree/main/refactoring

* `読書ログ | 『Clean Craftsmanship』 第5章、リファクタリングはたしかに"ルービックキューブ" <https://nikkie-ftnext.hatenablog.com/entry/clean-craftsmanship-refactoring-is-rubiks-cube>`__
* `入門F2 〜VS CodeのRename Symbolで楽々リファクタリング〜 <https://nikkie-ftnext.hatenablog.com/entry/vscode-f2-easy-refactoring>`__
* `エディタの機能を知って身につけるリファクタリング 〜VS CodeでExtract編〜 <https://nikkie-ftnext.hatenablog.com/entry/vscode-extract-easy-refactoring>`__
