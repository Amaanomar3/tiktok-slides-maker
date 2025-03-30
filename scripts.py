import openai


class scripts:

    def generate_subtitles(script, model="gpt-3.5-turbo",max_chars=100):
        """
        Generates AI-enhanced subtitles from the provided script and splits them into slides.
        :param script: The input script to generate subtitles from.
        :param model: The AI model to use for the text generation.
        :param max_chars: The max character count per slide.
        :return: A list of slides with subtitles.
        """
        response = openai.ChatCompletion.create(
                model = model,
                messages=[
                    {"role": "system", "content" : "Generate engagaging subtitles from the given script, optimized for TikTok slides"},
                    {"role": "user", "content": script}
                ],
                max_tokens=500
        )
        
        generated_text = response["choices"][0]["message"]["content"]
        slides = split_into_slides(generated_text, max_chars)
        return slides

    def split_into_slides(text, max_chars):
        """
        Splits text into multiple slides based on the character limit.
        :param text: the generated subtitle text.
        :param max_chars: Max characters per slide.
        :return: A list of subtitle slides.
        """

        words = text.split()
        slides, current_slide = [], ""
        
        for word in words:
            if len(current_slide) + len(word) + 1 <= max_chars:
                current_slide += (" " + word) if current_slide else word
            else:
                slides.append(current_slide)
                current_slide = word

            if current_slide:
                slides.append(current_slide)

            return slides

