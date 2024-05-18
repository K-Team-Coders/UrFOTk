import cv2
import json

import gradio as gr
from huggingface_hub import hf_hub_download

from ocrpipeline.predictor import PipelinePredictor
from ocrpipeline.linefinder import get_structured_text


def get_config_and_download_weights(repo_id, device='cpu'):
    # download weights and configs
    pipeline_config_path = hf_hub_download(repo_id, "pipeline_config.json")
    ocr_model_path = hf_hub_download(repo_id, "ocr/ocr_model.onnx")
    kenlm_path = hf_hub_download(repo_id, "ocr/kenlm_corpus.arpa")
    ocr_config_path = hf_hub_download(repo_id, "ocr/ocr_config.json")
    segm_model_path = hf_hub_download(repo_id, "segm/segm_model.onnx")
    segm_config_path = hf_hub_download(repo_id, "segm/segm_config.json")

    # change paths to downloaded weights and configs in main pipeline_config
    with open(pipeline_config_path, 'r') as f:
        pipeline_config = json.load(f)
    pipeline_config['main_process']['SegmPrediction']['model_path'] = segm_model_path
    pipeline_config['main_process']['SegmPrediction']['config_path'] = segm_config_path
    pipeline_config['main_process']['SegmPrediction']['num_threads'] = 2
    pipeline_config['main_process']['SegmPrediction']['device'] = device
    pipeline_config['main_process']['SegmPrediction']['runtime'] = "OpenVino"

    pipeline_config['main_process']['OCRPrediction']['model_path'] = ocr_model_path
    pipeline_config['main_process']['OCRPrediction']['lm_path'] = kenlm_path
    pipeline_config['main_process']['OCRPrediction']['config_path'] = ocr_config_path
    pipeline_config['main_process']['OCRPrediction']['num_threads'] = 2
    pipeline_config['main_process']['OCRPrediction']['device'] = device
    pipeline_config['main_process']['OCRPrediction']['runtime'] = "OpenVino"

    # save pipeline_config
    with open(pipeline_config_path, 'w') as f:
        json.dump(pipeline_config, f)

    return pipeline_config_path


def predict(image_path):
    image = cv2.imread(image_path)
    rotated_image, pred_data = PREDICTOR(image)
    structured_text = get_structured_text(pred_data, ['shrinked_text'])
    result_text = [' '.join(line_text) for page_text in structured_text
                   for line_text in page_text]
    return '\n'.join(result_text)


PIPELINE_CONFIG_PATH = get_config_and_download_weights("sberbank-ai/ReadingPipeline-notebooks")

PREDICTOR = PipelinePredictor(pipeline_config_path=PIPELINE_CONFIG_PATH)

gr.Interface(
    predict,
    inputs=gr.Image(label="Upload an image of handwritten school notebook", type="filepath"),
    outputs=gr.Textbox(label="Text on the image"),
    title="School notebook recognition",
).launch()

if __name__ == "__main__":
    predict("./uploads/birth_2.jpg")
