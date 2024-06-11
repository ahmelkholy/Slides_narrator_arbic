import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Arabic text to be converted to speech
text = """
ومن هنا وجب على المصمم أن يضع نصوصا مؤقتة على التصميم ليظهر للعميل الشكل كاملاً، دور مولد النص العربى أن يوفر على المصمم عناء البحث عن نص بديل لا علاقة له بالموضوع الذى يتحدث عنه التصميم فيظهر بشكل لا يليق.
هذا النص يمكن أن يتم تركيبه على أي تصميم دون مشكلة فلن يبدو وكأنه نص منسوخ، غير منظم، غير منسق، أو حتى غير مفهوم. لأنه مازال نصاً بديلاً ومؤقتاً.
"""

# Set properties before adding anything to speak
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Set the voice to Arabic
voices = engine.getProperty('voices')

for voice in voices:
    if 'arabic' in voice.languages:
        engine.setProperty('voice', voice.id)
        break

# Save the speech to a file
output_path = "arabic_text.mp3"
engine.save_to_file(text, output_path)

# Run the speech engine
engine.runAndWait()

output_path
