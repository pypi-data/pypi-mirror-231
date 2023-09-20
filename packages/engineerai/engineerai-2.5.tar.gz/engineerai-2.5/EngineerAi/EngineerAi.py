import os
from typing import List
import requests
import openai
import gtts
import pyaudio
import numpy as np
import wave
import cv2
import textwrap

from pydub import AudioSegment
from pydub.generators import Sine
import speech_recognition as sr

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

char_to_freq = {
    'a': 440.00, 'b': 493.88, 'c': 523.25, 'd': 587.33, 'e': 659.26,
    'f': 698.46, 'g': 783.99, 'h': 880.00, 'i': 987.77, 'j': 1046.50,
    'k': 1174.66, 'l': 1318.51, 'm': 1396.91, 'n': 1567.98, 'o': 1760.00,
    'p': 1975.53, 'q': 2093.00, 'r': 2349.32, 's': 2637.02, 't': 2793.83,
    'u': 3135.96, 'v': 3520.00, 'w': 3951.07, 'x': 4186.01, 'y': 4698.63,
    'z': 5274.04,

    'أ': 440.00, 'ب': 493.88, 'ت': 523.25, 'ث': 587.33, 'ج': 659.26,
    'ح': 698.46, 'خ': 783.99, 'د': 880.00, 'ه': 987.77, 'و': 1046.50,
    'ز': 1174.66, 'ح': 1318.51, 'ط': 1396.91, 'ي': 1567.98, 'ك': 1760.00,
    'ل': 1975.53, 'م': 2093.00, 'ن': 2349.32, 'س': 2637.02, 'ع': 2793.83,
    'غ': 3135.96, 'ف': 3520.00, 'ق': 3951.07, 'ر': 4186.01, 'ش': 4698.63,

    'а': 440.00, 'б': 493.88, 'в': 523.25, 'г': 587.33, 'д': 659.26,
    'е': 698.46, 'ё': 783.99, 'ж': 880.00, 'з': 987.77, 'и': 1046.50,
    'й': 1174.66, 'к': 1318.51, 'л': 1396.91, 'м': 1567.98, 'н': 1760.00,
    'о': 1975.53, 'п': 2093.00, 'р': 2349.32, 'с': 2637.02, 'т': 2793.83,
    'у': 3135.96, 'ф': 3520.00, 'х': 3951.07, 'ц': 4186.01, 'ч': 4698.63,
}

