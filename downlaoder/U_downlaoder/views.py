from django.shortcuts import render, redirect
import yt_dlp
import re
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        url = request.POST.get('link')
        
        # Set a temporary message to indicate downloading
        messages.info(request, 'Downloading...')

        try:
            # Define yt-dlp options
            ydl_opts = {
                'format': 'best',  # Download the best quality available
                'outtmpl': '%(title)s-%(upload_date)s.%(ext)s',  # Output template
            }

            # Create a context for yt-dlp and download the video
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)  # Download the video
                title = info_dict.get('title', 'No Title')
                filename = re.sub(r'[\\/*?:"<>|]', "", title) + ".mp4"  # Ensure a valid filename

                messages.success(request, f'Download complete: {filename}')
        
        except yt_dlp.utils.DownloadError as e:
            messages.error(request, f'Error: {str(e)}')

        return redirect('home')

    return render(request, "home.html")
