import streamlit as st
import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# インポート先の情報を入力する
# 入力フォームを作成
st.title('*Enter The Deploye Information* :sunglasses:')
with st.form(key = 'snowflake_form'):
    account_name = st.text_input('Account Name')
    user_name    = st.text_input('User Name')
    password     = st.text_input('Password', type='password')
    warehouse    = st.text_input('Warehouse')
    database     = st.text_input('Database')
    schema       = st.text_input('Schema')
    table        = st.text_input('Table')
    # 送信ボタンを作成
    submit_button = st.form_submit_button(label='Connect !!!')


# Snowflakeへの接続を確立する
def snowflake_connection():
    try:
        conn = snowflake.connector.connect (
            account  = account_name,
            user     = user_name,
            password = password,
            database = database,
            schema   = schema
        )
        return conn
    except Exception as e:
        st.error("Failed to connect to Snowflake: {}".format(e))
        return None

# 接続を確認する
conn = snowflake_connection()
if conn is not None:
    st.success("Successfully connected to Snowflake!")
else:
    st.error("Failed to connect to Snowflake.")

# 入力したデータベース名・スキーマ名を選択
database_name = database
schema_name   = schema
table_name    = table

# Snowflakeに挿入したいファイルアップロード
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # pandasでCSVファイルを読み込む
    df        = pd.read_csv(uploaded_file)
    # カラム名を大文字にする
    dfcolumns = df.columns.str.upper()
    # 読み込んだデータを表示する
    st.write(df)

if st.button('OK !!!'):
    # Get available warehouses
    cursor     = conn.cursor()
    cursor.execute(f'USE WAREHOUSE {warehouse}')

    success, num_chunks, num_rows, output = write_pandas(
            conn       = conn,
            df         = df,
            database   = database_name,
            schema     = schema_name,
            table_name = table_name
        )
    st.success("Successfully upload to Snowflake!")

else:
    st.error("Failed to load the csv data ....")