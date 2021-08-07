from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np

model = load_model('autism-Child-2021-7-28')
#model2 = load_model('tuned_autim_custom_20210526')
def show():
    st.header('请回答一下1-10选项关于自闭症的问题！')
    if st.checkbox('1、当你叫孩子的名字时，他/她会看着你吗？'):
        A1_Score ='0'
    else:
        A1_Score ='1'

    if st.checkbox('2、你和孩子眼神交流有多容易？'):
        A2_Score ='0'
    else:
        A2_Score ='1'
    if st.checkbox('3、你的孩子是否指出'):
        A3_Score ='0'
    else:
        A3_Score ='1'
    if st.checkbox('4、你的孩子有没有和你分享兴趣(e、 g.盯着有趣的景象）'):
        A4_Score ='0'
    else:
        A4_Score ='1'
    if st.checkbox('5、你的孩子假装吗(e、 g.爱护娃娃，用玩具电话交谈）'):
        A5_Score ='0'
    else:
        A5_Score ='1'
    if st.checkbox('6、你的孩子会跟着你看吗？'):
        A6_Score ='0'
    else:
        A6_Score ='1'
    if st.checkbox('7、如果你或家里其他人明显感到不安，你的孩子有没有表现出来想安慰他们吗(e、 （抚摸头发，拥抱头发）'):
        A7_Score ='0'
    else:
        A7_Score ='1'
    if st.checkbox('8、你能把孩子的第一句话描述成：'):
        A8_Score ='0'
    else:
        A8_Score ='1'
    if st.checkbox('9、你的孩子会用简单的手势吗(e、 g.挥手告别）'):
        A9_Score ='0'
    else:
        A9_Score ='1'
    if st.checkbox('10、你的孩子会毫无目的地盯着什么都不看吗？'):
        A10_Score ='0'
    else:
        A10_Score ='1'
    st.header('请填写一下基本信息')
    age = st.number_input('年龄', min_value=1, max_value=100, value=25)
    gender = st.selectbox('性别', ['m', 'f'])
    ethnicity = st.selectbox('种族', ['Yellow race', 'White race','Black race','Brown race','Others'])
    if st.checkbox('是否有黄疸?'):
        jundice = 'yes'
    else:
        jundice = 'no'
    if st.checkbox('是否去寻找自闭症医生的初步诊断?'):
        austim = 'yes'
    else:
        austim = 'no'
    contry_of_res = st.selectbox('来自那个国家？', ['China','Egypt','Cairo','Sudan','Khartoum','Japan','Jordan', 'United States', 'United Kingdom', 'Austria', 'United Arab Emirates','Kuwait','Europe','Russia','Mexico','Pakistan','Cyprus'])
    if st.checkbox('用过APP参加筛选吗？'):
        used_app_before = 'yes'
    else:
        used_app_before = 'no'

    sum=int(A1_Score)+int(A2_Score)+int(A3_Score)+int(A4_Score)+int(A5_Score)+int(A6_Score)+int(A7_Score)+int(A8_Score)+int(A9_Score)+int(A10_Score);
    result = st.number_input('1-10的问题得分多少？', min_value=0, max_value=10, value=sum)
    age_desc = st.selectbox('测试的人处于那个年龄段', ['4-11years', '12-16years', '18 and more'])
    relation= st.selectbox('谁在完成此次测试？', ['Parent', 'self', 'caregiver','medical staff','clinician','etc'])
    output=""
    input_dict = {'A1_Score':A1_Score,'A2_Score':A2_Score,'A3_Score':A3_Score,'A4_Score':A4_Score,'A5_Score':A5_Score,'A6_Score':A6_Score,'A7_Score':A7_Score,'A8_Score':A8_Score,'A9_Score':A9_Score,'A10_Score':A10_Score,
                  'age':age,'gender':gender,'ethnicity':ethnicity,'jundice':jundice,'austim':austim,'contry_of_res':contry_of_res,'used_app_before':used_app_before,'result':result,'age_desc':age_desc,'relation':relation}
    input_df = pd.DataFrame([input_dict])
    output = predict(model=model, input_df=input_df)

    if st.button("预测"):
        output = predict(model=model, input_df=input_df)

        f1=output
        if f1 =='YES':
            st.success('根据系统预测：有潜在的自闭症特征,Class/ASD:{}'.format(f1))
        elif f1 =='NO':
            st.success('根据系统预测：没有自闭症特征,Class/ASD:{}'.format(f1))

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions
#def predict2(model2, input_df):
# predictions_df = predict_model(estimator=model2, data=input_df)
# predictions = predictions_df['Label'][0]
# return predictions





if __name__ == '__main__':
    show()