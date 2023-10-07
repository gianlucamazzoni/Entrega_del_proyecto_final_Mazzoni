from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django. contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Nintendo, Playstation, Xbox, Avatar
from .forms import NintendoFormulario, PlaystationFormulario, XboxFormulario, UserEditForm, AvatarFormulario
# Create your views here.

def Lista(req, Desarrolladora, Fecha_de_inauguración, Juego, Fecha_de_salida):

    Lista = Nintendo(Desarrolladora=Desarrolladora, Fecha_de_inauguración=Fecha_de_inauguración, Juego=Juego, Fecha_de_salida=Fecha_de_salida)
    Lista.save()

    Lista = Playstation(Desarrolladora=Desarrolladora, Fecha_de_inauguración=Fecha_de_inauguración, Juego=Juego, Fecha_de_salida=Fecha_de_salida)
    Lista.save()

    Lista = Xbox(Desarrolladora=Desarrolladora, Fecha_de_inauguración=Fecha_de_inauguración, Juego=Juego, Fecha_de_salida=Fecha_de_salida)
    Lista.save()






def Lista_DFJF_nintendo(req):
    
    Listar = Nintendo.objects.all()

    return render(req, "Lista_DFJF_nintendo.html", {"Listar_DFJF_nintendo": Listar})

def Lista_DFJF_playstation(req):
    
    Listar = Playstation.objects.all()

    return render(req, "Lista_DFJF_playstation.html", {"Listar_DFJF_playstation": Listar})

def Lista_DFJF_xbox(req):
    
    Listar = Xbox.objects.all()

    return render(req, "Lista_DFJF_xbox.html", {"Listar_DFJF_xbox": Listar})







def Inicio(req):

    try:
        avatar = Avatar.objects.get(user=req.user.id)
        return render(req, 'Inicio.html', {"url_avatar": avatar.imagen.url})
    except:
        return render(req, 'Inicio.html')

def nintendo(req):
    return render(req, 'Nintendo.html')

def playstation(req):
    return render(req, 'Playstation.html')

def xbox(req):
    return render(req, 'Xbox.html')


def Links(req):
    return render(req, 'Links.html')


def nintendoFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = NintendoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Lista = Nintendo(Desarrolladora=data["Desarrolladora"], Fecha_de_inauguración=data["Fecha de inauguración"], Juego=req.POST["Juego"], Fecha_de_salida=req.POST["Fecha de salida"])
            Lista.save()
            return render(req,"Inicio.html")
    else:
        miFormulario = NintendoFormulario()
        return render(req,"NintendoFormulario.html", {"miFormulario":miFormulario})

def playstationFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = PlaystationFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Lista = Playstation(Desarrolladora=data["Desarrolladora"], Fecha_de_inauguración=data["Fecha de inauguración"], Juego=req.POST["Juego"], Fecha_de_salida=req.POST["Fecha de salida"])
            Lista.save()

            return render(req,"Inicio.html")
    else:
        miFormulario = PlaystationFormulario()
        return render(req,"PlaystationFormulario.html", {"miFormulario":miFormulario})

def xboxFormulario(req):
    print('method', req.method)
    print('POST', req.POST)
    if req.method == 'POST':
        miFormulario = XboxFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Lista = Xbox(Desarrolladora=data["Desarrolladora"], Fecha_de_inauguración=data["Fecha de inauguración"], Juego=req.POST["Juego"], Fecha_de_salida=req.POST["Fecha de salida"])
            Lista.save()
            return render(req,"Inicio.html")
    else:
        miFormulario = XboxFormulario()
        return render(req,"XboxFormulario.html", {"miFormulario": miFormulario})
    

def BuscarDesarrolladorasNin(req):
     return render(req, "BusquedaDesarrolladorasNintendo.html")
def BuscarNin(req: HttpRequest):   
    if req.GET['Desarrolladora']: 
        Desarrolladora = req.GET['Desarrolladora']
        Lista = Nintendo.objects.filter(Desarrolladora=Desarrolladora)
        return render(req, "ResultadoBusquedaNintendo.html", {"Lista": Lista})
    else:
        return HttpResponse(f"Debe agregar una Desarrolladora")
    

def BuscarDesarrolladorasPlay(req):
     return render(req, "BusquedaDesarrolladorasPlaystation.html")
def BuscarPlay(req: HttpRequest):   
    if req.GET['Desarrolladora']: 
        Desarrolladora = req.GET['Desarrolladora']
        Lista = Playstation.objects.filter(Desarrolladora=Desarrolladora)
        return render(req, "ResultadoBusquedaPlaystation.html", {"Lista": Lista})
    else:
        return HttpResponse(f"Debe agregar una Desarrolladora")


