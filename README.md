# streamlit_csv

直近の目標:streamlitの画面からcsvのアップロード出来るようにする

# 環境セットアップ

``` bash

conda create --name streamlit-csv -c https://repo.anaconda.com/pkgs/snowflake python=3.8 -y

conda activate streamlit-csv

conda install -c https://repo.anaconda.com/pkgs/snowflake snowflake-snowpark-python pandas notebook scikit-learn cachetools -y

pip install streamlit

!pip install awswrangler

streamlit run test.py

```
