import smtplib

# 送信元メールアドレス
form_mailaddress = "form_address@gmail.com"
# 送信先メールアドレス
main_to = 'to_address@gmail.com'

# パスワード(Googleメールの場合発行したアプリケーションパスワードを使用すること)
password = "password"

# メッセージ
msg = "Hello World"

# SMTPオブジェクト作成
smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
# 設定
smtpobj.ehlo()

# TLS接続スタート
smtpobj.starttls()

# 設定
smtpobj.ehlo()

# ログイン
smtpobj.login(form_mailaddress, password)

# 送信
smtpobj.sendmail(form_mailaddress, main_to, msg)

# コネクション切断
smtpobj.close()
