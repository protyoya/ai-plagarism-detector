import tensorflow as tf
import tensorflow_text as tf_text
import numpy as np
import streamlit as st
import pandas as pd

model = tf.keras.models.load_model('ai-text-detection/model/')
st.write("## AI Text Generation Detection")


