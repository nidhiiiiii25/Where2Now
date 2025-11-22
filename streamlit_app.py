import streamlit as st
st.markdown("""
<style>
    .main {
        background-color: #0d1117;
    }
    textarea {
        font-size: 1.1rem !important;
    }
</style>
""", unsafe_allow_html=True)


# -------------- BASIC PAGE SETUP --------------
st.set_page_config(
    page_title="Where2Now",
    page_icon="✈️",
    layout="centered"
)

# -------------- MAIN APP FUNCTION --------------
def main():
    # Centered title with emojis
    st.markdown(
        """
        <h1 style="text-align: center; font-size: 3rem;">
            ✈️ Where2Now 🌍
        </h1>
        """,
        unsafe_allow_html=True,
    )

    # Tagline
    st.markdown(
        """
        <p style="text-align: center; font-size: 1.2rem; color: #666;">
            Your trip. My plan.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Prompt text - Gen Z + clean
    st.markdown("### Where are we vibing next? 👀")

    # Input box for user
    user_input = st.text_input(
        "Tell me your travel thoughts (example: “I’m going to Bangalore, plan my trip”)",
        placeholder="I’m going to Bangalore, what’s the weather and where can I go?"
    )

    # Button to trigger response
    from agents.tourism_agent import tourism_agent

# Button to trigger response
    if st.button("Ask Where2Now"):
        if not user_input.strip():
            st.warning("Type something first so I know where we're heading 🙂")
        else:
            answer = tourism_agent(user_input)
            st.markdown(answer)

    # A small footer
    st.markdown(
        """
        <p style="text-align: center; font-size: 0.9rem; color: #999; margin-top: 3rem;">
            Where2Now • Prototype Step 1 • UI + Vibe only
        </p>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
