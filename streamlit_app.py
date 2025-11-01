import streamlit as st
import pandas as pd
import urllib.parse

st.set_page_config(
    page_title="My Portfolio",
    page_icon="☝️",
    # layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/66846143?v=4", width=200)
    st.header("Connect with Me")
    
    st.link_button("LinkedIn", "https://www.linkedin.com/in/rafael-mendoza-8a5788254/", use_container_width=True)
    st.link_button("GitHub", "https://github.com/GReturn", use_container_width=True)
    st.link_button("Email", "mailto:spongebobrafael@gmail.com", use_container_width=True)
    
    st.divider()
    
    st.header("Download My Resume")
    
    with open("Resume.pdf", "rb") as file:
        st.download_button(
            label="Download Resume (PDF)",
            data=file,
            file_name="Resume.pdf",
            mime="application/octet-stream",
            use_container_width=True,
        )

col1, col2 = st.columns([1.5, 2.5])

with col1:
    st.image("https://avatars.githubusercontent.com/u/66846143?v=4", width=300)

with col2:
    st.title("Rafael Mendoza")
    st.subheader("Computer Science Undergrad Student")
    st.markdown(
        """
        I am a passionate coder with interests in software development,
        project management, and DevOps. This portfolio is built with Streamlit 
        in compliance of a school assignment.
        """
    )

st.divider()

# Autobio & Skills

tab1, tab2 = st.tabs(["Autobiography", "My Skills"])

with tab1:
    st.header("My Story")
    st.markdown(
        """
        Hello! I'm Rafael, I'm part of the species with high intelligence 
        and I have the XY chromosomes in my genetic data. 
        I live in a rocky planet, which the locals may call "Earth" in the 
        galaxy of Milky Way: the neighboring galaxy of Andromeda, 
        where my home planet could be located. The technological, economical, 
        natural, and evolutionary advancements here on Earth piqued the interests 
        of my ancestors. As their newborn descendants, we are tasked 
        to research and provide valuable data to those at home. 
        
        In all seriousness, my journey into the world of tech
        started with watching YouTube videos by Michael Reeves.
        I truly believe that with tech, I can create something fun, wacky, 
        or useful for me and/or to my community. 
        
        I'm currently a Third Year Computer Science student at 
        the Cebu Institute of Technology University.
        
        What drives me is the power of technology to build a better future.
    
        """
    )

with tab2:
    st.header("Technical Skills")
    
    skill_col1, skill_col2 = st.columns(2)
    
    with skill_col1:
        st.subheader("Platform Development")
        st.markdown(
            """
            - **Mobile:** (Kotlin, Jetpack Compose)
            - **Desktop (Windows):** (WPF, WinForms, JavaFX)
            - **Web:** (React, TypeScript)
            """
        )
        
    with skill_col2:
        st.subheader("Software Development")
        st.markdown(
            """
            - **Backend:** (Java, C#, Python, REST APIs)
            - **Visualization:** (Deck.gl, Seaborn)
            - **Tools:** (Git, Docker, VS Code)
            """
        )
        
    st.subheader("Skill Proficiency")
    st.write("A self-assessment of my key technical skills.")
    st.progress(100, text="LLM Prompting 🙄")
    st.progress(80, text="Software Development")
    st.progress(20, text="DevOps")

st.divider()

# Github Activity
st.header("My GitHub Activity")
st.write("Here's a look at my coding activity and top languages.")

github_username = "GReturn"

col1, col2 = st.columns(2)
with col1:
    st.subheader("GitHub Stats")
    st.markdown(
        f"![GitHub Stats](https://github-readme-stats.vercel.app/api?username={github_username}&show_icons=true&theme=transparent&hide_border=true&title_color=FF4B4B&text_color=FFFFFF&icon_color=FF4B4B)",
        unsafe_allow_html=True
    )
with col2:
    st.subheader("Top Languages")
    st.markdown(
        f"![Top Languages](https://github-readme-stats.vercel.app/api/top-langs/?username={github_username}&&hide_border=true&title_color=FF4B4B&text_color=FFFFFF&icon_color=FF9900&theme=transparent&langs_count=6&hide=Assembly,CSS,HTML&layout=compact)",
        unsafe_allow_html=True
    )

st.divider()

# Expanders
st.header("My Projects")
st.write("Click to expand and learn more about my work.")

with st.expander("Project 1: 3D Earthquake Visualizer (Deck.gl)"):
    st.markdown(
        """
        - **Description:** An interactive 3D cartograph visualizing earthquake
          data for the Philippines, built with Streamlit and Deck.gl.
        - **Tech Used:** TypeScript, Mapbox, Deck.gl, and React.
        """
    )
    st.link_button("View on GitHub", "https://github.com/GReturn/philippines-equake-locator-3d")



st.divider()

# Location
st.header("Where I Take My Education")
st.write("Once again, I am taking up my undergraduate studies at the Cebu Institute of Technology University.")

location_data = pd.DataFrame({
    'lat': [10.2941678],
    'lon': [123.8813376]
})

st.map(location_data, zoom=10)
st.caption("A map showing my university's location.")


st.divider()

# Contak
st.header("Get In Touch!")
st.write("Please fill out the form to send me a message.")

MY_EMAIL = "spongebobrafael@gmail.com"

with st.form("contact_form", clear_on_submit=True):
    name = st.text_input("Your Name", placeholder="Juan C. Dela Cruz")
    email = st.text_input("Your Email", placeholder="juandelacruz@gmail.com")
    message = st.text_area("Your Message", placeholder="Your message here...")
    
    submitted = st.form_submit_button("Create Email Draft")
    
    if submitted:
        if not name or not email or not message:
            st.warning("Please fill out all the fields to create the email draft.")
        else:
            st.balloons()

            subject = f"Portfolio Contact - From {name}"
            body = (
                f"Hello,\n\n"
                f"My name is {name} and my email is {email}.\n\n"
                f"Message:\n{message}\n"
            )

            encoded_subject = urllib.parse.quote(subject)
            encoded_body = urllib.parse.quote(body)

            mailto_link = f"mailto:{MY_EMAIL}?subject={encoded_subject}&body={encoded_body}"
            st.success("Draft ready! Click the button below to open your email client.")
            st.link_button("Click here to open your email", mailto_link, use_container_width=True)

st.caption("© 2025 Rafael Mendoza | Built with Streamlit")