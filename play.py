from fairseq.checkpoint_utils import load_model_ensemble_and_task_from_hf_hub
from fairseq.models.text_to_speech.hub_interface import TTSHubInterface
import numpy as np
from scipy.io import wavfile
import subprocess

output_file_path = 'output_audio.wav'
output_file_path_slow = 'output_audio_slow.wav'


models, cfg, task = load_model_ensemble_and_task_from_hf_hub(
    "facebook/fastspeech2-en-ljspeech",
    arg_overrides={"vocoder": "hifigan", "fp16": False}
)
model = models[0]
TTSHubInterface.update_cfg_with_data_cfg(cfg, task.data_cfg)
generator = task.build_generator([model], cfg)

# text = '"' + good_morning() + '"'
def play_sound(text):
    # subprocess.call(["aplay", output_file_path_slow])
    sample = TTSHubInterface.get_model_input(task, text)
    wav, rate = TTSHubInterface.get_prediction(task, model, generator, sample)

    wav = np.int16(wav * 32767)
    wavfile.write(output_file_path, rate, wav)


    subprocess.call(["aplay", output_file_path])
    print(text)