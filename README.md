# Pandoc drawio export filter

DrawIOファイルを含むMarkdownをPandocでWordに変換するときに、デフォルトではフォント関連のエラーが発生します。  
そのため、このフィルタを用いて、DrawIOファイルをPNG画像に変換し、エラーを解消します。  

## 1. 特徴

- Pandocのカスタムフィルターとして動作します。
- 拡張子が`.drawio.svg`のファイルを、Draw.IOのコマンドラインでPNGファイルに変換します。

## 2. インストール方法

### 2.1. 事前に必要なもの

- Pandoc≧3.6.2: <https://github.com/jgm/pandoc/releases>  
  ※古いバージョンのPandocだと、動作が異なる場合があります。
- Python≧3.10: <https://www.python.org/downloads/>
- Docker
- drawio-desktop-headless: <https://github.com/rlespinasse/docker-drawio-desktop-headless>  
- (オプション)rsvg-convert
  
  
`drawio-desktop-headless`は、以下のコマンドでインストールできます。  

```shell-session
$ dockre pull rlespinasse/drawio-desktop-headless
```
  
`rsvg-convert`は、本フィルタとは直接関係はありませんが、SVGファイルを含むMarkdownをPandocでWordに変換するときに必要になります。  
`rsvg-convert`は、以下のコマンドでインストールできます。  

- Windowsの場合

```shell-session
(管理者権限で実行)
# winget install --accept-source-agreements chocolatey.chocolatey
# choco install rsvg-convert
```

- Fedoraの場合

```shell-session
(管理者権限で実行)
# dnf install librsvg2-tools
```

- Debianの場合

```shell-session
(管理者権限で実行)
# apt install librsvg2-bin
```

### 2.2. インストール

``` shell-session
$ git clone https://github.com/Akira106/pandoc_drawio_export_filter.git
$ cd pandoc_drawio_export_filter
$ pip3 install .
```

※ 上記の実行時に`XXXXX which is not on PATH.`のようなWarningメッセージが出た場合、環境変数`PATH`に、インストール先のパスを追加してください。
  
  
## 3. Wordファイルへの変換

pandocのオプションに、`--filter=pandoc_drawio_export_filter`を追加してください。  

VSCodeの拡張機能であるMarkdown Preview Enhancedを使ってエクスポートする場合は、例えば以下のような設定をしてください。  
※エクスポート設定の詳細は、Markdown Preview Enhancedのマニュアルをご参照ください。  

`例`

    ---
    output:
      word_document:
        path: output_docx/test_export.docx
        pandoc_args: ['--filter=pandoc_drawio_export_filter', '--wrap=preserve']
    ---
