from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from apps.account.models import CustomUser
from apps.account.forms import CustomUserCreationForm
from django.contrib import messages

@login_required
def account(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('account-admin')
    else:
        return redirect('account-customer')

@login_required
def account_admin(request):
    if not request.user.is_superuser and not request.user.is_staff:
        return HttpResponseForbidden("Acceso denegado")

    clientes = CustomUser.objects.filter(is_staff=False, is_superuser=False)
    context = {
        'usuarios': clientes
    }

    return render(request, 'account-admin.html', context)

@login_required
def account_customer(request):
    if request.user.is_superuser or request.user.is_staff:
        return HttpResponseForbidden("Acceso denegado")
    return render(request, 'account-customer.html')

@login_required  
def buscar(request,pk):
    if pk!='':
        clientes=CustomUser.objects.get(rut=pk)
        context={'usuarios':clientes}
        if clientes:
            return render(request, 'modify-customer.html', context)

        else:
            context={'mensaje','Error - Usuario no encontrado'}
            return render(request,'account-admin.html',context)

@login_required  

@login_required
def editar_usuario(request):
    if request.method == "POST":
        rut = request.POST.get("rut")
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        
        try:
            usuario = CustomUser.objects.get(rut=rut)
            usuario.nombre = nombre
            usuario.email = email
            usuario.save()
            messages.success(request, "Usuario modificado correctamente.")
        except CustomUser.DoesNotExist:
            messages.error(request, "Error - Usuario no encontrado.")
        except Exception as e:
            messages.error(request, f"Error - No se pudo modificar el usuario: {str(e)}")
    else:
        messages.error(request, "Error - Método de solicitud no permitido. Por favor, usa el método POST.")

    return redirect('account-admin')




@login_required    
def delete(request,pk):
    context={}
    try:
        cliente=CustomUser.objects.get(rut=pk)
        cliente.delete()
        mensaje='Cliente Eliminado Exitosamente'
        clientes=CustomUser.objects.all()
        context={'usuarios':clientes,'mensaje':mensaje}
        return render(request,'account-admin.html',context)
    except:
        mensaje='Rut de Cliente no Existe'    
        clientes=CustomUser.objects.all()
        context={'usuarios':clientes,'mensaje':mensaje}
        return render(request,'account-admin.html',context) 
