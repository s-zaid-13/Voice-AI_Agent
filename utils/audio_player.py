import base64
import time

import streamlit as st
import streamlit.components.v1 as components


def autoplay_audio(audio_bytes: bytes) -> None:
    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    audio_id = f"tts_{int(time.time() * 1000)}"

    html = f"""
    <audio id="{audio_id}" autoplay style="display:none;">
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
    </audio>

    <script>
    (function() {{
        const audio = document.getElementById("{audio_id}");

        if (audio) {{
            audio.play().catch(error => {{
                console.error(error);
            }});
        }}
    }})();
    </script>
    """

    components.html(html, height=0)
