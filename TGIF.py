import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import platform
from matplotlib import font_manager, rc

# 한글 폰트 설정 (이게 없으면 그래프의 한글이 깨집니다)
if platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False 

st.title("국세청 근로소득 데이터 분석기")

# 데이터 불러오기
file_path = "국세청_근로소득 백분위(천분위) 자료_20241231.csv"

try:
    # 핵심 수정: encoding='cp949' 추가
    df = pd.read_csv(file_path, encoding='cp949')
    st.success("데이터를 성공적으로 불러왔습니다!")
    
    # 데이터 미리보기
    st.subheader("데이터 미리보기")
    st.dataframe(df.head(10)) 
    
    # 데이터분석 그래프 그리기
    st.subheader("근로소득 항목별 그래프")

    column_names = df.columns.tolist() 
    selected_column = st.selectbox("항목을 선택하세요 : ", column_names)

    # 그래프 그리기
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(df[selected_column], ax=ax, color="#FFFACD") 
    ax.set_title(f"[{selected_column}] 분포 그래프") 
    ax.set_xlabel(selected_column) 
    ax.set_ylabel("빈도수") 

    # streamlit에 그래프 표시
    st.pyplot(fig)

except FileNotFoundError:
    st.error(f" '{file_path}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")
except Exception as e:
    st.error(f"오류가 발생했습니다: {e}")