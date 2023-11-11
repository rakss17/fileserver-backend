from django.shortcuts import render, redirect, get_object_or_404
from .forms import FileUploadForm
from .models import UploadedFile


def file_list(request):
    files = UploadedFile.objects.all().order_by('-uploaded_at')

    if request.method == 'POST':
            form = FileUploadForm(request.POST, request.FILES)
            if form.is_valid():
                
                uploaded_file = form.save(commit=False)
                uploaded_file.original_filename = form.cleaned_data['file'].name
                uploaded_file.file_size = form.cleaned_data['file'].size
                uploaded_file.save()
                return redirect('file_list')
    else:
        form = FileUploadForm()
    return render(request, 'file/file_list.html', {'form': form, 'files': files})


def delete_file(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    file.delete()
    return redirect('file_list')