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
        ### Origin Story

        Hello! I'm Rafael. I'm part of a mildly intelligent species (arguably).  
        I possess XY chromosomes and currently inhabit a rocky planet the locals call **Earth**, in the **Milky Way galaxy**, right beside our neighbor **Andromeda**.

        Our ancestors took interest in this civilization -- the tech, the economy, the evolution, the chaos. 
        As their descendants, we continue their job: **observe, experiment, and contribute meaningful data back home**.


        ### Awakening of Interest

        In all seriousness, my entry to tech started with watching Michael Reeves on YouTube. 

        Yes. That guy.

        He made tech feel like a sandbox where the only real limit is how terrible an idea you're willing to execute.

        That idea stuck.


        ### Today

        I'm currently a **3rd Year Computer Science student** at **Cebu Institute of Technology - University**.

        I enjoy learning how systems work and how I can manipulate them to create things that are:

        - wacky
        - fun
        - or genuinely useful

        Sometimes all three at once.


        ### My Drive

        Technology is basically a superpower disguised as code + hardware.

        I want to use that superpower to build things that:

        - help my community
        - solve real problems
        - or at least make someone laugh

        **I believe tech has the power to build a better future, and I want to be part of that build process.**
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
    st.progress(20, text="DevOps (Willing to learn!)")

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

with st.expander("3D Earthquake Visualizer (Deck.gl)"):
    st.markdown(
        """
        - **Description:** An interactive 3D cartograph visualizing earthquake
          data for the Philippines.
        - **Tech Used:** TypeScript, Mapbox, Deck.gl, and React.
        """
    )
    st.link_button("View on GitHub", "https://github.com/GReturn/philippines-equake-locator-3d")


with st.expander("BuzyPC"):
    st.markdown(
        """
        - **Description:** An AI-powered PC builder Android app based on the user's budget.
        - **Tech Used:** Kotlin.
        """
    )
    st.link_button("View on GitHub", "https://github.com/GReturn/BuzyPC")

with st.expander("FeelNEETS"):
    st.markdown(
        """
        - **Description:** A Blazor web app that shows PhilNITS reviewers and answer keys from 2007 until 2025.
        - **Tech Used:** C#, .NET Blazor WebAssembly.
        """
    )
    st.link_button("View on GitHub", "https://github.com/GReturn/FeelNeets")

with st.expander("Sustaina"):
    st.markdown(
        """
        - **Description:** A real-time Android app platform that leverages AI to crowdsource 
        and visualize environmental issues.
        - **Tech Used:** Kotlin, Jetpack Compose, Google Maps API, Tensorflow, Firebase.
        """
    )
    st.link_button("View on GitHub", "https://github.com/Smoll05/hackaton-sustaina")


with st.expander("AIO Stubu"):
    st.markdown(
        """
        - **Description:** An All-In-One (AIO) Study Buddy (Stubu) desktop app. It is an 
            offline-first productivity desktop application for Windows that 
            equips students with essential study tools in one platform.
        - **Tech Used:** Java, JavaFX.
        """
    )
    st.link_button("View on GitHub", "https://github.com/liya28/AIOStuBu")


with st.expander("FinishLine"):
    st.markdown(
        """
        - **Description:** A JavaFX educational typing game. It is a school-based typing 
            game that improves typing proficiency while reinforcing 
            Computer Science concepts. 
        - **Tech Used:** Java, JavaFX, JDBC, MySQL.
        """
    )
    st.link_button("View on GitHub", "https://github.com/liya28/FinishLine")


with st.expander("QR Genie"):
    st.markdown(
        """
        - **Description:** A Java-based tool for batch QR code generation. Automates the 
            creation of QR codes from Excel input and integrated them 
            onto reference images. 
        - **Tech Used:** Java.
        """
    )
    st.link_button("View on GitHub", "https://github.com/GReturn/QR-Genie")

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
st.write("Please fill out the form to send me a message. Yes, this is functional (in a way).")

MY_EMAIL = "spongebobrafael@gmail.com"

with st.form("contact_form", clear_on_submit=True, enter_to_submit=False):
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
