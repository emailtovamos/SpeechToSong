import speech_recognition as sr
import time

# obtain audio from the microphone
r = sr.Recognizer()
while(1):

    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        # print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
        from googleapiclient.discovery import build
        import pprint

        my_api_key = "YOUR_API_KEY"
        my_cse_id = "CSE_ID"

        def google_search(search_term, api_key, cse_id, **kwargs):
            service = build("customsearch", "v1", developerKey=api_key)
            res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
            return res['items']

        results = google_search(
            r.recognize_google(audio)+' site:youtube.com', my_api_key, my_cse_id, num=1)
        print(results[0]['link'])

        import pafy
        import os
        url=results[0]['link']
        video = pafy.new(url)
        video.duration, video.likes, video.dislikes
        best = video.getbest()
        best = video.getbest(preftype="mp4")
        if int(video.duration[3:5]) < 5:
             filename=best.download(quiet=False)
             full=video.title+".mp4"
             os.popen(full)
        time.sleep(2)

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
