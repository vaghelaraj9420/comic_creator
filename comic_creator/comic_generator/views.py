from django.shortcuts import render, redirect
from .forms import ComicPanelForm
from .models import ComicPanel
import requests
import base64


API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
API_KEY = "VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM"

def generate_image(text):
    response = requests.post(
        API_URL,
        headers={
            "Accept": "image/png",
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={"inputs": text}
    )
    return response.content

# def create_comic_panel(request):
#     if request.method == 'POST':
#         form = ComicPanelForm(request.POST)
#         if form.is_valid():
#             comic_text = form.cleaned_data['text']
#             image_data = generate_image(comic_text)
#             comic_panel = form.save(commit=False)
#             comic_panel.image_url = image_data
#             comic_panel.save()
#             return redirect('create_comic_panel')
#     else:
#         form = ComicPanelForm()

#     panels = ComicPanel.objects.all()
#     return render(request, 'comic_generator/comic_panel.html', {'form': form, 'panels': panels})

# def create_comic_panel(request):
#     # Handling form submission 
#     user_input_text = "Astronaut riding a horse"  # Replace with actual user input

#     # Making API call to generate image
#     API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
#     headers = {
#         "Accept": "image/png",
#         "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
#         "Content-Type": "application/json",
#     }

#     payload = {"inputs": user_input_text}
#     response = requests.post(API_URL, headers=headers, json=payload)

#     # Converting image to base64-encoded string
#     image_base64 = base64.b64encode(response.content).decode('utf-8')

#     # Passing the base64-encoded string to the template
#     return render(request, 'comic_panel.html', {'image_base64': image_base64})


def create_comic_panel(request):
    if request.method == 'POST':
        form = ComicPanelForm(request.POST)
        if form.is_valid():
            # Process form data
            comic_text = form.cleaned_data['text']

            # Making API call to generate image
            API_URL = "https://xdwvg9no7pefghrn.us-east-1.aws.endpoints.huggingface.cloud"
            headers = {
                "Accept": "image/png",
                "Authorization": "Bearer VknySbLLTUjbxXAXCjyfaFIPwUTCeRXbFSOjwRiCxsxFyhbnGjSFalPKrpvvDAaPVzWEevPljilLVDBiTzfIbWFdxOkYJxnOPoHhkkVGzAknaOulWggusSFewzpqsNWM",
                "Content-Type": "application/json",
            }

            payload = {"inputs": comic_text}
            response = requests.post(API_URL, headers=headers, json=payload)

            # Check if the API call was successful
            if response.status_code == 200:
                # Converting image to base64-encoded string
                image_base64 = base64.b64encode(response.content).decode('utf-8')

                # Save form data along with the image URL
                comic_panel = form.save(commit=False)
                comic_panel.image_url = image_base64  # Save the base64-encoded image
                comic_panel.save()

                return redirect('create_comic_panel')  # Redirect after successful submission
            else:
                # Handle API error, e.g., log or display an error message
                pass
    else:
        form = ComicPanelForm()

    # Fetch existing comic panels
    panels = ComicPanel.objects.all()

    return render(request, 'comic_generator/comic_panel.html', {'form': form, 'panels': panels})