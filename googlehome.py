from google.cloud import texttospeech
from google.cloud import speech_v1
from google.cloud.speech_v1 import enums
from google.cloud.speech_v1 import types
import soundfile as sf
import sounddevice as sd
from scipy.io.wavfile import write
import os
import io
import subprocess
import time
import random
import datetime




def question():
    client = texttospeech.TextToSpeechClient.from_service_account_json('vision-project-207707-f84d39ceed76.json')


    ourText = "What do you want"
    synthesis_input = texttospeech.SynthesisInput(text=ourText)

    languageCode = 'en-US'

    gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(language_code=languageCode, ssml_gender=gender)

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("audio content written to output file")
    os.system("output.mp3")

def STT():
    client = speech_v1.SpeechClient.from_service_account_json('vision-project-207707-f84d39ceed76.json')



    sampleRate = 44100
    recDuration = 5
    totaLSamples = int(sampleRate * recDuration)

    print('Start Recording')

    myRecording = sd.rec(totaLSamples, sampleRate, 1)
    sd.wait()
    print('Done Recording')

    write('voiceRecording.wav', sampleRate, myRecording)
    data, recSampleRate = sf.read('voiceRecording.wav')
    sf.write('voiceRecording.FLAC', data, sampleRate)

    encoding = enums.RecognitionConfig.AudioEncoding.FLAC
    languageCode = 'en-US'
    config = {'encoding': encoding, 'sample_rate_hertz': sampleRate, 'language_code': languageCode}

    path = 'voiceRecording.FLAC'

    with io.open(path, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)
        response = client.recognize(config, audio)


    for result in response.results:
        response_user = (result.alternatives[0].transcript)
    return response_user


def todays_date_question():
    client = texttospeech.TextToSpeechClient.from_service_account_json('vision-project-207707-f84d39ceed76.json')

    x = datetime.datetime.now()
    todays_date = "Todays date is " + str(x.strftime("%A")) + str(x.strftime("%B")) + "," + str(x.year)
    ourText = todays_date
    synthesis_input = texttospeech.SynthesisInput(text=ourText)

    languageCode = 'en-US'

    gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(language_code=languageCode, ssml_gender=gender)

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("audio content written to output file")
    os.system("output.mp3")


def Calculation(a,b,sign):
    client = texttospeech.TextToSpeechClient.from_service_account_json('vision-project-207707-f84d39ceed76.json')

    if sign == "+":
        sum = a + b
        ourText = str(sum)
    elif sign == "*":
        sum1 = a*b
        ourText = str(sum1)
    elif sign == "-" :
        sum2 = a-b
        ourText = str(sum2)
    elif sign == "/":
        sum3 = a/b
        ourText = str(sum3)





    synthesis_input = texttospeech.SynthesisInput(text=ourText)

    languageCode = 'en-US'

    gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(language_code=languageCode, ssml_gender=gender)

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("audio content written to output file")
    os.system("output.mp3")



def TTS():
    client = texttospeech.TextToSpeechClient.from_service_account_json('vision-project-207707-f84d39ceed76.json')

    x = random.randint(1, 2)

    if x == 1:
        ourText = 'heads'

    if x == 2:
        ourText = 'tails'

    synthesis_input = texttospeech.SynthesisInput(text=ourText)

    languageCode = 'en-GB'

    gender = texttospeech.SsmlVoiceGender.NEUTRAL

    voice = texttospeech.VoiceSelectionParams(language_code=languageCode, ssml_gender=gender)

    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)
        print("audio content written to output file")
    os.system("output.mp3")


def music():

    os.system("5Am.mp3")








while True:
    question()
    time.sleep(4)
    questions123 = STT()
    if "flip a coin" in questions123:
        TTS()
        time.sleep(4)

    if "today" in questions123 and "date" in questions123:
        todays_date_question()
        time.sleep(4)
    if "+" in questions123:
        numbers = questions123.split(" ")
        Calculation(int(numbers[0]), int(numbers[2]),"+")
        time.sleep(4 )
    if "*" in questions123:
        numbers = questions123.split(" ")
        Calculation(int(numbers[0]), int(numbers[2]),"*")
        time.sleep(4)
    if "-" in questions123:
        numbers = questions123.split(" ")
        Calculation(int(numbers[0]), int(numbers[2]),"-")
        time.sleep(4)

    if "/" in questions123:
        numbers = questions123.split(" ")
        Calculation(int(numbers[0]), int(numbers[2]),"/")
        time.sleep(4)

    if "play a song"  in questions123:
        music()
        time.sleep(10)


    if "stop" in questions123:
        break
