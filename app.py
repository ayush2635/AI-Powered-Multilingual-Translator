import os
import streamlit as st
from transformers import MBartForConditionalGeneration, MBart50Tokenizer

# Paths
MODEL_DIR = "mbart-finetuned"
SPLIT_DIR = os.path.join(MODEL_DIR, "mbart-splits")
MODEL_PATH = os.path.join(MODEL_DIR, "model.safetensors")

@st.cache_resource
def load_model():
    # Rebuild model.safetensors if not present
    if not os.path.exists(MODEL_PATH):
        with open(MODEL_PATH, "wb") as outfile:
            i = 0
            while True:
                part_path = os.path.join(SPLIT_DIR, f"model.safetensors.part_{i:03d}")
                if not os.path.exists(part_path):
                    break
                with open(part_path, "rb") as part_file:
                    outfile.write(part_file.read())
                i += 1
        st.success(f"✅ Reconstructed model.safetensors from {i} parts")

    # Load model and tokenizer
    model = MBartForConditionalGeneration.from_pretrained(
        MODEL_DIR,
        trust_remote_code=True
    )
    tokenizer = MBart50Tokenizer.from_pretrained(MODEL_DIR)
    return model, tokenizer

# --- Streamlit UI ---
st.set_page_config(page_title="Multilingual Translator", layout="centered")
st.title("🌍 AI-Powered Multilingual Translator")

model, tokenizer = load_model()
st.success("✅ Model loaded successfully!")

# Translator UI
input_text = st.text_area("Enter English text to translate:")
target_lang = st.selectbox("Select target language", ["Spanish", "French", "Italian", "Portuguese", "Hindi"])

LANGUAGE_CODES = {
    "Spanish": "es_XX",
    "French": "fr_XX",
    "Italian": "it_IT",
    "Portuguese": "pt_XX",
    "Hindi": "hi_IN"
}

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        tokenizer.src_lang = "en_XX"
        encoded = tokenizer(input_text, return_tensors="pt")
        generated_tokens = model.generate(**encoded, forced_bos_token_id=tokenizer.lang_code_to_id[LANGUAGE_CODES[target_lang]])
        translated = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        st.success(f"Translation ({target_lang}):")
        st.markdown(f"**{translated}**")
