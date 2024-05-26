# question_bank_exercise
## Existing Library/Software
- python 3.11
- 前端 : bootstrap 5.3
- GUI: eel
- Database: sqlite
## step 1 clone github
- 把專案載入你想要放的資料夾底下，去 git bash 輸入以下指令
```
git clone https://github.com/Shaila-Hsiao/question_bank_exercise/
```
## step 2 安裝 python 所需套件
- eel
  ```
  pip install eel
  ```
- 或者直接輸入
  ```
  pip install -r requirements.txt
  ```
## step 3 開啟程式碼
> 記得要到 {your url}\question_bank_exercise\eel_tut\ 資料夾下輸入指令
- 輸入指令開啟 app.py
  ```
  python app.py
  ```
- 成功開啟的畫面
  - 請選擇 【章節】、【題型】:

    ![image](https://github.com/Shaila-Hsiao/question_bank_exercise/assets/105621058/c736f212-9694-43eb-ab56-ade0f57655ed)

    - 選擇題

      ![image](https://github.com/Shaila-Hsiao/question_bank_exercise/assets/105621058/f147679b-5297-424e-b591-2a4f308677bb)

    - 是非題

      ![image](https://github.com/Shaila-Hsiao/question_bank_exercise/assets/105621058/aef336a5-6457-41b8-9eb8-a930a0b51d65)

      ![1713976025049](https://github.com/Shaila-Hsiao/question_bank_exercise/assets/105621058/3c736115-5d1c-49e0-be7a-269674065e78)

## fix
- [X] Json 格式篩選題目有問題 
- [X] 是非題
- [ ] 有返回鍵:
  - [X] 返回選擇章節頁面重新選擇章節
  - [ ] 返回上一題
- [X] 紀錄練習過的題目
