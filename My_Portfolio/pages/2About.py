import streamlit as st
import subprocess

st.set_page_config(
    page_title="Sakshi Savle Portfolio",
    page_icon="🕶️", 
)
st.markdown("# About")
#st.sidebar.markdown("# About")



st.write("""##### I am a passionate computer science engineering student with a keen interest in artificial intelligence and machine learning.I am particularly fascinated by robotics and drone technology.Aspire to contribute towards advancements in these areas.I am driven by curiosity to explore innovative solutions and technology that can revolutionize the way we interact with the world.I am commited to continous learning and growth in order to make a meaningful impact in the field of technology.""")
st.write("---")
program_skill,soft_skill=st.columns(2)
with program_skill:
    st.write("""##### Programming skill \n
- ##### Python \n - ##### SQL \n - ##### C language \n - ##### Frontend web development""")
   

with soft_skill:
    st.write("""##### Soft skill \n
- ##### Problem solving \n - ##### Leadership \n - ##### Team work \n - ##### Presentation skill """)

filename="pages\Sakshi_Savle.pdf"
#def MY_CV(filename):
if st.button("MY_CV"):
    try:
        subprocess.Popen(["start", filename], shell=True)
    except Exception as e:
        st.error(f"Error:{e}")







#st.write(f"{p_skill}")
#st.write("""##### Hello """)
#st.write(f'<div class="title"><center> hello </center> </div>', unsafe_allow_html=True)

#st.button("MY_CV",)
 




