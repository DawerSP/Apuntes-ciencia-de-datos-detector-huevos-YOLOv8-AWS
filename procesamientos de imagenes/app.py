from pathlib import Path

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image
from streamlit_drawable_canvas import st_canvas


RUTA_MODELO = Path(__file__).with_name("modelo_mnist.keras")


@st.cache_resource
def cargar_modelo():
    if not RUTA_MODELO.exists():
        raise FileNotFoundError(
            f"No se encontró el modelo: {RUTA_MODELO}\n"
            "Coloca modelo_mnist.keras en la misma carpeta que app.py."
        )
    return tf.keras.models.load_model(RUTA_MODELO)


modelo = cargar_modelo()

st.title("Reconocedor de números")
st.write("Dibuja un número del 0 al 9 y pulsa **Predecir**.")

lienzo = st_canvas(
    fill_color="rgba(0, 0, 0, 0)",
    stroke_width=18,
    stroke_color="#FFFFFF",
    background_color="#000000",
    width=280,
    height=280,
    drawing_mode="freedraw",
    return_image_data=True,
    key="lienzo",
)

if st.button("Predecir"):
    if lienzo.image_data is None:
        st.warning("Primero dibuja un número.")
    else:
        imagen = Image.fromarray(
            lienzo.image_data.astype("uint8")
        ).convert("L")
        imagen = imagen.resize((28, 28), Image.Resampling.LANCZOS)

        entrada = np.asarray(imagen, dtype=np.float32) / 255.0
        entrada = entrada.reshape(1, 28, 28, 1)

        probabilidades = modelo.predict(entrada, verbose=0)[0]
        numero = int(np.argmax(probabilidades))

        st.subheader(f"El modelo predice: {numero}")
        st.write(f"Confianza: {probabilidades[numero]:.1%}")