def BuscarDesarrolladorasXbox(req):
     return render(req, "BusquedaDesarrolladorasXbox.html")
def BuscarXbox(req: HttpRequest):   
    if req.GET['Desarrolladora']: 
        Desarrolladora = req.GET['Desarrolladora']
        Lista = Xbox.objects.filter(Desarrolladora=Desarrolladora)
        return render(req, "ResultadoBusquedaXbox.html", {"Lista": Lista})
    else:
        return HttpResponse(f"Debe agregar una Desarrolladora")
    

@staff_member_required(login_url='/PaginaWeb/Login/')
def ListaXbox(req):

    Juego = Xbox.objects.all()

    return render(req, "ListaXbox.html", {"Juego": Juego})

@staff_member_required(login_url='/PaginaWeb/Login/')
def ListaPlaystation(req):

    Juego = Playstation.objects.all()

    return render(req, "ListaPlaystation.html", {"Juego": Juego})

@staff_member_required(login_url='/PaginaWeb/Login/')
def ListaNintendo(req):

    Juego = Nintendo.objects.all()

    return render(req, "ListaNintendo.html", {"Juego": Juego})





def eliminarJuegoNin(req, id):

    if req.method == 'POST':

        nintendo = Nintendo.objects.get(id=id)
        nintendo.delete()

        Juego = Nintendo.objects.all()

        return render(req, "ListaNintendo.html", {"Juego": Juego})


def eliminarJuegoPlay(req, id):

    if req.method == 'POST':

        playstation = Playstation.objects.get(id=id)
        playstation.delete()

        Juego = Playstation.objects.all()
        return render(req, "ListaPlaystation.html", {"Juego": Juego})
    

def eliminarJuegoXbox(req, id):

    if req.method == 'POST':

        xbox = Xbox.objects.get(id=id)
        xbox.delete()
        Juego = Xbox.objects.all()
        return render(req, "ListaXbox.html", {"Juego": Juego})
    

def EditarJuegoXbox(req, id):
    
    Lista = Xbox.objects.get(id=id)

    if req.method == 'POST':    
        miFormulario = XboxFormulario(req.POST)      
        if miFormulario.is_valid():       
            data = miFormulario.cleaned_data
            Lista.Desarrolladora = data["Desarrolladora"]
            Lista.Fecha_de_inauguración = data["Fecha de inauguración"]
            Lista.Juego = data["Juego"]
            Lista.Fecha_de_salida = data["Fecha de salida"]
            Lista.save()


            return render(req,"Inicio.html")
    else:
        miFormulario = XboxFormulario(initial={
            "Desarrolladora": Lista.Desarrolladora,
            "Fecha de inauguración": Lista.Fecha_de_inauguración,
            "Juego": Lista.Juego,
            "Desarrolladora": Lista.Desarrolladora,
        })
        return render(req,"EditarXbox.html", {"miFormulario": miFormulario, "id":Lista.id})
    


def EditarJuegoPlay(req, id):
    
    Lista = Playstation.objects.get(id=id)

    if req.method == 'POST':   
        miFormulario = PlaystationFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Lista.Desarrolladora = data["Desarrolladora"]
            Lista.Fecha_de_inauguración = data["Fecha de inauguración"]
            Lista.Juego = data["Juego"]
            Lista.Fecha_de_salida = data["Fecha de salida"]
            Lista.save()

            return render(req,"Inicio.html")
    else:
        miFormulario = PlaystationFormulario(initial={
            "Desarrolladora": Lista.Desarrolladora,
            "Fecha de inauguración": Lista.Fecha_de_inauguración,
            "Juego": Lista.Juego,
            "Desarrolladora": Lista.Desarrolladora,
        })
        return render(req,"EditarPlay.html", {"miFormulario": miFormulario, "id":Lista.id})
    

