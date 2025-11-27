# 1. ベースイメージの指定 (軽量版Python)
FROM python:3.9-slim

# 2. 作業ディレクトリ（コンテナ内の作業場所）を設定
# これ以降のコマンドは全てコンテナ内の /app フォルダで行われます
WORKDIR /app

# 3. 必要なファイル(requirements.txt)をコンテナにコピー
# COPY [ホストのファイル] [コンテナの配置場所]
COPY requirements.txt .

# 4. ライブラリのインストール実行
# pip <ピップ> はPythonのライブラリ管理ツールです
# -r は「リスト(requirements)から読み込む」というオプションです
RUN pip install --no-cache-dir -r requirements.txt

# 5. プログラム本体をコンテナにコピー
COPY main.py .

# 6. コンテナ起動時に実行するコマンド
CMD ["python", "main.py"]