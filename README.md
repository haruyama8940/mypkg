# mypkg
## 課題2 <内容>
- <内容>
  - 講義で作成したデバイスドライバを改造し、kyakuノードとzinzyaノードを作成  
  - kyakuノードからお賽銭（100or1000or10000）のトピックを出し、zinzyaノードで  
    お賽銭の学に応じた運勢占いを行う。
- <オリジナリティ>
  - 関数化を用いて簡潔なコードへとすること及び、お賽銭の額、運勢という2つのランダム性 
    を用いて実際におみくじを引く際の臨場感を演出
## <動作動画>
  - リンク　https://youtu.be/u64slHveWAA
## <実行環境>
ubuntu(desktop,server問わない)及び対応するROS環境が必要
次の環境では動作を確認
|||
|:---|---:|
|OS|ubuntu 18.04|
|ROS_ver|melodic|

## <動作手順>
- 環境構築
Ubuntuに関してはインストール 
ROSに関してはワークスペースの作成、catkin_make、roscoreができる
環境が作成されているものとし、構築については割愛する
※作成の際にcatkin_buildではなくcatkin_buildを使用のこと
作成したワークスペース内、srcへ移動後、次のコマンドを使用しcloneを  
行い、その後buildを行う
```bash
$cd {作成したワークスペース}/src
$git clone https://github.com/haruyama8940/mypkg.git
$cd ../ &&　catkin_make

```
- 動作
ターミナルを3枚起動
1枚目のターミナルで次のコマンドを用いて権限を付与、その後rosを起動
```bash
$cd {作成したワークスペース}/src/mypkg/scripts
$chmod +x kyaku.py && chmod +x zinzya.py
$roscore
```
2枚目のターミナルで次のコマンドを用いてkyakuノードを起動
```bash
$rosrun mypkg kyaku.py
```
3枚目のターミナルで次のコマンドを用いてzinzyaノードを起動
```bash
$rosrun mypkg zinzya.py
```
良いおみくじライフを
