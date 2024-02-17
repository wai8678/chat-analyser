import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt



st.sidebar.title("CHAT ANALZER")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    data=bytes_data.decode("utf-8")
    df= preprocessor.preprocess(data)

    st.dataframe(df)

    user_list=df['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Overall")

    selected_user=st.sidebar.selectbox("Show analysis of Whom ?",user_list)
    if st.sidebar.button("SHOW ANALYSIS"):

        num_messages,words,num_media_messages=helper.fetch_stats(selected_user,df)
        col1 , col2 , col3 =st.columns(3)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)
        with col2:
            st.header("Total words")
            st.title(words)

        with col3:
            st.header("Total media shared ")
            st.title(num_media_messages)


        #buisest
        if selected_user=='overall':
            st.title('Most busy users')
            x = helper.most_busy_users(df)
            fig , ax =plt.subplots()

            col1,col2=st.columns(2)

            with col1:
                ax.bar(x.index, x.values)
                plt.xticks(rotation='vertical')
                st.pyplot(fig)
