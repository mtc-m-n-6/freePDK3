# 作業メモ（再利用する知識）

## PowerShell
### fcが動かない
- 原因：PowerShellでは `fc` が `Format-Custom` のエイリアス。ファイル比較は `fc.exe` を使う。
- 調べ方：`Get-Command fc -All`／`Get-Help <コマンド> -Examples`／外部コマンドは `<コマンド> /?` や `--help`。
- 画像・HTMLの比較：`Compare-Object` と `Get-FileHash` を使う。

## Git作業の流れ（毎回同じ）
1. `git switch main` → `git pull`（最新にする）
2. GitHubでIssueを作る（目的・完了条件）
3. `git switch -c 種類/番号-説明`（ブランチ作成）
4. 修正する（VS Code）
5. 意図ごとに `git add <ファイル>` → `git diff --staged` → `git commit -m "動詞で始まる文 (#番号)"`
6. `git push -u origin <ブランチ名>`
7. GitHubでPR作成（末尾に `Closes #番号`）
8. Files changedを自分で読み、コメント → Merge → Delete branch
9. `git switch main` → `git pull` → `git branch -d <ブランチ名>` → `git fetch --prune`
10. `git status` と `git log --oneline` で状態を確認（記憶ではなく状態で確認）

## ruff インストール＆実行
- ruff は、余分なLibrary インポートをチェックするコマンド
### VScodeへのインストール
1.　VS Codeで拡張機能を開いて、【Ruff — Astral Software】をインストール
2.　Ctrl + Shift + P　⇒　Preferences: Open User Settings (JSON) で下記一文を追加
    {
        "ruff.importStrategy": "useBundled"
    }
3.　Ctrl + Shift + P　⇒　Developer: Reload Window
4.　Ctrl + Shift + P　⇒　Ruff: Format Document
