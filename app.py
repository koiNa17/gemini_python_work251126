import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# ページ設定
st.set_page_config(page_title="株価ダッシュボード", layout="wide")

st.title('米国・日本株価可視化アプリ')

# サイドバー設定
st.sidebar.header("設定")
ticker = st.sidebar.text_input('ティッカーシンボルを入力', 'AAPL')

st.write(f'### {ticker} の株価分析')

try:
    # データを取得（期間を長めに5年に設定）
    data = yf.download(ticker, period='5y')

    # --- データの「過剰包装」を解く（バグ回避策） ---
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    # ----------------------------------------

    if data.empty:
        st.error("データが見つかりません。")
    else:
        # --- データのお掃除 ---
        data = data.dropna()
        if data.index.tz is not None:
            data.index = data.index.tz_localize(None)
        
        # --- テクニカル指標の計算 (Day 6) ---
        # 20日移動平均線
        data['SMA_20'] = data['Close'].rolling(window=20).mean()
        # 50日移動平均線
        data['SMA_50'] = data['Close'].rolling(window=50).mean()
        # --------------------------------

        # 最新データ表示用
        latest_close = float(data['Close'].iloc[-1])
        prev_close = float(data['Close'].iloc[-2])
        delta = latest_close - prev_close
        delta_percent = (delta / prev_close) * 100

        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="現在の終値", 
                value=f"${latest_close:.2f}", 
                delta=f"{delta:.2f} ({delta_percent:.2f}%)"
            )

        # --- グラフの作成 ---
        fig = go.Figure()

        # 1. ローソク足
        fig.add_trace(go.Candlestick(
            x=data.index,
            open=data['Open'],
            high=data['High'],
            low=data['Low'],
            close=data['Close'],
            name='OHLC'
        ))

        # 2. 移動平均線（20日）
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_20'],
            mode='lines',
            name='SMA 20 (短期)',
            line=dict(color='orange', width=1.5)
        ))

        # 3. 移動平均線（50日）
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA_50'],
            mode='lines',
            name='SMA 50 (中期)',
            line=dict(color='skyblue', width=1.5)
        ))

        # レイアウト調整
        fig.update_layout(
            title=f'{ticker} Candlestick Chart with SMA',
            xaxis_title='Date',
            yaxis_title='Price',
            height=600,
            xaxis_rangeslider_visible=False
        )

        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"エラーが発生しました: {e}")