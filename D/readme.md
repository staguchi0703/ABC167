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
