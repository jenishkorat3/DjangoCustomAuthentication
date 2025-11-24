from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import logout
from core.decorators import login_and_role_required


@login_and_role_required("customer")
def customer_dashboard(request):
    return render(request, 'customer/dashboard.html')


@login_and_role_required("customer")
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            messages.success(
                request, "Password changed successfully. Please login with new password.")
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'customer/change_password.html', {'form': form})
