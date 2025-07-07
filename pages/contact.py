import streamlit as st

st.set_page_config(
    page_title="Contact - Ahmed Selim | Data Engineer",
    layout="wide",
    page_icon="📧"
)

# Custom CSS for modern look
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fa;
        }
        .contact-link {
            color: #2c7be5;
            text-decoration: none;
            font-weight: 600;
        }
        .section-header {
            color: #2c7be5;
            font-size: 2.5rem;
            margin-bottom: 30px;
            text-align: center;
        }
        .contact-form {
            background: #fff;
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(44,123,229,0.08);
            padding: 2rem;
            margin: 2rem 0;
        }
        .form-field {
            margin-bottom: 1.5rem;
        }
        .form-label {
            color: #2c7be5;
            font-weight: 600;
            margin-bottom: 0.5rem;
            display: block;
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

# CONTACT PAGE
st.markdown("<div style='margin-top: 60px;'></div>", unsafe_allow_html=True)

# Contact header
st.markdown('<h1 class="section-header">📧 Contact Me</h1>', unsafe_allow_html=True)

# Center contact form
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
        <div class="contact-form">
            <p style="font-size:1.2rem; color:#2c7be5; text-align:center; margin-bottom:30px;">
                <strong>Let's Connect!</strong><br>
                I'd love to hear from you. Send me a message and I'll get back to you as soon as possible.
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Contact form
    with st.form("contact_form"):
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        name = st.text_input("👤 Your Name", placeholder="Enter your full name")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        email = st.text_input("📧 Your Email", placeholder="Enter your email address")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        subject = st.text_input("📝 Subject", placeholder="What's this about?")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="form-field">', unsafe_allow_html=True)
        message = st.text_area("💬 Message", placeholder="Tell me about your project or inquiry...", height=150)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Form submission
        submitted = st.form_submit_button("Send Message 🚀", use_container_width=True)
        
        if submitted:
            if name and email and subject and message:
                st.success("✅ Thank you for your message! I'll get back to you soon.")
                st.balloons()
                
                # Here you would typically send the email or save to database
                # For now, we'll just show the submitted data
                st.markdown("---")
                st.markdown("**Message Details:**")
                st.write(f"**Name:** {name}")
                st.write(f"**Email:** {email}")
                st.write(f"**Subject:** {subject}")
                st.write(f"**Message:** {message}")
            else:
                st.error("❌ Please fill in all fields before sending.")
    
    # Alternative contact methods
    st.markdown("---")
    st.markdown("""
        <div style="text-align:center; margin-top:30px;">
            <h3 style="color:#2c7be5;">Other Ways to Reach Me</h3>
            <p style="font-size:1.1rem;">
                <a href="mailto:ahmedselimelsayed@gmail.com" class="contact-link">📧 Direct Email</a><br><br>
                <a href="https://linkedin.com/in/yourprofile" class="contact-link" target="_blank">💼 LinkedIn</a><br><br>
                <a href="https://github.com/yourusername" class="contact-link" target="_blank">🐙 GitHub</a>
            </p>
        </div>
    """, unsafe_allow_html=True)
    
    # Back to home button
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center;">
            <a href="http://localhost:8501" target="_blank" class="contact-link" style="background: #2c7be5; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">
                ← Back to Home
            </a>
        </div>
    """, unsafe_allow_html=True)