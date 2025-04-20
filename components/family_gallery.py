import streamlit as st
import time
import random
from PIL import Image
from io import BytesIO

def show_family_gallery(family_data):
    st.write("Here are your family members!")

    # Create a smooth animation effect for the gallery
    cols = st.columns(3)  # Arrange images in 3 columns for a neat layout

    for i, member in enumerate(family_data):
        with cols[i % 3]:  # Distribute images across columns
            # Show uploaded image
            image = Image.open(BytesIO(member['image']))
            st.image(image, caption=member['name'], use_column_width=True)
            time.sleep(random.uniform(0.5, 1.5))  # Adding random delay for animation effect

            # Pronounce name (can be enhanced by adding audio functionality)
            st.write(f"Pronounced: {member['name']}")

    st.write("Enjoy the memories of your loved ones!")
