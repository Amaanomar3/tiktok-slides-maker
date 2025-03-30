"""This is the main python script"""
import scripts

def main():
    sample_script = "TikTok is one of the fastest-growing platforms. Here's how you can use it effectively!"
    slides = scripts.generate_subtitles(sample_script)

    for i, slide in enumerate(slides, 1):
        print(f"Slide {i}: {slide}")
    

if __name__ == "__main__":
    main()
