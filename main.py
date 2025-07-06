import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ahmed Selim | Data Engineer",
    layout="wide",
    page_icon=":bar_chart:"
)

# Initialize session state for navigation
if 'current_section' not in st.session_state:
    st.session_state.current_section = 'Home'

# Custom CSS for modern look
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fa;
        }
        .project-card {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(44,123,229,0.08);
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        .project-title {
            color: #2c7be5;
            font-size: 1.3rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        .project-desc {
            color: #444;
            font-size: 1.05rem;
            margin-bottom: 1rem;
        }
        .contact-link {
            color: #2c7be5;
            text-decoration: none;
            font-weight: 600;
        }
        .nav-button {
            background: none;
            border: none;
            color: #2c7be5;
            font-size: 1rem;
            cursor: pointer;
            padding: 0.5rem 0;
            width: 100%;
            text-align: left;
        }
        .nav-button:hover {
            color: #1a5bb8;
        }
        .active-nav {
            color: #1a5bb8;
            font-weight: bold;
        }
        .section-divider {
            margin: 80px 0;
            border-top: 3px solid #2c7be5;
            padding-top: 40px;
        }
        .section-header {
            color: #2c7be5;
            font-size: 2.5rem;
            margin-bottom: 30px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with clickable navigation
with st.sidebar:
    st.markdown("## Ahmed Selim")
    st.markdown("**Python Developer & Data Engineer**")
    st.markdown("---")
    
    # Home button
    if st.button("🏡 Home", key="home_btn", use_container_width=True):
        st.session_state.current_section = 'Home'
    
    # Projects button
    if st.button("💼 Projects", key="projects_btn", use_container_width=True):
        st.session_state.current_section = 'Projects'
    
    st.markdown("[📧 Contact Me](mailto:ahmedselimelsayed@gmail.com)")
    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.9rem; color:#888;'>© 2024 Ahmed Selim</div>",
        unsafe_allow_html=True
    )
    
    # Current section indicator
    st.markdown(f"**Current: {st.session_state.current_section}**")

# Main content - All sections displayed
st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

# HOME SECTION
home_container = st.container()
with home_container:
    st.markdown('<div id="home"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">🏡 Home</h1>', unsafe_allow_html=True)
    
    # Center content in columns
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.title("Ahmed Selim")
        st.subheader("Python Developer & Data Engineer")
        st.markdown("""
            <p style="font-size:1.1rem; color:#444;">
            I am a Python developer and data engineer passionate about building scalable data solutions and creating efficient software.<br><br>
            With several years of experience in the tech industry, I specialize in designing, developing, and maintaining robust data pipelines and backend systems. My expertise includes working with cloud platforms, automating workflows, and leveraging modern data engineering tools to solve complex business problems.<br><br>
            I enjoy collaborating with cross-functional teams to deliver impactful solutions, and I am always eager to learn new technologies and best practices. My goal is to contribute to innovative projects that drive data-driven decision making and operational excellence.
            </p>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-top: 30px; font-size: 1.1rem; color: #444;">
                <strong>Below you will find some of the apps I have built.</strong>
                <span style="color: #2c7be5;"> Feel free to contact me for collaboration or inquiries!</span>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
            <div style="margin-top: 30px;">
                <a href="mailto:ahmedselimelsayed@gmail.com" class="contact-link">📧 Email Me</a>
            </div>
        """, unsafe_allow_html=True)
        
        # Quick link to projects
        if st.button("View My Projects Below 🚀", key="view_projects", use_container_width=True):
            st.session_state.current_section = 'Projects'
            st.rerun()

# SECTION DIVIDER
st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# PROJECTS SECTION
projects_container = st.container()
with projects_container:
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown('<h1 class="section-header">💼 My Projects</h1>', unsafe_allow_html=True)
    
    # Check if data.csv exists
    try:
        df = pd.read_csv("data.csv")
        
        if len(df) == 0:
            st.warning("No projects found in data.csv")
        else:
            # Create columns for projects
            project_cols = st.columns(2, gap="large")
            
            for idx, row in df.iterrows():
                with project_cols[idx % 2]:
                    st.markdown(f"""
                        <div class="project-card">
                            <div class="project-title">{row["title"]}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    # Handle image display with error handling
                    try:
                        st.image(f"images/{row['image']}", use_container_width=True, caption=None)
                    except Exception as e:
                        st.warning(f"Could not load image: {row['image']}")
                    
                    st.markdown(f"""
                        <div class="project-desc">{row["description"]}</div>
                        <a href="{row['url']}" target="_blank" class="contact-link">🔗 Source Code</a>
                    """, unsafe_allow_html=True)
    
    except FileNotFoundError:
        st.error("data.csv file not found. Please make sure the file exists in the project directory.")
        st.info("Create a data.csv file with columns: title, description, image, url")
        
        # Show sample data structure
        st.markdown("**Sample data.csv structure:**")
        sample_data = {
            "title": ["Project 1", "Project 2"],
            "description": ["Description of project 1", "Description of project 2"],
            "image": ["project1.png", "project2.png"],
            "url": ["https://github.com/user/project1", "https://github.com/user/project2"]
        }
        st.dataframe(pd.DataFrame(sample_data))
    
    except Exception as e:
        st.error(f"Error loading projects: {str(e)}")
    
    # Back to home button
    st.markdown("---")
    if st.button("↑ Back to Home", key="back_home", use_container_width=True):
        st.session_state.current_section = 'Home'
        st.rerun()

# Add some spacing at the bottom
st.markdown("<div style='margin-bottom: 100px;'></div>", unsafe_allow_html=True)

# Auto-scroll to section based on sidebar selection
if st.session_state.current_section == 'Projects':
    st.markdown("""
        <script>
            document.getElementById('projects').scrollIntoView({behavior: 'smooth'});
        </script>
    """, unsafe_allow_html=True)
elif st.session_state.current_section == 'Home':
    st.markdown("""
        <script>
            document.getElementById('home').scrollIntoView({behavior: 'smooth'});
        </script>
    """, unsafe_allow_html=True)