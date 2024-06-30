import gradio as gr


def generate_pdf(prompt):
    from fpdf import FPDF

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, prompt)
    pdf_file = "/mnt/data/generated_prompt.pdf"
    pdf.output(pdf_file)
    return pdf_file


# Advanced features
def get_advanced_features():
    with gr.Accordion("Advanced Features", open=False):
        temp = gr.Slider(
            0.0,
            1.0,
            value=0.5,
            label="Model Temperature",
            step=0.05, interactive=True,
            info="Higher values produce more diverse outputs"
        )
        context_len = gr.Slider(
            0,
            2048,
            value=512,
            label="Context Length",
            step=64,
            interactive=True,
            info="The maximum numbers of tokens"
        )
    return temp, context_len


with gr.Blocks() as demo:
    gr.Markdown(
        """
        <center><h2>AI-Powered Prompt to PDF Generator</h2></center>
        <p>Welcome to the AI-Powered Prompt to PDF Generator! This tool allows you to select different AI models, customize their parameters, and generate personalized content in PDF format.</p>
        <p><b>Features:</b></p>
        <ul>
            <li>Select from various AI models</li>
            <li>Adjust advanced parameters like model temperature and context length</li>
            <li>Input your custom prompt to generate content</li>
            <li>Download the generated content as a PDF</li>
        </ul>
        <p><b>Note:</b> This tool is designed to help you experiment with different AI models and generate unique content based on your inputs. The process may take some time depending on the complexity of the prompt and model selected.</p>
        """
    )

    with gr.Tab("Select Model"):
        model_dropdown = gr.Dropdown(
            ["Model 1", "Model 2", "Model 3"],
            label="Select Model"
        )
        temperature, context_length = get_advanced_features()

    with gr.Tab("Model Selection"):
        model_radio = gr.Radio(
            ["Huggingface/ModelA", "Huggingface/ModelB", "Huggingface/ModelC"],
            label="Choose a Model"
        )

    with gr.Tab("Prompt"):
        prompt_text = gr.Textbox(
            label="Enter your prompt here",
            lines=10,
            placeholder="Type your prompt..."
        )

    with gr.Tab("Generate Output"):
        generate_button = gr.Button("Generate PDF")
        output_file = gr.File(label="Download your PDF")

        generate_button.click(generate_pdf, inputs=prompt_text, outputs=output_file)

demo.launch(share=True, show_api=False)


## some changes for testing purpose
