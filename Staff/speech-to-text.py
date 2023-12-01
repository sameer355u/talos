# import io
# import speech_to_text
#
# # Create a speech client
# client = speech_to_text.SpeechClient()
#
# # Load the audio file
# with io.open("audio.wav", "rb") as f:
#     audio_data = f.read()
#
# # Set the audio configuration
# config = speech_to_text.RecognitionConfig()
# config.language_code = "en-US"
#
# # Create a recognition request
# request = speech_to_text.RecognitionRequest(audio=audio_data, config=config)
#
# # Transcribe the audio file
# response = client.recognize(request=request)
#
# # Get the transcript
# transcript = response.results[0].alternatives[0].transcript
#
# # Print the transcript
# print(transcript)
#
#
#
# # from flask import Flask, render_template, request, jsonify
# # import io
# # from google.cloud import speech
# # import pyaudio
# #
# # app = Flask(__name__)
# #
# # client = speech.SpeechClient.from_service_account_file('alien-craft-377409-8b9f944e0028.json')
# #
# # FORMAT = pyaudio.paInt16
# # CHANNELS = 1
# # RATE = 16000
# # CHUNK = 1024
# # RECORD_SECONDS = 10
# # # Adjust the recording duration as needed
# # isRecording = False
# # mediaStream = None
# #
# #
# # @app.route('/transcribe', methods=['GET', 'POST'])
# # def transcribe_audio():
# #     if request.method == 'GET':
# #         return render_template('Patient_Registration_Updated.html', transcribed_text=None)
# #     else:
# #         audio_data = io.BytesIO()
# #         audio = pyaudio.PyAudio()
# #         stream = audio.open(format=FORMAT, channels=CHANNELS,
# #                             rate=RATE, input=True,
# #                             frames_per_buffer=CHUNK)
# #
# #         print("Recording...")
# #         frames = []
# #
# #         for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
# #             data = stream.read(CHUNK)
# #             frames.append(data)
# #
# #         print("Finished recording")
# #
# #         stream.stop_stream()
# #         stream.close()
# #         audio.terminate()
# #
# #         audio_data = b''.join(frames)
# #
# #         audio_config = speech.RecognitionConfig(
# #             encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
# #             sample_rate_hertz=RATE,
# #             language_code="en-US",
# #         )
# #         print('config')
# #         response = client.recognize(config=audio_config, audio=speech.RecognitionAudio(content=audio_data))
# #
# #         if response.results:
# #             print('in response')
# #             transcribed_text = response.results[0].alternatives[0].transcript
# #             print(transcribed_text)
# #             jsonify({"transcription": transcribed_text})
# #             return render_template('Patient_Registration_Updated.html', transcribed_text=transcribed_text)
# #
# #         else:
# #             return jsonify({"error": "No transcription result found"}), 400
