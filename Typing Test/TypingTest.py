import streamlit as st
import time

def calculate_wpm(text, elapsed_time):
    num_words = len(text.split())
    wpm = int(num_words / (elapsed_time / 60)) if elapsed_time != 0 else 0
    return wpm

def main():
    st.set_page_config(page_title="📝 Typing Speed Test", page_icon="🚀")

    st.title("🏁 Typing Speed Test")

    st.header("🚴‍♂️ Test your Typing Speed and Accuracy")
    st.write("🔥 Practice makes perfect. Type the text below as fast and accurately as you can.")

    text_to_type = "The quick brown fox jumps over the lazy dog"
    st.subheader("📜 Text to Type:")
    st.markdown(f"<p style='text-align: center; font-size: 30px;'>{text_to_type}</p>", unsafe_allow_html=True)

    start_button = st.button("🚀 Start Test")

    if start_button:
        st.session_state.start_time = time.time()
        st.session_state.typing_started = True
        st.session_state.finished = False
        st.warning("⏰ Timer has started. Type the text below.")

    if st.session_state.get("typing_started") and not st.session_state.get("finished"):
        user_input = st.text_input("👉 Type here:")

        elapsed_time = time.time() - st.session_state.start_time
        wpm = calculate_wpm(text_to_type, elapsed_time)

        if user_input == text_to_type:
            st.success("🎉 Congratulations! You typed the text correctly.")
            st.subheader("🚀 Your Typing Speed:")
            st.write("WPM: {}".format(wpm))
            st.session_state.finished = True
        elif user_input:
            st.warning("⚠️ Oops! Your input doesn't match the text. Keep trying!")

        if st.button("🔄 Restart Test"):
            st.session_state.typing_started = False
            st.session_state.start_time = 0
            st.session_state.finished = False

    if not st.session_state.get("typing_started"):
        st.write("👇 Click the 'Start Test' button to begin.")
        st.session_state.finished = False

if __name__ == "__main__":
    main()
