from urllib import request
from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages    
from django.core.mail import EmailMessage, send_mail
from cancer import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import authenticate, login, logout
from .tokens import generate_token
from django.shortcuts import render, redirect
from scane.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import AnonymousUser, User
from django.views.generic import TemplateView
from .forms import HomeForm, HomeForm2
from .process import *
from .models import *
from django.contrib import messages
import io
import cv2
import numpy
import imutils
import tensorflow as tf
import numpy as np
from keras.applications.vgg16 import  preprocess_input
from PIL import Image
from .forms import NewUserForm
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add thi
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
from keras.layers import Input
from django.contrib import messages
import io
import cv2
import numpy
import imutils
import tensorflow as tf
import numpy as np
from keras.applications.vgg16 import preprocess_input
from PIL import Image

def form(request):
    return render(request,'scane/form.html')

def index(request):
    return render (request,'scane/index.html')
    
def about(request):
    return render (request,'scane/about.html')

def blog(request):
    return render (request,'scane/blog.html')

def contact(request):
    return render (request,'scane/contact.html')

def doctors(request):
    return render (request,'scane/doctors.html')

def blog_details(request):
    return render (request,'scane/blog-details.html')

def about_News1(request):
    return render (request,'scane/about_News1.html')


def processing(request):
    return render (request,'scane/processing.html')

def signup(request):
    return render (request,'scane/signup.html')

def signin(request):
    return render (request,'scane/signin.html')
    
def test(request):
    return render (request,'scane/test.html')

def test2(request):
    return render (request,'scane/test2.html')



def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('scane/signin.html')
###############################################################



class HomeView(TemplateView):

	# Define the template
	template_name = 'scane/form1.html'

	# Handle HTTP GET requests through this view

	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			result = translate(posted)
			form = HomeForm()											

		# Render the page
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
		}
		return render(request, self.template_name, args)

class HomeView2(TemplateView):

	# Define the template
	template_name = 'scane/form2.html'

	# Handle HTTP GET requests through this view

	def get(self, request):

		# Define the view
		form = HomeForm()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)


	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the view
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			result = transcribe(posted)
			form = HomeForm()											

		# Render the page
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
		}
		return render(request, self.template_name, args)


class HomeView3(TemplateView):

	# Define template for this view
	template_name = 'scane/form3.html'

	# Handle HTTP GET requests through this view

 

	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page with the form included
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view
        

	def post(self, request):
        
		# Define the form
		form = HomeForm(request.POST)

		# Validate input
		if form.is_valid():


			# Store cleaned input data
			posted = form.cleaned_data['post']

			# Process data
			result = computeGC(form.cleaned_data['post'])


			# Clear text field
			form = HomeForm()										

		# Render the page with form and result data
    
		args = {'form': form, 'posted': posted, 'result': result}

		return render(request, self.template_name, args)

# Default view for this app
class HomeView4(TemplateView):

	# Define the HTML template
	template_name = 'scane/form4.html'

	# Handle HTTP GET requests through this view

	def get(self, request):
		
		# Define the form
		form = HomeForm2()

		# Render the page
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):

		# Define the form
		form = HomeForm2(request.POST)

		# Validate input
		if form.is_valid():
			posted = form.cleaned_data['post']
			against = form.cleaned_data['against']
			result = parseMotif(posted, against)
			form = HomeForm2()				

		# Render page with results							
		args = {
			'form': form, 
			'posted': posted, 
			'against': against,
			'result': result,
		}
		return render(request, self.template_name, args)



class HomeView5(TemplateView):

	# template for this view
	template_name = 'scane/form5.html'

	# Handle HTTP GET requests through this view
	
	def get(self, request):

		# Define the form
		form = HomeForm()

		# Render the page with form included
		args = {'form': form,}
		return render(request, self.template_name, args)

	# Handle HTTP POST requests through this view

	def post(self, request):
		# Define the form
		form = HomeForm(request.POST)
		# Validate input
		if form.is_valid():
			# Store data from input field
			posted = form.cleaned_data['post']

			# Calculate results
			result = baseDistribution(posted)
			total = sum(result)
			distribution = []
			for i in range(0, len(result)):
				distribution.append((str((round(result[i] / total*100),'%','Base Pairs'             ))))
			# clear text field
			form = HomeForm()
		# Render the page with new args
		args = {
			'form': form, 
			'posted': posted, 
			'result': result,
			'distribution': distribution
		}
		return render(request, self.template_name, args)




