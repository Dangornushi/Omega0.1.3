# Omega0.1.3

## Omegaとは?

pythonとbatchファイルで構成された自作言語。
exeファイルが同梱されていますが不調が多いのでおすすめはしません。
batch使用のためおよび作者のマシンの都合でwindows専用です。（Windows10proで動作確認。）

## 前バージョンとの比較/変更点

- exe化(でもあんま意味なかった、、、)
- 関数定義
- それに伴った文法のアップデート

## 基本文法

サンプルプログラム：

~~~omega:main.om
class Main{
    def fu1{
        print{"OK"};
        end;
    }
    def fu2{
        int x = 12;
        str w = dangomushi;
        print{int x};
        print{str w};
        end;
    }
    func fu1
    func fu2
}
~~~

結果:
~~~
OK
12
dangomushi
~~~

- プログラムはすべてMainクラスの中に書きます。
- 関数定義にはdefを使います。関数の範囲の指定には、語尾に「;」をつけて最後にendを付けます。
- 今のところ関数に引数や型の指定はできません。
- 関数の使用にはfuncを使います.使用するにはfuncの前に宣言されてなければなりません。
- 変数にはint型かstr型をつけることが必須であり、今のところ使用する関数内で定義する必要があります。
- 変数名は何が何でも文字列になります。たとえ数字を指定しても、です。ただし、おすすめはしません。
- 変数の使用には、型宣言が必要です。

## 実行方法

- ダウンロードしたzipを展開して任意の場所に。
- 展開したファイルの中の「Omega.scr」内にある「Omega.bat」のパスをコピーして、コマンドプロンプトかなんやらを使ってそこにたどり着く。
- たどり着けたら念のためdirコマンドなどでフォルダを捜査。Omega.batとOmega.pyがあればとりあえず安心。
- コマンドプロンプトに「Omega <実行したいOmegaファイルのパス>」と打ち込み。
- プロンプト上に結果が！

## その他

製作者：dangomushi(pythonmaster)

Qiita: https://qiita.com/ThinkpadL540 (自部のモチベのためにもフォローしていただけると幸いです！)
