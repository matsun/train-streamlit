import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit hello')

st.write('プログレスバー')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i+1)
  time.sleep(0.01)

'Done!!!'

st.write('DisplayImage')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに表示')
if button:
  right_column.write('右カラムだよー')

expander = st.expander('問い合わせ')
expander.write('問い合わせ')


text = st.text_input('趣味は?')
'趣味は', text, 'です。'

cond = st.slider('調子は', 1, 50, 4)
'調子は', cond, 'です'

option = st.selectbox(
  '好きな絵を指定してください',
  list(range(1,11))

)
'好きな数字は', option, 'です。'
# if st.checkbox('Show Image'):
#   img = Image.open('sample.jpg')
#   st.image(img, caption='hoge', use_column_width=True)

# df = pd.DataFrame({
#     '1列目': [1,2,3,4],
#     '2列目': [10,20,30,40]
# })

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# st.table(df.style.highlight_max(axis=0))

"""
# 賞
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

"""