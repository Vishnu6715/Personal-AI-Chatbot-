import os, base64, time, smtplib
from email.message import EmailMessage

import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("Add GROQ_API_KEY in Streamlit Secrets or .env file")
    st.stop()

client = Groq(api_key=api_key)

st.set_page_config(
    page_title="Vishnu AI Assistant Pro",
    page_icon="🤖",
    layout="wide"
)

def file_to_base64(path):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return ""

def send_contact_email(name, email, message):
    email_user = st.secrets.get("EMAIL_USER") or os.getenv("EMAIL_USER")
    email_pass = st.secrets.get("EMAIL_PASS") or os.getenv("EMAIL_PASS")

    if not email_user or not email_pass:
        st.error("Add EMAIL_USER and EMAIL_PASS in Streamlit Secrets")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"📩 New Contact Request from {name}"
    msg["From"] = email_user
    msg["To"] = "vishnukumarvishnukumar919@gmail.com"
    msg["Reply-To"] = email

    msg.set_content(f"""
Hello Vishnu,

🎉 You have received a new contact request from your portfolio website.

----------------------------------------
👤 Name  : {name}
📧 Email : {email}

💬 Message:
{message}
----------------------------------------

You can reply directly to this email to contact the sender.

Regards,
Vishnu AI Portfolio
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_user, email_pass)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email sending failed: {e}")
        return False

    msg = EmailMessage()
    msg["Subject"] = f"New Portfolio Contact from {name}"
    msg["From"] = email_user
    msg["To"] = "vishnukumarvishnukumar919@gmail.com"

    msg.set_content(f"""
New message from your portfolio website:

Name: {name}
Email: {email}

Message:
{message}
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(email_user, email_pass)
            smtp.send_message(msg)
        return True
    except Exception as e:
        st.error(f"Email sending failed: {e}")
        return False

bg = file_to_base64("background.webp")

RESUME_DATA = """
Name: Vishnu Kumar V
Role: Full Stack Developer | AI Enthusiast
Education: B.E Electronics and Communication Engineering, Kongu Engineering College
Skills: C, Python, Java, HTML, CSS, JavaScript, Flutter, Basic ML, NLP, MySQL
Tools: VS Code, Android Studio
Projects:
1. One Step to Personalized Career Guidance - AI career guidance platform
2. Unique Eight Queen Challenge Game - logic puzzle game
3. Tamil AI Chatbot for Health Tips - Tamil NLP health chatbot
Achievements:
1st Prize - World Creativity and Invention Day
1st Prize - 24-Hour Hackathon, GCE Erode
2nd Prize - TECHIST Project Presentation
3rd Prize - PSG Project Presentation
Certifications:
NCC A Certificate, Data Analysis, Flutter Mobile App Development
Languages: English, Tamil, Malayalam Basic
"""

SYSTEM_PROMPT = f"""
You are Vishnu Kumar V's personal AI resume assistant.
Answer professionally and friendly based only on this resume data.

{RESUME_DATA}
"""

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]

