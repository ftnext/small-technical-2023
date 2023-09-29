import rot13


class TestTransform:
    def test_空文字列を渡すと空文字列を返す(self):
        assert "" == rot13.transform("")

    def test_アルファベット小文字を渡すと13字ずらした文字列を返す(self):
        assert "nopqrstuvwxyzabcdefghijklm" == rot13.transform(
            "abcdefghijklmnopqrstuvwxyz"
        )

    def test_アルファベット大文字を渡すと13字ずらした文字列を返す(self):
        assert "NOPQRSTUVWXYZABCDEFGHIJKLM" == rot13.transform(
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        )

    def test_アルファベットの記号を渡すと13字ずらさずに元の文字列を返す(self):
        assert "`{@[" == rot13.transform("`{@[")

    def test_数字の文字列を渡すと13字ずらさずに元の文字列を返す(self):
        assert "1234567890" == rot13.transform("1234567890")

    def test_アルファベットでない文字列を渡すと13字ずらさずに元の文字列を返す(self):
        assert "åéîøüçñあ" == rot13.transform("åéîøüçñあ")

    def test_絵文字を渡すと13字ずらさずに元の文字列を返す(self):
        assert "✅🚫🙋" == rot13.transform("✅🚫🙋")
