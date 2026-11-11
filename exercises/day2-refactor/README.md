pip install pillow が必要なこと
入力画像（chipmunk.png）は、リポジトリに含まれていないこと
実行の仕方：python.exe ..\freePDK3\exercises\day2-refactor\magnified_images.py
INPUT画像（..\img\chipmunk.png）はDALLで作成。ライセンスが不明なので、コミットしないのが安全です。

# day2-refactor（教材スクリプト）

## 何をするか（Before時点の理解）
- 入力：イメージファイル（C:\Git\img\chipmunk.png）
- 処理：イメージファイル拡大図を作成する
- 出力：イメージファイル拡大図一覧を表示するHTMLファイル

## 実行方法
- 事前に `pip install pillow`
- 入力画像（chipmunk.png）はリポジトリに含まない。`C:\Git\img\` に置く
- 実行：`cd C:\Git\run_before` → `python.exe ..\freePDK3\exercises\day2-refactor\magnified_images.py`