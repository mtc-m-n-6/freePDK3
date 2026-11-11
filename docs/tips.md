# 作業メモ（再利用する知識）

## PowerShell
### fcが動かない
- 原因：PowerShellでは `fc` が `Format-Custom` のエイリアス。ファイル比較は `fc.exe` を使う。
- 調べ方：`Get-Command fc -All`／`Get-Help <コマンド> -Examples`／外部コマンドは `<コマンド> /?` や `--help`。
- 画像・HTMLの比較：`Compare-Object` と `Get-FileHash` を使う。