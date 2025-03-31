"""This is the main python script"""
from scripts import scriptsGenerator
import os


def main():
    # Get API key from environment variable
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set in the environment variables")
    
    gen = scriptsGenerator(api_key=api_key)
    sample_script = "TikTok is one of the fastest-growing platforms. Here's how you can use it effectively!"
    slides = gen.generate_subtitles(sample_script)

    for i, slide in enumerate(slides, 1):
        print(f"Slide {i}: {slide}")

if __name__ == "__main__":
    main()
