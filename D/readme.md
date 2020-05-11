# 解1

## 方針

* テレポートしていくとループがあることに気が付く
* 一度訪れた場所をリストで記憶しておくと、はじめて同じ場所を2回目に訪れた時、その地点がループの開始点である事がわかる
* 訪れたリストをルール開始前と後で分けて処理する
* Kが大きいので全部をSIMするのは不可
* Nも全探索するとギリギリの大きさであることに注意

## 実装

* `if node in footprint:`として訪れたかどうか判定したくなるが`N = 2 * 10 ** 5`なので処理が間に合わない。
  * 結局footprintの中をすべて検索しているので、if文をNのfor文で回すと`O(N**2)`となってTLE
  
    ``` NG.py
    # NGの例（O(N^2)）
    for i in range(N):
      if i in footprint:
          some_func
      else:
          footprint.append(i)
    ```

  * 対策は各ノードの未踏管理フラグのリストを用意し`O(1)`でアクセスすること
  
    ``` OK.py
    # OKの例（O(N)）
    footprint = [False for _ in range(N)]

    for i in range(N):
      if footprint[i]:
          some_func
      else:
          footprint[i] = True
    ```

* 呼び出されたノードをリストで持っておく
* ループ開始が確認されたタイミングで上のリストをぶった切って、非ループ部とループ部を分けて考える。


# 解2

## ダブリング

* 各ノードから2のN乗回遷移した表を作って参照する
  * まず一回目に各ノードから遷移したリストを作る
  * N番目（2**N）のリストはN-1のリストから参照して作る
    * N-1番目内で参照するとN-1番目までの参照を2回やったことになるから2倍になる
    * 二倍になるということはN番目のリストになる

## 実装

* 最大遷移回数を2進数にして桁の数だけ参照リストを作る
  * 各2のN乗遷移に対応
  
    ```
    for _ in range(len(bit_k)-1):
      temp_list = telepo_list[-1]
      new_telep = [temp_list[i-1] for i in temp_list]
      telepo_list.append(new_telep)
    ```


* bitシフトで使う桁のとことだけ遷移を行う
* 遷移は下の桁から行うので `if ((K >> i) & 1):`
* また参照する遷移リストも先頭から使う

    ```
      goto = 1
      for i in range(len(bit_k)):
          temp_list = telepo_list[i]
          if ((K >> i) & 1):
              goto = temp_list[goto - 1]
    ```