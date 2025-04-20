import streamlit as st
from io import BytesIO

def show_memory_backstory(family_data):
    # Iterate through the family data and show the backstory of each member
    for member in family_data:
        st.write(f"#### {member['name']}'s Childhood Memory")
        st.write(f"{member['memory']}")
        st.write("---")

        # Play voice recording
        st.write(f"Click the button below to hear {member['name']}'s voice:")
        audio_data = BytesIO(member['voice'])
        st.audio(audio_data, format="audio/mp3")

        st.write("### Play Memory in Their Voice")
        if st.button(f"Play {member['name']}'s Memory"):
            st.audio(audio_data, format="audio/mp3")

