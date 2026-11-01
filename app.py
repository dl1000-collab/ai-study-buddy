import streamlit as st

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

st.title("📚 AI Study Buddy")
st.caption("Your study assistant for making notes and revision")

tool = st.sidebar.radio(
    "Study Tools",
    ["Make Notes", "Chat with AI"]
)

if tool == "Make Notes":
    st.header("📝 Make Study Notes")

    topic = st.text_input("Enter your chapter or topic")
    school_class = st.selectbox(
        "Choose your class",
        ["Class 9", "Class 10", "Class 11", "Class 12", "Other"]
    )
    length = st.selectbox(
        "Notes length",
        ["Short", "Medium", "Detailed"]
    )

    if st.button("Prepare Notes"):
        if topic.strip():
            notes = f"""
# Study Notes: {topic}

**Class:** {school_class}
**Topic:** {topic}

## 1. Introduction
{topic} is the topic you have selected for study.
Write a short introduction using your textbook.

## 2. Key Points
- Understand the meaning of {topic}.
- Learn the important definitions.
- Identify the main concepts and facts.
- Review examples from your textbook.

## 3. Important Questions
1. What is {topic}?
2. Explain the main features of {topic}.
3. Describe the importance of {topic}.
4. Give suitable examples of {topic}.

## 4. Quick Revision
Revise the definitions, key points, examples,
and important questions from your textbook.

## 5. Study Tip
Read the chapter, add textbook facts to these notes,
and practise writing answers in your own words.
"""
            if length == "Short":
                notes = f"""# {topic}
Class: {school_class}

## Key Points
- Learn the definition of {topic}.
- Remember its main features.
- Revise important examples.

## Quick Questions
1. What is {topic}?
2. Why is it important?
"""
            elif length == "Detailed":
                notes += """

## 6. Further Study
- Add important dates, names, and facts.
- Include diagrams or examples where relevant.
- Review the chapter exercises.
- Practise long-answer questions.
"""

            st.markdown(notes)
            st.download_button(
                "Download Notes",
                data=notes,
                file_name="study_notes.txt",
                mime="text/plain"
            )
        else:
            st.warning("Please enter a topic first.")

elif tool == "Chat with AI":
    st.header("💬 Study Help")
    st.info(
        "This offline demo does not connect to a real AI model. "
        "Use the study prompts below to organise your learning."
    )

    question = st.text_input("Enter a study question")

    if st.button("Get Study Guide"):
        if question.strip():
            st.markdown(f"### Your question: {question}")
            st.markdown("""
**How to work through this question:**

1. Find the relevant chapter in your textbook.
2. Identify the important definition or concept.
3. Write the main points in your own words.
4. Add an example from your lesson.
5. Check your answer against your textbook.
""")
        else:
            st.warning("Please enter a question.")

st.sidebar.markdown("---")
st.sidebar.caption("Student learning project")
st.sidebar.caption("Works without an API key")