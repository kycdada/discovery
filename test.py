import pandas as pd
import uuid
import sys

# 組み込む前に、テストする用

# pandas 関連ロジックテスト
# dataframeでcsvをopen
df = pd.read_csv("./test.csv",sep=",")

# 追加データ用frame作成
uuid = uuid.uuid1()
add_df = pd.DataFrame([[0,0,uuid]],columns=["full_path","document_id","uuid"])

# データ追加(appendメソッドは代入しなきゃダメ)
df = df.append(add_df,ignore_index=True)


# do_whileでuuid重複チェック
# 無限ループにならないために100ループで終了
pd_loop = 100

while True:
    break_flg = True
    pd_loop-=1
    # pandasフレームを列で回す、uuidが被ってないか判断
    for id in df["uuid"]:
        this_uuid = 123
        print(id)
        # 念のため、型変換してから、比較
        if(str(this_uuid) == str(id)):
            
            break_flg = False
            print("loop")
    if(break_flg):
        break
    if(pd_loop <= 0):
        print("ループが止まらないため、強制終了")
        sys.exit()

