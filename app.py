import gradio as gr
import random

def career_simulator(name, stream, career, hours, skill):
    effort = hours
    skill_score = 5 if skill == "Yes" else 1
    luck = random.randint(1, 10)

    total = effort + skill_score + luck

    if total >= 20:
        result = f"🌟 {name}, you became highly successful in {career}!\nHigh Salary 💰 | High Satisfaction 😄"
    elif total >= 12:
        result = f"🙂 You built a stable career in {career}.\nMedium Salary 💼 | Medium Satisfaction 😊"
    else:
        result = f"😬 You struggled in {career}.\nLow Salary 📉 | Low Satisfaction 😕"

    return result

app = gr.Interface(
    fn=career_simulator,
    inputs=[
        gr.Textbox(label="Your Name"),
        gr.Dropdown(["Science", "Commerce", "Arts"], label="Stream"),
        gr.Textbox(label="Career Choice"),
        gr.Slider(1, 10, label="Study Hours"),
        gr.Radio(["Yes", "No"], label="Learn Extra Skills?")
    ],
    outputs="text",
    title="🎓 Career Journey Simulator"
)

app.launch()