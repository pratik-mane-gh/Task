from gtts import gTTS

text = """
Welcome to this web development demo session.
In this session, we will cover the following topics:
Learn HTML
Understand the structure of web pages.
Create headings, paragraphs, tables, forms, and links.
Learn CSS
Style web pages with colors, fonts, and layouts.
Create responsive designs for mobile and desktop devices.
Learn JavaScript
Add interactivity to websites.
Create dynamic content, validations, and animations.
Work with Bootstrap
Use ready-made components and templates.
Build responsive websites faster and more efficiently.
Build Real-World Projects
Develop practical websites and web applications.
Apply concepts learned during the course.
"""

tts = gTTS(text=text, lang="en")
tts.save("web_development_demo.mp3")

print("Audio saved as web_development_demo.mp3")