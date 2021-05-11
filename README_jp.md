# ExportAllShapeKeysAsObj
Blender スクリプト

## 概要
このスクリプトはアクティブなオブジェクトの全てのシェイプキーを頂点の順番を保持してOBJにエクスポートします。
エクスポートされる各OBJファイルの名称はシェイプキーの名称です。

![screen1](screen1.png 'screen1')

オプションの動作として、 _Mix Non Zero Shape Keys_ にチェックを入れて実行した場合は、値が0ではないシェイプキーのエクスポートはスキップし、それらのシェイプキーの値はそのままに、それ以外のシェイプキーをエクスポートします。つまり、0でないシェイプキーが他のシェイプキーにミックスされた形状がエクスポートされます。

_Mix Non Zero Shape Keys_ のチェックを入れずに実行した場合はシェイプキーの値に関係なく、全てのシェイプキーがそれぞれそのまま出力されます。

![screen2](screen2.png 'screen2') ![screen3](screen3.png 'screen3')

I tested this only on blender 2.92. Use this script at your own risk.

## 使い方
1. 対象のオブジェクトを選択。

2. "File" > "Export" > "Export All Shape Keys As Obj" で実行。

3. 保存先のディレクトリを選択し、必要ならばオプションを指定 :
 - Mix Non Zero Shape Keys
  + チェックを入れて実行した場合、値が0ではないシェイプキーのエクスポートはスキップし、それらのシェイプキーの値はそのままに、それ以外のシェイプキーをエクスポートする。

  + チェックを入れずに実行した場合、シェイプキーの値に関係なく、全てのシェイプキーがそれぞれそのまま出力される。

 - Scale
  + blender の標準のOBJエクスポートオプションと同じ

 - Apply Modifiers
  + blender の標準のOBJエクスポートオプションと同じ

 - Write Materials
  + blender の標準のOBJエクスポートオプションと同じ

## インストール
Edit > Preferences > Add-ons > Install... and select export_all_shape_keys_as_obj.py

## 注意
* このスクリプトは既存の同名OBJファイルが存在した場合 **上書きします** 。
