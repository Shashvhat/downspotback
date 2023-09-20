from flask import Flask, request, render_template, redirect, url_for,jsonify
from pytube import YouTube,Search

app = Flask(__name__)

# @app.route('/getVidInfo', methods=['GET', 'POST'])

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'POST':
    # video_url = request.form['video_url']
    try:
        # Create a YouTube object
        data = request.args.get('data')
        yt = YouTube('https://www.youtube.com/watch?v=cFee50gHcIM&pp=ygURc3lzdGVtIHBlciBzeXN0ZW0%3D')
        s = Search(data)
        # print(s.results)
        
        for i in s.results:
            print(i.title)

        # Select the highest resolution stream
        # stream = yt.streams.get_highest_resolution()
        
        # Download the video
        stream = yt.streams.get_by_itag(313)
        # stream.download()
        # stream.audio_codec
        
        return jsonify('Downloaded successfully.')
    except Exception as e:
        return redirect(url_for('index', message=f'Error: {str(e)}'))

    return 'Downloaded successfully.'

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
