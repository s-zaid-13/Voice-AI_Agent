import streamlit as st
from streamlit_mic_recorder import mic_recorder

from agent import VoiceAgent
from utils.audio_player import autoplay_audio

st.set_page_config(
    page_title="Real-Time Voice AI Agent", page_icon="🎙️", layout="centered"
)


if "agent" not in st.session_state:
    st.session_state.agent = VoiceAgent()

if "latest_audio" not in st.session_state:
    st.session_state.latest_audio = None

if "last_recording_id" not in st.session_state:
    st.session_state.last_recording_id = None

if "processing" not in st.session_state:
    st.session_state.processing = False

agent = st.session_state.agent


with st.sidebar:

    st.title("🎙️ Voice AI Agent")

    if st.button(
        "🗑 Clear Conversation",
        use_container_width=True,
    ):
        agent.conversation.clear()
        st.session_state.latest_audio = None
        st.session_state.last_recording_id = None
        st.rerun()

    st.divider()

    st.markdown("""
    ### Tech Stack

    - Groq Whisper
    - Gemini
    - ElevenLabs
    - Streamlit
    - Browser MediaRecorder
    """)

left, right = st.columns([4, 1])

with left:
    st.title("🎙️ Real-Time Voice AI Agent")
    st.caption("Powered by Groq Whisper • Gemini • ElevenLabs")

with right:
    st.metric(
        "Status",
        "Ready" if not st.session_state.processing else "Processing",
    )

st.divider()

st.markdown(
    """
<div style="
padding:18px;
border-radius:14px;
border:1px solid #2E8BFF;
background:rgba(46,139,255,0.08);
">

### 👋 Welcome

Click **Start Talking**, speak naturally, then press **Stop & Send**.

Your conversation history is automatically remembered.

</div>
""",
    unsafe_allow_html=True,
)

with st.container(border=True):

    st.subheader("💬 Conversation")

    for message in agent.conversation.get_messages():

        if message["role"] == "system":
            continue

        avatar = "🧑" if message["role"] == "user" else "🤖"

        with st.chat_message(
            message["role"],
            avatar=avatar,
        ):
            st.markdown(message["content"])


if st.session_state.latest_audio is not None:

    autoplay_audio(
        st.session_state.latest_audio,
    )

    st.session_state.latest_audio = None


with st.expander("🎤 Voice Recorder", expanded=True):
    audio = mic_recorder(
        start_prompt="🎙️ Start Talking",
        stop_prompt="⏹️ Stop & Send",
        use_container_width=True,
        key="voice_recorder",
    )


if (
    audio
    and audio.get("id") != st.session_state.last_recording_id
    and not st.session_state.processing
):

    st.session_state.processing = True
    st.session_state.last_recording_id = audio["id"]

    try:

        with st.status(
            "Processing your request...",
            expanded=True,
        ) as status:
            progress = st.progress(0)
            status.write("💾 Saving recording...")
            progress.progress(20)
            audio_path = agent.recorder.save(
                audio_bytes=audio["bytes"],
                input_format=audio["format"],
            )

            status.write("📝 Transcribing speech...")
            progress.progress(45)
            transcript = agent.transcribe(audio_path)

            status.write("🧠 Thinking...")
            progress.progress(70)

            response = agent.generate_response(transcript)

            status.write("🔊 Generating voice...")
            progress.progress(90)

            response_audio = agent.generate_audio(response)

            status.update(label="Completed", state="complete")
            progress.progress(100)
            progress.empty()

        st.session_state.latest_audio = response_audio.read_bytes()

    except Exception as exc:

        st.error(str(exc))

    finally:

        st.session_state.processing = False

    st.rerun()


st.divider()

col1, col2 = st.columns(2)

with col1:
    st.caption("🎙️ Real-Time Voice AI Agent")

with col2:
    st.caption("Built with ❤️ using Groq • Gemini • ElevenLabs")