def EditarJuegoNin(req, id):
    
    Lista = Nintendo.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = NintendoFormulario(req.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            Lista.Desarrolladora = data["Desarrolladora"]
            Lista.Fecha_de_inauguración = data["Fecha de inauguración"]
            Lista.Juego = data["Juego"]
            Lista.Fecha_de_salida = data["Fecha de salida"]
            Lista.save()

            return render(req,"Inicio.html")
    else:
        miFormulario = NintendoFormulario(initial={
            "Desarrolladora": Lista.Desarrolladora,
            "Fecha de inauguración": Lista.Fecha_de_inauguración,
            "Juego": Lista.Juego,
            "Desarrolladora": Lista.Desarrolladora,
        })
        return render(req,"EditarNin.html", {"miFormulario": miFormulario, "id":Lista.id})
    



class NintendoList(LoginRequiredMixin, ListView):
    model = Nintendo
    template_name = "Nintendo_List.html"
    context_object_name = "Lista"


class NintendoDetail(DetailView):
    model = Nintendo
    template_name = "Nintendo_Detail.html"
    context_object_name = "Lista"


class NintendoCreate(CreateView):
    model = Nintendo
    template_name = "Nintendo_create.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/'


class NintendoUpdate(UpdateView):
    model = Nintendo
    template_name = "Nintendo_update.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/Lista-nintendo/'
    context_object_name = "Lista"


class NintendoDelete(DeleteView):
    model = Nintendo
    template_name = "Nintendo_delete.html"
    success_url = '/PaginaWeb/Lista-nintendo/'
    context_object_name = "Lista"

class PlaystationList(LoginRequiredMixin, ListView):
    model = Playstation
    template_name = "Playstation_List.html"
    context_object_name = "Lista"


class PlaystationDetail(DetailView):
    model = Playstation
    template_name = "Playstation_Detail.html"
    context_object_name = "Lista"


class PlaystationCreate(CreateView):
    model = Playstation
    template_name = "Playstation_create.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/'


class PlaystationUpdate(UpdateView):
    model = Playstation
    template_name = "Playstation_update.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/Lista-playstation/'
    context_object_name = "Lista"


class PlaystationDelete(DeleteView):
    model = Playstation
    template_name = "Playstation_delete.html"
    success_url = '/PaginaWeb/Lista-playstation/'
    context_object_name = "Lista"

class XboxList(LoginRequiredMixin, ListView):
    model = Xbox
    template_name = "Xbox_List.html"
    context_object_name = "Lista"


class XboxDetail(DetailView):
    model = Xbox
    template_name = "Xbox_Detail.html"
    context_object_name = "Lista"


class XboxCreate(CreateView):
    model = Xbox
    template_name = "Xbox_create.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/'
    

class XboxUpdate(UpdateView):
    model = Xbox
    template_name = "Xbox_update.html"
    fields = ['Desarrolladora', 'Fecha_de_inauguración', 'Juego', 'Fecha_de_salida']
    success_url = '/PaginaWeb/Lista-xbox/'
    context_object_name = "Lista"


class XboxDelete(DeleteView):
    model = Xbox
    template_name = "Xbox_delete.html"
    success_url = '/PaginaWeb/Lista-xbox/'
    context_object_name = "Lista"



def Login(req):

    if req.method == 'POST':
        
        miFormulario = AuthenticationForm(req, data=req.POST)
        
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario = data["username"]
            psd = data["password"]

            user = authenticate(username = usuario, password = psd )

            if user:
                login(req, user)
                return render(req,"Inicio.html", {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(req,"Inicio.html", {"mensaje": f"Datos incorrectos"})
    else:
        miFormulario = AuthenticationForm()
        return render(req,"Login.html", {"miFormulario": miFormulario})
    


def register(req):

    if req.method == 'POST':
        
        miFormulario = UserCreationForm(req.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            usuario = data["username"]
            miFormulario.save()
            return render(req,"Inicio.html", {"mensaje": f"El usuario {usuario} fue creado con exito!!"})         
        
        return render(req,"Inicio.html", {"mensaje": f"Formulario invalido"})
    
    else:
        miFormulario = UserCreationForm()
        return render(req,"Registro.html", {"miFormulario": miFormulario})
    

def EditarPerfil(req):
  
    usuario = req.user
    if req.method == 'POST':
        
        miFormulario = UserEditForm(req.POST, instance=req.user)
        
        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]
            usuario.email = data["email"]
            usuario.set_password(data["password1"])
            usuario.save()

            return render(req, "Inicio.html", {"mensaje": "Datos actualizados con exito!"})
        else:
            return render(req, "EditarPerfil.html", {"miFormulario": miFormulario})
    
    else:
    
        miFormulario = UserEditForm(instance=usuario)
        return render(req,"EditarPerfil.html", {"miFormulario": miFormulario})
    

def Agregar_avatar(req):
    
    if req.method == 'POST':
        
        miFormulario = AvatarFormulario(req.POST, req.FILES)
        
        if miFormulario.is_valid():
        
            data = miFormulario.cleaned_data
            
            avatar = Avatar(user=req.user, imagen=data["imagen"])           
            
            avatar.save()

            return render(req, "Inicio.html", {"mensaje": "Avatar actualizado exitosamente!"})
        
    else:
    
        miFormulario = AvatarFormulario()
        return render(req,"Agregar_avatar.html", {"miFormulario": miFormulario})