def home(request):
    return render(request,'scane/home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'scane/index.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def dna(request):
    inputfile="DNA_sequence_original.txt" 
    f=open(inputfile,"r")
    seq=f.read()
    seq=seq.replace("\n","") 
    seq=seq.replace("\r","")
    print("Numper of Nucludieds in DNA is:",len(seq),"\n")

    print("Numper of Adenine is:",seq.count("A"),"\n")
    print("Numper of Cytosine is:",seq.count("C"),"\n")
    print("Numper of Guanine is:",seq.count("G"),"\n")
    print("Numper of Thymine is:",seq.count("T"),"\n")

    print("#"*50,"\n")


    table = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 #الجدول بتاع تحول الحمض النووي ل برونين
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
            }

    count = {}

    for i in range(0, len(seq)-2, 3):
        codon = seq[i:i+3]
        #print(codon)
        aa = table[codon]
        if aa not in count:
            count[aa] = 0
        count[aa] += 1

    for aa in sorted(count.keys()):
        print("Numper of amino Acide","{}  {}".format(aa, count[aa]),"\n")

    print("#"*50,"\n")
    print("Translated DNA IS:","\n")
    def translate(seq):
    
        table = {
            'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
            'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                 #الجدول بتاع تحول الحمض النووي ل برونين
            'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
            'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
            'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
            'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
            'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
            'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
            'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
            'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
        protein=""
        if len(seq)%3==0:
            for i in range(0,len(seq),3):
                codon=seq[i:i+3]
                protein+=table[codon]
        return protein
    def read_seq(inputfile):
        with open(inputfile,"r") as f:
            seq=f.read()
        seq=seq.replace("\n","")
        seq=seq.replace("\r","")
        return seq
    prt = read_seq("amino_acid_sequence_original.txt")
    dna = read_seq("DNA_sequence_original.txt")

    p=translate(dna[20:935])
    print (p,"\n")
    if(p==prt):
        print ("The analysis was completed successfully \n  ")
    return(request)




###################################ML#################################################


from django.shortcuts import render
from keras.layers import Input
from django.contrib import messages
import io
import cv2
import numpy
import imutils
import tensorflow as tf
import numpy as np
from keras.applications.vgg16 import preprocess_input
from PIL import Image
from tensorflow import *

def convert_img_to_batch_opencv(my_img):
    img = cv2.imread(my_img)
    if img is None:
        print("Error: Image not loaded")
        return None
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # find the extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    # add contour on the image
    img_cnt = cv2.drawContours(img.copy(), [c], -1, (0, 255, 255), 4)
    # add extreme points
    img_pnt = cv2.circle(img_cnt.copy(), extLeft, 8, (0, 0, 255), -1)
    img_pnt = cv2.circle(img_pnt, extRight, 8, (0, 255, 0), -1)
    img_pnt = cv2.circle(img_pnt, extTop, 8, (255, 0, 0), -1)
    img_pnt = cv2.circle(img_pnt, extBot, 8, (255, 255, 0), -1)
    # crop
    ADD_PIXELS = 0
    new_img = img[extTop[1] - ADD_PIXELS:extBot[1] + ADD_PIXELS, extLeft[0] - ADD_PIXELS:extRight[0] + ADD_PIXELS].copy()
    img = cv2.resize(new_img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img = preprocess_input(img)
    img = np.array([img])
    return img

def predict_tumor(img):
    model = tf.keras.models.load_model('scene/models/2019-06-07_VGG_model.h5')
    predictions = model.predict(convert_img_to_batch_opencv(img))
    predictions = [1 if x >0.67 else 0 for x in predictions]
    return predictions[0]

def compare_2_model( res2 , res1):
    CATEGORIES = ["glioma", "meningioma", "no_tumor", "pituitary"]
    if (res2 == 2 and res1==1):
        return 1
    if (res2 == 0 and res1==0):
        return 2
    if (res2 == 1 and res1 == 0):
        return 3
    if (res2 == 2 and res1==0):
         return 0
    if (res2 == 3 and res1 == 0):
        print("pituitary")
        return 4
    else:
         return CATEGORIES[res2]

def Radiology_Diagnostics(request):
    try:
        if request.method == "POST" and request.FILES['myfile']:
            try:
                my_f = request.FILES["myfile"].read()
                image = Image.open(io.BytesIO(my_f))
                opencvImage_model_1 = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
                res1 = predict_tumor(opencvImage_model_1)
                opencvImage_model_2 = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)
                X = cv2.resize(opencvImage_model_2, (150, 150))
                X= x.reshape((150, 150, 1))
                X = X / 255.0
                x = np.array([X])
                mymodel = tf.keras.models.load_model('scene/models/mod2.h5')
                predictions = mymodel.predictclasses(X)
                res2 = predictions[0]
                fin_res = compare_2_model(res2, res1)
                print(fin_res)
                context = { "fin_re": fin_res , "test":"test" }
                return render(request, 'scane/show_res.html' , context)
            except:
                    print("error occurs ya jo")
    except :
            pass
    return render(request, 'scane/Radiology_Diagnostics.html')

def show_res(request):

    return render(request, 'scane/show_res.html')









###################################ML#################################################


#################### index####################################### 
def r1(request):
    return render(request, 'scane/r1.html', {'title':'r1'})
   
########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system #################################### 
            htmly = get_template('scane/Email.html')
            d = { 'username': username }
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            ################################################################## 
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'scane/register.html', {'form': form, 'title':'reqister here'})
   
################ login forms################################################### 
def Login(request):

    if request.method == 'POST':
   
        # AuthenticationForm_can_also_be_used__
   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' wecome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'scane/login.html', {'form':form, 'title':'log in'})

