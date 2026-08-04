import streamlit as st
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="GPT-2 Text Generator",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🤖 GPT-2 Generator")

st.sidebar.markdown("### Generation Settings")
st.sidebar.info(
    """
    Adjust the parameters and generate text
    using the fine-tuned GPT-2 model.
    """
)

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def load_model():
    tokenizer = GPT2Tokenizer.from_pretrained("models/final_model")
    model = GPT2LMHeadModel.from_pretrained("models/final_model")
    return tokenizer, model

tokenizer, model = load_model()

# -----------------------------
# Main Title
# -----------------------------
st.title("🤖 GPT-2 Text Generator")

st.write(
    "Generate coherent text from a prompt using a fine-tuned GPT-2 model."
)

# -----------------------------
# User Input
# -----------------------------
prompt = st.text_area(
    "Enter Prompt",
    height=180,
    placeholder="Example: Once upon a time..."
)

temperature = st.slider(
    "Temperature",
    min_value=0.1,
    max_value=1.5,
    value=0.8,
    step=0.1
)

max_length = st.slider(
    "Maximum Length",
    min_value=30,
    max_value=300,
    value=120
)

# -----------------------------
# Generate Button
# -----------------------------
if st.button("🚀 Generate Text", use_container_width=True):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:

        inputs = tokenizer.encode(
            prompt,
            return_tensors="pt"
        )

        with st.spinner("Generating text..."):

            outputs = model.generate(
                inputs,
                max_length=max_length,
                do_sample=True,
                temperature=temperature,
                top_k=50,
                top_p=0.95,
                repetition_penalty=1.2,
                pad_token_id=tokenizer.eos_token_id
            )

            generated_text = tokenizer.decode(
                outputs[0],
                skip_special_tokens=True
            )

        st.success("Text Generated Successfully!")

        st.subheader("Generated Text")

        st.text_area(
            "",
            generated_text,
            height=250
        )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption("GPT-2 Fine-Tuned Text Generation | Prodigy InfoTech Task-01")