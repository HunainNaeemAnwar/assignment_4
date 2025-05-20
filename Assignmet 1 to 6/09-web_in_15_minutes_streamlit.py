import streamlit as st

st.set_page_config(page_title="Text Analyzer", layout="centered")

st.title(" Text Analyzer Web App")

st.markdown("Enter your text below and choose transformations:")


user_input = st.text_area(" Write something here", height=200)


st.subheader(" Choose transformations:")
col1, col2, col3, col4 = st.columns(4)

with col1:
    upper = st.checkbox("UPPERCASE")
with col2:
    lower = st.checkbox("lowercase")
with col3:
    title_case = st.checkbox("Title Case")
with col4:
    remove_spaces = st.checkbox("Remove Extra Spaces")


if st.button("Analyze") and user_input:
   
    char_count = len(user_input)
    word_count = len(user_input.split())
    space_count = user_input.count(" ")

    st.subheader("Analysis:")
    st.write(f"**Characters:** {char_count}")
    st.write(f"**Words:** {word_count}")
    st.write(f"**Spaces:** {space_count}")

  
    transformed_text = user_input

    if remove_spaces:
        transformed_text = " ".join(transformed_text.split())
    if upper:
        transformed_text = transformed_text.upper()
    elif lower:
        transformed_text = transformed_text.lower()
    elif title_case:
        transformed_text = transformed_text.title()

    st.subheader("Transformed Text:")
    st.code(transformed_text)
elif user_input == "":
    st.info("Please enter some text.")
