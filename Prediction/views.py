from django.shortcuts import render
import pickle
from django.conf import settings
from .forms import DataForm

with open(settings.MODEL_PATH, 'rb') as f:
    model = pickle.load(f)

def predict_flower(request):
    prediction = None
    flower_predicted_name = None
    form = DataForm()

    if request.method == "POST":
        # If reset button clicked
        if request.POST.get("reset") == "true":
            # Reinitialize everything
            form = DataForm()  # blank form
            prediction = None
            flower_predicted_name = None
        else:
            form = DataForm(request.POST)
            if form.is_valid():
                data = form.save(commit=False)
                features = [[
                    data.sepalLengthCm,
                    data.sepalWidthCm,
                    data.petalLengthCm,
                    data.petalWidthCm
                ]]
                prediction = model.predict(features)
                flower_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
                flower_predicted_name = flower_names.get(int(prediction[0]), "Unknown")
                data.species = int(prediction[0])
                data.save()
                form = DataForm()  # clear form for fresh entry

    return render(request, 'predict_flower.html', {
        'form': form,
        'prediction': prediction,
        'flower_predicted_name': flower_predicted_name
    })