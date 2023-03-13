import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "Please feel free to ask me anything"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "GAIA Research")

demo.launch(share=True)