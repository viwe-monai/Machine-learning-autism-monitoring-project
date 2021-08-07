from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('autism-Toddler2021-7-28')

def show():
    st.header('请回答一下1-10选项关于自闭症的问题！')
    if st.checkbox('1、当你叫孩子的名字时，他/她会看着你吗？'):
        A1 ='0'
    else:
        A1 ='1'

    if st.checkbox('2、你和孩子眼神交流有多容易？'):
        A2 ='0'
    else:
        A2 ='1'
    if st.checkbox('3、你的孩子是否指出'):
        A3 ='0'
    else:
        A3 ='1'
    if st.checkbox('4、你的孩子有没有和你分享兴趣(e、 g.盯着有趣的景象）'):
        A4 ='0'
    else:
        A4 ='1'
    if st.checkbox('5、你的孩子假装吗(e、 g.爱护娃娃，用玩具电话交谈）'):
        A5 ='0'
    else:
        A5 ='1'
    if st.checkbox('6、你的孩子会跟着你看吗？'):
        A6 ='0'
    else:
        A6 ='1'
    if st.checkbox('7、如果你或家里其他人明显感到不安，你的孩子有没有表现出来想安慰他们吗(e、 （抚摸头发，拥抱头发）'):
        A7 ='0'
    else:
        A7 ='1'
    if st.checkbox('8、你能把孩子的第一句话描述成：'):
        A8 ='0'
    else:
        A8 ='1'
    if st.checkbox('9、你的孩子会用简单的手势吗(e、 g.挥手告别）'):
        A9 ='0'
    else:
        A9 ='1'
    if st.checkbox('10、你的孩子会毫无目的地盯着什么都不看吗？'):
        A10 ='0'
    else:
        A10 ='1'
    st.header('请填写一下基本信息')
    Age_Mons = st.number_input('周龄', min_value=1, max_value=100, value=25)

    sum=int(A1)+int(A2)+int(A3)+int(A4)+int(A5)+int(A6)+int(A7)+int(A8)+int(A9)+int(A10);
    result = st.number_input('1-10的问题得分多少？', min_value=0, max_value=10, value=sum)
    gender = st.selectbox('性别', ['m', 'f'])
    Ethnicity = st.selectbox('种族', ['Yellow race', 'White race','Black race','Brown race','Others'])
    if st.checkbox('是否有黄疸?'):
        Jaundice = 'yes'
    else:
        Jaundice = 'no'

    if st.checkbox('是否有亲人得ASD？'):
        family_have_ASD = 'yes'
    else:
        family_have_ASD = 'no'

    who = st.selectbox('谁完成了这个测试？', ['family member','Health Care Professional','Self','Others'])
    output=""
    input_dict = {'A1':A1,'A2':A2,'A3':A3,'A4':A4,'A5':A5,'A6':A6,'A7':A7,'A8':A8,'A9':A9,'A10':A10,
                     'Age_Mons':Age_Mons,'Qchat-10-Score':result,'Sex':gender,'Ethnicity':Ethnicity,'Jaundice':Jaundice,'Family_mem_with_ASD':family_have_ASD,'Who completed the test':who}
    input_df = pd.DataFrame([input_dict])
    output = predict(model=model, input_df=input_df)

    if st.button("预测"):
        output = predict(model=model, input_df=input_df)


        if output =='YES':
             st.success('根据系统预测：有潜在的自闭症特征,Class/ASD:{}'.format(f1))
        elif output =='NO':
             st.success('根据系统预测：没有自闭症特征,Class/ASD:{}'.format(f1))

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions






if __name__ == '__main__':
    show()