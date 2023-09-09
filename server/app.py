import streamlit as st
import requests
from PIL import Image
from api import static

st.set_page_config(
    page_title='FPL Assistant',
    page_icon='⚽'
)

def get_img(id):
    if not id:
        return None
    img_url = f'https://resources.premierleague.com/premierleague/photos/players/250x250/p{id}.png'
    img = Image.open((requests.get(img_url, stream=True).raw))
    return img

def main():
    if 'static' not in st.session_state:
        st.session_state.static = static()
        st.session_state.elements = st.session_state.static.get_elements_summary()
    st.title('Welcome to FPL Assistant')
    most_selected = st.session_state.elements.sort_values(
        by=['selected_by_percent'], ascending=False).head()
    cols = ['web_name', 'selected_by_percent', 'total_points', 'now_cost']
    st.write(most_selected[cols])
    id_list = most_selected['code'].tolist()
    img_list = []
    for id in id_list:
        img_list.append(get_img(id))
    st.image(img_list, width=150)



if __name__ == '__main__':
    main()
