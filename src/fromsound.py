import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import librosa
import numpy as np
import math


def create_canvas_gauge(parent):
    # Canvasウィジェットを使ってメーターを作成
    canvas = tk.Canvas(parent, width=300, height=200, bg="white")
    canvas.pack(pady=20)

    # 円弧を描画
    canvas.create_arc(
        20, 20, 280, 280, start=30, extent=120, style=tk.ARC, width=3, outline="blue"
    )

    # 初期の針の位置を描画
    needle = canvas.create_line(150, 150, 150, 50, width=4, fill="red")

    def update_needle(position):
        # 針の角度を計算 (-1 から 1 の範囲で指定)
        angle = 30 + (120 * (position + 1) / 2)
        radians = math.radians(angle)
        x = 150 + 100 * math.cos(radians)
        y = 150 - 100 * math.sin(radians)
        canvas.coords(needle, 150, 150, x, y)

    return update_needle


def start_audio_stream(update_gauge):
    # サンプリングレートとバッファサイズを設定
    sample_rate = 22050  # librosaのデフォルトサンプリングレート
    buffer_size = 1024

    # 音声コールバック関数
    def audio_callback(indata, frames, time, status):
        if status:
            print(f"Error: {status}", flush=True)
        samples = np.squeeze(indata)

        # librosaを使ってピッチ解析
        try:
            # 音声データのゼロ交差数を用いて基本周波数を推定
            pitches, magnitudes = librosa.core.piptrack(y=samples, sr=sample_rate)

            # 最大の振幅を持つ周波数を取得（簡易的な方法）
            pitch = 0
            if magnitudes.any():
                index = magnitudes.argmax()
                pitch = pitches[
                    index // magnitudes.shape[1], index % magnitudes.shape[1]
                ]

            if pitch > 0:
                # ピッチを基準に、針の位置を -1 から 1 の範囲にマッピング
                reference_pitch = 440.0  # A4の基準ピッチ
                deviation = (pitch - reference_pitch) / reference_pitch
                deviation = max(-1, min(1, deviation))  # -1 から 1 にクランプ

                # メーターを更新
                update_gauge(deviation)

        except Exception as e:
            print(f"Error analyzing pitch: {e}")

    # サウンドデバイスのストリームを開く
    stream = sd.InputStream(
        callback=audio_callback,
        channels=1,
        samplerate=sample_rate,
        blocksize=buffer_size,
    )
    stream.start()


def build(parent, pitch_list):
    # 音声入力タブに関連するUIを作成
    frame_inputsound = ttk.Frame(parent)
    frame_inputsound.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    # メーターの作成
    update_gauge = create_canvas_gauge(frame_inputsound)

    # ボタンを作成してリアルタイム音声解析を開始
    start_button = ttk.Button(
        frame_inputsound,
        text="リアルタイム解析開始",
        command=lambda: start_audio_stream(update_gauge),
    )
    start_button.pack(pady=10)
