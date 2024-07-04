import argparse
import gradio as gr
import edge_tts
import asyncio
import os
# https://speech.platform.bing.com/consumer/speech/synthesize/readaloud/voices/list?trustedclienttoken=6A5AA1D4EAFF4E9FB37E23D68491D6F4 - там голоса брать. думаю поймете. ShortName короче
SUPPORTED_VOICES = {
    'DmitryNeural-Руский(муж.)': 'ru-RU-DmitryNeural',
    'SvetlanaNeural-Русский(жен.)': 'ru-RU-SvetlanaNeural',
    'OstapNeural-Украинский(муж.)': 'uk-UA-OstapNeural',
    'PolinaNeural-Украинский(жен.)': 'uk-UA-PolinaNeural'
}

# Смена голоса
def changeVoice(voices):
    example = SUPPORTED_VOICES[voices]
    example_file = os.path.join(os.path.dirname(__file__), "example/"+example+".wav")
    return example_file

# Преобразование текста в речь
async def textToSpeech(text, voices, rate, volume):
    output_file = "output.mp3"
    voices = SUPPORTED_VOICES[voices]
    if (rate >= 0):
        rates = rate = "+" + str(rate) + "%"
    else:
        rates = str(rate) + "%"
    if (volume >= 0):
        volumes = "+" + str(volume) + "%"
    else:
        volumes = str(volume) + "%"
    communicate = edge_tts.Communicate(text,
                                       voices,
                                       rate=rates,
                                       volume=volumes,
                                       proxy=None)
    await communicate.save(output_file)
    audio_file = os.path.join(os.path.dirname(__file__), "output.mp3")
    if (os.path.exists(audio_file)):
        return audio_file
    else:
        raise gr.Error("Преобразование не удалось！")
        return FileNotFoundError


# Сбросить результат конвертации
def clearSpeech():
    output_file = os.path.join(os.path.dirname(__file__), "output.mp3")
    if (os.path.exists(output_file)):
        os.remove(output_file)
    return None, None


with gr.Blocks(css="style.css", title="Преобразование текста в речь") as demo:
    gr.Markdown("""
    # Преобразование текста в речь через Microsoft Edge
    """)
    with gr.Row():
        with gr.Column():
            text = gr.TextArea(label="Текст", elem_classes="text-area")
            btn = gr.Button("Сгенерировать", elem_id="submit-btn")
        with gr.Column():
            voices = gr.Dropdown(choices=[
                "DmitryNeural-Руский(муж.)", "SvetlanaNeural-Русский(жен.)", "OstapNeural-Украинский(муж.)", "PolinaNeural-Украинский(жен.)"
            ],
                                 value="DmitryNeural-Руский(муж.)",
                                 label="Голос",
                                 info="Пожалуйста, выберите голос",
                                 interactive=True)
            
            example = gr.Audio(label="Пример голоса",
                              value="example/ru-RU-DmitryNeural.wav",
                              interactive=False,
                              elem_classes="example")

            voices.change(fn=changeVoice,inputs=voices,outputs=example)
            rate = gr.Slider(-100,
                             100,
                             step=1,
                             value=0,
                             label="Увеличение / уменьшение скорости речи",
                             info="Скорость речи быстрее / медленнее",
                             interactive=True)
            
            volume = gr.Slider(-100,
                               100,
                               step=1,
                               value=0,
                               label="Увеличение / уменьшение громкости звука",
                               info="Увеличить / уменьшить громкость звука",
                               interactive=True)
            audio = gr.Audio(label="Результат",
                             interactive=False,
                             elem_classes="audio")
            btn.click(fn=textToSpeech,
                      inputs=[text, voices, rate, volume],
                      outputs=[audio])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-name", default="127.0.0.1", help="Gradio server name")
    args = parser.parse_args()
    demo.launch(server_name=args.server_name)
