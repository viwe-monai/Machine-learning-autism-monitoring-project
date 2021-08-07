from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('autism-Adolescent-2021-7-28')
#model2 = load_model('tuned_autim_custom_20210526')
def show():

    st.header('请回答一下1-10选项关于自闭症的问题！')
    file_upload = st.file_uploader("请上传CSV文件进行自闭症的预测", type=["csv"])
    if file_upload is not None:
      data = pd.read_csv(file_upload)
      predictions = predict_model(estimator=model, data=data)
      st.write(predictions)

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions


if __name__ == '__main__':
    show()