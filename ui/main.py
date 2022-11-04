import gradio as gr
from wrapper import *
from tweets_scraper import *

def create_options(tweets):
    ret = tweets.split("\n")
    for elem in ret:
        if elem == "" or elem == "\n":
            ret.remove(elem)
    return ret

with gr.Blocks() as demo:
    gr.Markdown("# NLP Project - Group 22")

    with gr.Accordion("Web Scraping Demo"):
        with gr.Column(scale=1):
            tweets_select_input = gr.Radio(label="number of tweets", choices=[6,12,18,24,30])
            tags_input = gr.CheckboxGroup(label="additional tags", choices=["Senate", "Senator", "US", "Midterms", "Fetterman", "Democrat", "Republican", "GOP", "Pennsylvania","stroke", "dog", "America", "vote"])

            scrape_submit_btn = gr.Button("Scrape", variant="primary")
            scrape_output = gr.Textbox(label="twitter scraping output")

    scrape_submit_btn.click(scrape_ui, inputs=[tweets_select_input, tags_input], outputs=scrape_output)

    with gr.Accordion("Subjectivity Analysis Demo"):
        with gr.Row():
            with gr.Column(scale=1):
                subj_text_input = gr.Textbox(label="input")
                with gr.Row():
                    subj_clear_btn = gr.Button("Clear")
                    subj_submit_btn = gr.Button("Submit", variant="primary")
                tweets_select = gr.Radio(label="scraped tweets")
            with gr.Column(scale=1):
                subj_output = gr.Label(label="output")
            
    subj_submit_btn.click(subjectivity_analysis, inputs=subj_text_input, outputs=subj_output)

    subj_clear_btn.click(fn=lambda value: gr.update(value=""), inputs=subj_submit_btn, outputs=subj_text_input)

    scrape_output.change(fn=lambda choices: gr.update(choices=create_options(choices)), inputs=scrape_output, outputs=tweets_select)
    tweets_select.change(fn=lambda value: gr.update(value=value), inputs=tweets_select, outputs=subj_text_input)
    

    with gr.Accordion("Sentiment Analysis Demo"):
        with gr.Row():
            with gr.Column(scale=1):
                senti_text_input = gr.Textbox(label="input")
                with gr.Row():
                    senti_clear_btn = gr.Button("Clear")
                    senti_submit_btn = gr.Button("Submit", variant="primary")
                tweets_select = gr.Radio(label="scraped tweets")
            with gr.Column(scale=1):
                senti_output = gr.Label(label="output")
            
    senti_submit_btn.click(sentiment_analysis, inputs=senti_text_input, outputs=senti_output)

    senti_clear_btn.click(fn=lambda value: gr.update(value=""), inputs=senti_submit_btn, outputs=senti_text_input)

    scrape_output.change(fn=lambda choices: gr.update(choices=create_options(choices)), inputs=scrape_output, outputs=tweets_select)
    tweets_select.change(fn=lambda value: gr.update(value=value), inputs=tweets_select, outputs=senti_text_input)


    with gr.Accordion("Sarcasm Analysis Demo"):
        with gr.Row():
            with gr.Column(scale=1):
                sarcas_text_input = gr.Textbox(label="input")
                with gr.Row():
                    sarcas_clear_btn = gr.Button("Clear")
                    sarcas_submit_btn = gr.Button("Submit", variant="primary")
                tweets_select = gr.Radio(label="scraped tweets")
            with gr.Column(scale=1):
                sarcas_output = gr.Label(label="output")
            
    sarcas_submit_btn.click(sarcasm_analysis, inputs=sarcas_text_input, outputs=sarcas_output)

    sarcas_clear_btn.click(fn=lambda value: gr.update(value=""), inputs=sarcas_submit_btn, outputs=sarcas_text_input)

    scrape_output.change(fn=lambda choices: gr.update(choices=create_options(choices)), inputs=scrape_output, outputs=tweets_select)
    tweets_select.change(fn=lambda value: gr.update(value=value), inputs=tweets_select, outputs=sarcas_text_input)


    with gr.Accordion("Joint Analysis Demo"):
        with gr.Row():
            with gr.Column(scale=1):
                joint_text_input = gr.Textbox(label="input")
                with gr.Row():
                    joint_clear_btn = gr.Button("Clear")
                    joint_submit_btn = gr.Button("Submit", variant="primary")
                tweets_select = gr.Radio(label="scraped tweets")
            with gr.Column(scale=1):
                joint_faction_output = gr.Label(label="faction output")
                joint_sentiment_output = gr.Label(label="sentiment output")
            
    joint_submit_btn.click(fn=lambda value: gr.update(value=joint_analysis(value)[0]), inputs=joint_text_input, outputs=joint_faction_output)
    joint_submit_btn.click(fn=lambda value: gr.update(value=joint_analysis(value)[1]), inputs=joint_text_input, outputs=joint_sentiment_output)

    joint_clear_btn.click(fn=lambda value: gr.update(value=""), inputs=joint_submit_btn, outputs=joint_text_input)

    scrape_output.change(fn=lambda choices: gr.update(choices=create_options(choices)), inputs=scrape_output, outputs=tweets_select)
    tweets_select.change(fn=lambda value: gr.update(value=value), inputs=tweets_select, outputs=joint_text_input)

demo.launch()