st.markdown(f"""
<style>
.stApp {{
    background:
    linear-gradient(rgba(1,8,28,.88), rgba(1,8,28,.96)),
    url("data:image/webp;base64,{bg}");
    background-size: cover;
    background-attachment: fixed;
    color: #fff;
}}

.block-container {{
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}}

[data-testid="stSidebar"] {{
    background: rgba(1,10,35,.94);
    border-right: 1px solid rgba(56,189,248,.35);
}}

[data-testid="stSidebar"] * {{
    color: white;
}}

.logo {{
    font-size: 28px;
    font-weight: 900;
    background: linear-gradient(90deg,#ff4fd8,#38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.side-card {{
    padding: 13px 16px;
    margin: 10px 0;
    border-radius: 16px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.12);
}}

.hero-title {{
    font-size: 64px;
    font-weight: 950;
    background: linear-gradient(90deg,#18d9ff,#7c5cff,#ff4fd8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.card {{
    padding: 24px;
    border-radius: 24px;
    background: rgba(5,18,50,.76);
    border: 1px solid rgba(56,189,248,.28);
    box-shadow: 0 0 35px rgba(56,189,248,.14);
    backdrop-filter: blur(15px);
    margin-bottom: 20px;
}}

.mini-card {{
    padding: 18px;
    border-radius: 20px;
    background: rgba(255,255,255,.07);
    border: 1px solid rgba(255,255,255,.14);
    min-height: 120px;
}}

.badge {{
    display:inline-block;
    padding:8px 14px;
    border-radius:999px;
    background:rgba(56,189,248,.13);
    border:1px solid rgba(56,189,248,.35);
    margin:5px;
}}

.stat {{
    padding: 18px;
    border-radius: 18px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.15);
}}

.stButton button {{
    border-radius: 15px;
    background: linear-gradient(90deg,#ff4fd8,#4f46e5);
    color: white;
    border: none;
    padding: 10px 18px;
}}

.stTextInput input, .stTextArea textarea {{
    background: rgba(255,255,255,.08);
    color: white;
    border-radius: 12px;
}}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="logo">VISHNU AI</div>', unsafe_allow_html=True)
    st.caption("ASSISTANT PRO")

    st.markdown("""
    <div class="side-card">🏠 Home</div>
    <div class="side-card">🤖 AI Chat</div>
    <div class="side-card">📊 Skills</div>
    <div class="side-card">💼 Projects</div>
    <div class="side-card">🏆 Achievements</div>
    <div class="side-card">📜 Certificates</div>
    <div class="side-card">📄 Resume</div>
    <div class="side-card">📧 Contact</div>
    """, unsafe_allow_html=True)

    if os.path.exists("resume.pdf"):
        with open("resume.pdf", "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f,
                file_name="Vishnu_Kumar_Resume.pdf",
                mime="application/pdf"
            )

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        st.rerun()

top_left, top_right = st.columns([1.8, 1])

with top_left:
    st.markdown("""
    <br>
    <h4 style="color:#ff4fd8;">Hello, I'm</h4>
    <div class="hero-title">Vishnu Kumar V</div>
    <h3>Full Stack Developer | AI Enthusiast</h3>
    <p style="font-size:18px;color:#cbd5e1;">
    Welcome to my Personal AI Assistant. Ask anything about my skills,
    projects, achievements, education, and more.
    </p>
    <span class="badge">Python</span>
    <span class="badge">Streamlit</span>
    <span class="badge">Groq AI</span>
    <span class="badge">NLP</span>
    """, unsafe_allow_html=True)

with top_right:
    st.markdown("""
    <div class="card">
        <div class="stat">💼 <b>Experience</b><br>Fresher</div><br>
        <div class="stat">🚀 <b>Projects</b><br>3+</div><br>
        <div class="stat">🏆 <b>Achievements</b><br>4+</div><br>
        <div class="stat">📊 <b>Skills</b><br>10+</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("## 🤖 AI Resume Chat")

q1, q2, q3, q4 = st.columns(4)
prompt = None

if q1.button("Who is Vishnu?"):
    prompt = "Who is Vishnu Kumar?"
if q2.button("His skills?"):
    prompt = "What are Vishnu's technical skills?"
if q3.button("Projects"):
    prompt = "Explain Vishnu's projects."
if q4.button("Why hire him?"):
    prompt = "Why should we hire Vishnu?"

for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

user_input = st.chat_input("Ask me anything about my resume...")
final_prompt = prompt or user_input

if final_prompt:
    st.session_state.messages.append({"role": "user", "content": final_prompt})

    with st.chat_message("user"):
        st.write(final_prompt)

    with st.chat_message("assistant"):
        box = st.empty()
        box.markdown("🤖 AI is typing...")

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=st.session_state.messages,
            temperature=0.5,
            max_tokens=700
        )

        reply = response.choices[0].message.content
        typed = ""

        for word in reply.split():
            typed += word + " "
            box.write(typed)
            time.sleep(0.02)

    st.session_state.messages.append({"role": "assistant", "content": reply})

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("## 📊 My Skills")

skills = [
    ("Python", 90),
    ("HTML / CSS", 90),
    ("JavaScript", 85),
    ("Flutter", 80),
    ("AI / NLP", 75),
    ("MySQL", 70),
]

cols = st.columns(3)
for i, (skill, value) in enumerate(skills):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="mini-card">
            <h3>{skill}</h3>
            <h2>{value}%</h2>
        </div>
        """, unsafe_allow_html=True)
        st.progress(value)

st.markdown("## 📂 My Projects")

p1, p2, p3 = st.columns(3)

with p1:
    st.markdown("""
    <div class="mini-card">
    <h3>🚀 One Step to Career Guidance</h3>
    <p>AI-powered platform that helps students discover suitable career paths based on skills and interests.</p>
    <span class="badge">AI / ML</span>
    </div>
    """, unsafe_allow_html=True)

with p2:
    st.markdown("""
    <div class="mini-card">
    <h3>♛ Eight Queen Challenge Game</h3>
    <p>Logic-based puzzle game that improves strategic thinking and algorithmic problem solving.</p>
    <span class="badge">Java / Python</span>
    </div>
    """, unsafe_allow_html=True)

with p3:
    st.markdown("""
    <div class="mini-card">
    <h3>🤖 Tamil AI Chatbot</h3>
    <p>NLP chatbot that provides personalized health tips in Tamil language.</p>
    <span class="badge">NLP / Python</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("## 🏆 Achievements")

a1, a2, a3, a4 = st.columns(4)

achievements = [
    ("🥇", "1st Prize", "World Creativity and Invention Day"),
    ("🥇", "1st Prize", "24-Hour Hackathon, GCE Erode"),
    ("🥈", "2nd Prize", "TECHIST Project Presentation"),
    ("🥉", "3rd Prize", "PSG Project Presentation"),
]

for col, ach in zip([a1, a2, a3, a4], achievements):
    icon, title, desc = ach
    with col:
        st.markdown(f"""
        <div class="mini-card" style="text-align:center;">
            <h1>{icon}</h1>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

st.markdown("## 📧 Get In Touch")

c1, c2 = st.columns([1.4, 1])

with c1:
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        sent = st.form_submit_button("Send Message")

        if sent:
            if name and email and message:
                success = send_contact_email(name, email, message)
                if success:
                    st.success("✅ Message sent successfully! I will contact you soon.")
            else:
                st.warning("Please fill all details.")

with c2:
    st.markdown("""
    <div class="card">
    <h3>Contact Info</h3>
    <p>📧 Email: vishnukumarvishnukumar919@gmail.com</p>
    <p>📍 Location: Tamil Nadu, India</p>
    <p>💼 Role: Full Stack Developer</p>
    <p>🤖 Interest: AI, Web Development, Mobile Apps</p>
    </div>
    """, unsafe_allow_html=True)