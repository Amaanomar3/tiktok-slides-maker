from openai import OpenAI
import os



class scriptsGenerator:
    def __init__(self, api_key=None, model="gpt-3.5-turbo", max_chars=100):
        self.model = model
        self.max_chars = max_chars
        self.client = OpenAI(api_key=api_key or os.environ.get("OPENAI_API_KEY"))

    def generate_subtitles(self, script, max_chars=None):
        """
        Generates AI-enhanced subtitles from the provided script and splits them into slides.
        :param script: The input script to generate subtitles from.
        :param max_chars: The max character count per slide. If not provided, the default max_chars will be used.
        :return: A list of slides with subtitles.
        """
        if max_chars is None:
            max_chars = self.max_chars

        response = self.client.chat.completions.create(
            model = self.model,
            messages=[
                {"role": "system", "content" : "Generate engaging subtitles from the given topic/script, optimized for TikTok slides"},
                {"role": "user", "content": script}
            ],
            max_tokens=500
        )
        
        generated_text = response.choices[0].message.content
        slides = self.split_into_slides(generated_text, max_chars)
        return slides

    def split_into_slides(cls, text, max_chars):
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