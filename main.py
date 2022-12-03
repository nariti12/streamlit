import streamlit as st
import pandas as pd
from PIL import Image

st.title("Streamlit入門")

st.write("まんこ")

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})

st.dataframe(df.style.highlight_max(axis=0))

st.table(df.style.highlight_max(axis=0))


"""""
# ち
## ん
### こ

```python
port streamlit as st
import numpy as np
import pandas as pd
```
"""

st.write("ちんこ")

option = st.selectbox(
    'まんこです。',
    list(range(1,11))
)
"tinkomanko" ,option,"aaaa"


if st.checkbox("ちんぽこ"):
    img = Image.open("トムホラン-筋肉.jpg")
    st.image(img,caption = "maccho", use_column_width=True)

