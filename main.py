import streamlit as st
import params
import helper_funcs
from pathlib import Path

def set_page_config():
    st.set_page_config(
        page_title = "Traffic Signs Detection using YOLOv8",
        page_icon= ":no_bicycles:",
        layout= "wide",
        initial_sidebar_state= "expanded"
    )

def main():
    set_page_config()
    st.title("Traffic Signs Detection using YOLOv8")
    st.markdown("---")

    hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_st_style, unsafe_allow_html=True)

    with st.sidebar:
        st.header("Model Configurations")
        conf = float(st.slider("Confidence Level", 0, 100, 40)) / 100
        st.markdown("---")

    model_path = Path(params.MODEL_DIR)

    try:
        model = helper_funcs.load_model(model_path)
    except Exception as e:
        st.error("Unable to load model.")
        st.error(e)

    st.sidebar.header("Image/Video Configurations")
    rb_source = st.sidebar.radio("Select Source", params.SOURCES_LIST)
    source_img = None

    if rb_source == params.IMAGE:
        helper_funcs.detect_objects_in_image(conf,model)

    elif rb_source == params.VIDEO:
        helper_funcs.detect_objects_in_video(conf, model)

    else:
        st.error("Please select a valid source!")

if __name__ == '__main__':
    main()