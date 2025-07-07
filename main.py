import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Ahmed Selim | Data Engineer",
    layout="wide",
    page_icon=":bar_chart:"
)

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

# Sidebar with navigation
with st.sidebar:
    st.markdown("## Ahmed Selim")
    st.markdown("**Python Developer & Data Engineer**")
    st.markdown("---")
    
    # Navigation links
    st.markdown("### 🧭 Navigation")
    st.markdown("[🏡 Home](http://localhost:8501)")
    st.markdown("[📧 Contact](http://localhost:8502)")
    
    st.markdown("---")
    st.markdown(
        "<div style='font-size:0.9rem; color:#888;'>© 2024 Ahmed Selim</div>",
        unsafe_allow_html=True
    )

# HOME PAGE WITH PROJECTS
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
        
        # Quick link to contact
        st.markdown("""
            <div style="margin-top: 30px; text-align: center;">
                <a href="http://localhost:8502" target="_blank" class="contact-link" style="background: #2c7be5; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">
                    📧 Contact Me
                </a>
            </div>
        """, unsafe_allow_html=True)

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

# Add some spacing at the bottom
st.markdown("<div style='margin-bottom: 100px;'></div>", unsafe_allow_html=True)