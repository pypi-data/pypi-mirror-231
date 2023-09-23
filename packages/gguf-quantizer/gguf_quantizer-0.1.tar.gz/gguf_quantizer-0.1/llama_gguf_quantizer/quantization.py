import os 
def run(MODEL_ID, QUANTIZATION_METHODS) : 
  # Download model
  print("git lfs install")
  os.system("git lfs install")
  print(f"Start Downloading {MODEL_ID} .. (this process may take some time)")
  os.system(f"git clone https://huggingface.co/{MODEL_ID}")
  MODEL_NAME = MODEL_ID.split('/')[-1]
  GGML_VERSION = "gguf"
  print("Done!!")
  print(f"start converting {MODEL_NAME} Model weight to GGML FP16 format (this process may take some time)")
  # Convert to fp16
  fp16 = f"{MODEL_NAME}/{MODEL_NAME.lower()}.{GGML_VERSION}.fp16.bin"
  os.system(f"python llama.cpp/convert.py {MODEL_NAME} --outtype f16 --outfile {fp16}")
  # you can select more QUANTIZATION_METHODS
  for method in QUANTIZATION_METHODS:
      qtype = f"{MODEL_NAME}/{MODEL_NAME.lower()}.{GGML_VERSION}.{method}.bin"
      print(f"Start quantizing {MODEL_NAME}") 
      os.system(f"./llama.cpp/quantize {fp16} {qtype} {method}")
  print(f"The Quentized model path : {qtype} ")