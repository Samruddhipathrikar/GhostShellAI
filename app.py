
import streamlit as st

from services.ghost_ai import get_ghost_response
from services.command_analyzer import analyze_command


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="GhostShell AI",
    page_icon="👻",
    layout="wide"
)


# --------------------------------------------------
# Haunted Terminal CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background:
            radial-gradient(circle at top, #17231b 0%, #090d0a 45%, #030504 100%);
    }

    /* Main container */
    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* Main title */
    .ghost-title {
        text-align: center;
        font-family: "Courier New", monospace;
        font-size: 3.5rem;
        font-weight: bold;
        color: #73ff9f;
        text-shadow:
            0 0 8px #39ff75,
            0 0 18px rgba(57, 255, 117, 0.45);
        margin-bottom: 0;
    }

    /* Subtitle */
    .ghost-subtitle {
        text-align: center;
        color: #a0b5a6;
        font-family: "Courier New", monospace;
        font-size: 1rem;
        margin-top: 5px;
        margin-bottom: 25px;
    }

    /* Terminal box */
    .terminal-header {
        background: #101510;
        border: 1px solid #29432f;
        border-bottom: none;
        border-radius: 12px 12px 0 0;
        padding: 12px 18px;
        color: #7dff9e;
        font-family: "Courier New", monospace;
    }

    .terminal-body {
        background: rgba(4, 9, 5, 0.92);
        border: 1px solid #29432f;
        border-radius: 0 0 12px 12px;
        padding: 20px;
        color: #b7ffc9;
        font-family: "Courier New", monospace;
        margin-bottom: 20px;
    }

    /* Streamlit input */
    div[data-baseweb="input"] > div {
        background-color: #080d09 !important;
        border: 1px solid #315f3c !important;
    }

    div[data-baseweb="input"] input {
        color: #8dffa8 !important;
        font-family: "Courier New", monospace;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        background: #102416;
        color: #7dff9e;
        border: 1px solid #3e9656;
        border-radius: 8px;
        font-family: "Courier New", monospace;
        font-weight: bold;
        transition: 0.2s;
    }

    .stButton > button:hover {
        color: white;
        border-color: #72ff98;
        box-shadow: 0 0 15px rgba(75, 255, 125, 0.30);
    }

    /* History */
    .history-card {
        background: rgba(8, 15, 10, 0.85);
        border-left: 3px solid #49c96d;
        padding: 12px 16px;
        border-radius: 6px;
        margin-bottom: 10px;
        font-family: "Courier New", monospace;
    }

    .history-command {
        color: #7dff9e;
        font-weight: bold;
    }

    .history-info {
        color: #879c8c;
        font-size: 0.85rem;
    }

    /* Small status */
    .online-status {
        color: #62ff8b;
        font-family: "Courier New", monospace;
        font-size: 0.9rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "history" not in st.session_state:
    st.session_state.history = []


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("👻 GhostShell")

    st.caption("The spirit inside your machine.")

    st.divider()

    st.markdown("### 🧠 AI Engine")

    st.write("**Model:** Llama 3.2 3B")
    st.write("**Runtime:** Ollama")
    st.write("**Mode:** Local")
    st.write("**Cloud API:** None")

    st.markdown(
        '<p class="online-status">● LOCAL SPIRIT ACTIVE</p>',
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("### 🔮 Spirit")

    personality = st.selectbox(
        "Personality",
        [
            "Whispering Ghost",
            "Angry Poltergeist",
            "Ancient Programmer"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### 🛡️ Safety")

    st.caption(
        "GhostShell analyzes commands but does not execute them."
    )

    if st.button("🗑️ Clear History"):
        st.session_state.history = []
        st.rerun()


# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<h1 class="ghost-title">👻 GhostShell AI</h1>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class="ghost-subtitle">
        There is something living inside your terminal...
        <br>
        Powered locally by open-weight AI.
    </p>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Terminal Header
# --------------------------------------------------

st.markdown(
    """
    <div class="terminal-header">
        ● &nbsp; ● &nbsp; ●
        &nbsp;&nbsp;
        GHOSTSHELL://LOCAL_TERMINAL
    </div>

    <div class="terminal-body">
        > SYSTEM: GhostShell initialized...<br>
        > MODEL: llama3.2:3b<br>
        > CONNECTION: LOCAL<br>
        > STATUS: Something is listening... 👻
    </div>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# Command Input
# --------------------------------------------------

st.markdown("### 💀 Speak to the machine")

command = st.text_input(
    "Terminal command",
    placeholder="> git status",
    label_visibility="collapsed"
)

summon = st.button(
    "👻 SUMMON THE GHOST"
)


# --------------------------------------------------
# Process Command
# --------------------------------------------------

if summon:

    if command.strip():

        analysis = analyze_command(command)

        st.divider()

        st.markdown("## 🔮 Command Reading")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Command Type",
                analysis["type"]
            )

        with col2:
            st.markdown("**Haunting Level**")
            st.write(
                analysis["haunting_level"]
            )

        with col3:
            st.markdown("**Spirit**")
            st.write(personality)

        if analysis["warning"]:
            st.warning(
                f"⚠️ {analysis['warning']}"
            )

        # AI response
        st.markdown("## 🕯️ The Machine Whispers...")

        with st.spinner(
            f"{personality} is awakening..."
        ):

            response = get_ghost_response(
                command,
                personality
            )

        st.markdown(
            f"""
            <div class="terminal-body">
                👻 {response}
            </div>
            """,
            unsafe_allow_html=True
        )

        # Save command
        st.session_state.history.insert(
            0,
            {
                "command": command,
                "type": analysis["type"],
                "personality": personality
            }
        )

    else:

        st.warning(
            "👻 The ghost cannot hear silence. "
            "Enter a command first."
        )


# --------------------------------------------------
# Command History
# --------------------------------------------------

if st.session_state.history:

    st.divider()

    st.markdown("## 📜 Haunted Command History")

    for item in st.session_state.history[:5]:

        st.markdown(
            f"""
            <div class="history-card">

                <div class="history-command">
                    > {item["command"]}
                </div>

                <div class="history-info">
                    Spirit: {item["personality"]}
                    &nbsp; | &nbsp;
                    Classification: {item["type"]}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# --------------------------------------------------
# Footer
# --------------------------------------------------

st.divider()

st.caption(
    "👻 GhostShell AI • Open-weight AI • "
    "Local inference • No cloud required"
)
