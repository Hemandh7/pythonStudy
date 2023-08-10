from django.shortcuts import render, redirect

data_dict = {
    "name": "Ram",
    "age": 20,
    "city": "Delhi"
}

def create_view(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        value = request.POST.get('value')
        data_dict[key] = value
        return redirect('/read')
    return render(request, 'create.html')

def read_view(request):
    return render(request, 'read.html', {'data_dict': data_dict})


def update_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        new_value = request.POST['value']
        data_dict[key] = new_value
    return render(request, 'update.html', {'data_dict': data_dict})

def delete_view(request):
    if request.method == 'POST':
        key = request.POST['key']
        if key in data_dict:
            del data_dict[key]
    return render(request, 'delete.html', {'data_dict': data_dict})