class EngineerAi:
    def __init__(self) -> None:
        super().__init__()

    def text_to_frequencies(
            self,
            text: str
    ) -> list:
        """
        Args:
            text (str):  query

        Returns:
            list: list of frequencies
        """
        word = text.lower()
        sound_frequencies = []

        for c in word:
            frequency = char_to_freq.get(c, 0)
            sound_frequencies.append(frequency)
        return sound_frequencies

    def generate_sound(
            self,
            frequencies: List["float"],
            duration_ms: int,
            output_file: str
        ) -> None:
        """generate sound from frequencies

        Args:
            frequencies (List[&quot;float&quot;]): List of frequencies
            duration_ms (int): Duration
            output_file (str): output path
        """
        song = AudioSegment.silent(duration=0)
        for frequency in frequencies:
            sine_wave = Sine(frequency)
            note = sine_wave.to_audio_segment(duration=duration_ms)
            song += note
        song.export(output_file, format="wav")

    def text_to_sound(
            self,
            text: str,
            duration_ms: int,
            output_file: str
        ) -> None:
        """Text to sound 

        Args:
            text (str): query
            duration_ms (int): duration
            output_file (str): output path
        """
        freqs = self.text_to_frequencies(text)
        self.generate_sound(freqs, duration_ms, output_file)

    def frequencies_to_text(
            self,
            frequencies: List["float"]
        ) -> str:
        """frequencies to text

        Args:
            frequencies (List[&quot;float&quot;]): List of frequencies

        Returns:
            str: text
        """
        text = ""
        for freq in frequencies:
            if freq == 0:
                text += ' '
            else:
                closest_char = None
                closest_diff = float('inf')

                for char, char_freq in char_to_freq.items():
                    diff = abs(char_freq - freq)
                    if diff < closest_diff:
                        closest_diff = diff
                        closest_char = char

                text += closest_char

        return text

    def transcribe_audio(
            self,
            lang: str,
            audio_file: str
        ) -> str:
        """Audio to text using google service

        Args:
            lang (str): ISO 639-1 Language code ( ar-SA , en-US , etc ... )
            audio_file (str): audio path

        Returns:
            str: text
        """
        r = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language=lang)
            return text

    def chatai(
            self,
            key: str,
            question: str
        ) -> str:
        """Ask CHAT GPT

        Args:
            key (str): Open AI Key
            question (str): The question

        Returns:
            str: The answer
        """
        openai.api_key = key
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=question
        )

        answer = response.choices[0].text.strip()
        return answer

    def text_to_speech(
            self,
            text: str,
            lang: str,
            filename: str
        ) -> bool:
        """Text to speech using google service

        Args:
            text (str): Text to speech query
            lang (str): ISO 639-2 language code ( en, ar, etc.. )
            filename (str): Output path

        """
        gtts.gTTS(text=text, lang=lang, slow=False).save(filename)
        return True
    
    def photo_modern_to_old(
            self,
            filename: str,
            output_file: str
		) -> bool:
            """Convert a modern photo to old photo
				
				Args:
					filename (str): Input path
					output_file (str): Input path
					
			"""
            image = cv2.imread(filename)
            new_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            cv2.imwrite(output_file,new_image)
            return True
    
    def write_on_image(
        self,
        filename: str,
        output_file: str,
        text: str,
        position: str,
        text_color: tuple,
        font_name: str,
        font_size: int,
        max_line_length: int
    ) -> bool:
        """Write text on image

        Args:
            filename (str): Image path
            output_file (str): Output path
            text (str): Text
            position (str): Choice ('center', 'top', 'bottom', 'right', 'left')
            text_color (tuple): Text color
            font_name (str): Font name
            font_size (int): Font size
            max_line_length (int): Max line length
        """
        image = Image.open(filename)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_name, font_size)

        text_lines = textwrap.wrap(text, max_line_length)
        text_height = draw.textsize(text_lines[0], font=font)[1]
        image_width, image_height = image.size

        if position == "top":
            text_x = (image_width - draw.textsize(text_lines[0], font=font)[0]) // 2
            text_y = text_height + 10
        elif position == "left":
            text_x = 10
            text_y = (image_height + text_height) // 2
        elif position == "right":
            text_x = image_width - draw.textsize(text_lines[0], font=font)[0] - 10
            text_y = (image_height + text_height) // 2
        elif position == "bottom":
            text_x = (image_width - draw.textsize(text_lines[0], font=font)[0]) // 2
            text_y = image_height - 10
        elif position == "center":
            text_x = (image_width - draw.textsize(text_lines[0], font=font)[0]) // 2
            text_y = (image_height + text_height) // 2
        else:
            text_x = 10
            text_y = (image_height + text_height) // 2

        for line in text_lines:
            if text_y + text_height <= image_height:
                draw.text((text_x, text_y), line, fill=text_color, font=font)
            else:
                break
            text_y += text_height + 5

        image.save(output_file)

        return True
    
    def convert_image_format(
            self,
            filename: str,
            output_file: str,
            output_format: str
    ) -> bool:
        """Convert Image Format from (eg... jpg) to (eg... png)

        Args:
            filename (str): Image path
            output_file (str): Output path
            output_format (str): Output format
        """
        image = Image.open(filename)
        image.save(output_file, output_format)

        return True
    
    def enhance_image_quality(
            self,
            filename: str,
            output_file: str
    ) -> bool:
        """Enhance image quality

        Args:
            filename (str): Image path
            output_file (str): Output path
            output_format (str): Output format
        """
        image = Image.open(filename)
        enhanced_image = cv2.detailEnhance(image)
        cv2.imwrite(output_file, enhanced_image)

        return True
    
    