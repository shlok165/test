from django.shortcuts import render, HttpResponse
import firebase_admin
from firebase_admin import credentials, db
from home.firebase_handler.firebase_operations import write_data, read_data
from home.firebase_handler.firebase_operations import listen_for_changes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ServiceRequest
from django.views.decorators.csrf import csrf_exempt
import logging
from .models import ServiceRequest
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.shortcuts import render

# Initialize Firebase Admin if not already initialized
if not firebase_admin._apps:
    cred = credentials.Certificate('/home/slok/water_quality_analysis/hello/home/aquaintigrity-firebase-adminsdk-qg2xs-c7638bb689.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://aquaintigrity-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })



def index(request):
    # Fetch data from the 'test' node in the Firebase Realtime Database
    ref = db.reference('/test')  # Specify the 'test' node
    firebase_data = ref.get()  # Fetch all data under the 'test' node

    # Handle cases where firebase_data is None or missing keys
    temperature = firebase_data.get('temperature', 'No data available') if firebase_data else 'No data available'
    turbidity = firebase_data.get('turbidity', 'No data available') if firebase_data else 'No data available'
    TDS = firebase_data.get('TDS', 'No data available') if firebase_data else 'No data available'
    pH = firebase_data.get('pH', 'No data available') if firebase_data else 'No data available'


    context = {
        'temperature': temperature,
        'turbidity': turbidity,
        'TDS' : TDS,
        'pH' : pH,
    }

    return render(request, 'index.html', context)

def GraphChartView(request):
    return render(request, 'chart.html')

def read_example(request):
    # This view is called by the fetch API
    ref = db.reference('/test')  # Specify the 'test' node
    firebase_data = ref.get()

    # Handle cases where firebase_data is None or keys are missing
    temperature = firebase_data.get('temperature', 'No data available') if firebase_data else 'No data available'
    turbidity = firebase_data.get('turbidity', 'No data available') if firebase_data else 'No data available'
    TDS = firebase_data.get('TDS', 'No data available') if firebase_data else 'No data available'
    pH = firebase_data.get('pH', 'No data available') if firebase_data else 'No data available'
    
    # Return the data as a JSON response
    return JsonResponse({
        'temperature': temperature,
        'turbidity': turbidity,
        'TDS' : TDS,
        'pH' : pH,
    })


def about(request):
    return render(request, 'aboutUs.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contactUs.html')

def write_example(request):
    data = {
        "temperature": 20,
        "turbidity": 55,
        "pH": 65,
        "TDS": 20,
    }
    write_data(data)
    return HttpResponse("Data written successfully.")

def listen_to_data(request):
    listen_for_changes()
    return HttpResponse("Listening to Firebase data updates.")


logger = logging.getLogger(__name__)




@csrf_exempt
def submit_service_request(request):
    if request.method == 'POST':
        try:
            # Debug print
            print("POST data received:", request.POST)
            
            # Extract data with default values
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            phone = request.POST.get('phone', '')
            preferred_contact = request.POST.get('preferred-contact', 'email')
            service_type = request.POST.get('service-type', '')
            urgency = request.POST.get('urgency', 'normal')
            message = request.POST.get('message', '')
            
            # Debug print
            print(f"Extracted data: name={name}, email={email}, service_type={service_type}")
            
            # Create and save
            service_request = ServiceRequest(
                name=name,
                email=email,
                phone=phone,
                preferred_contact=preferred_contact,
                service_type=service_type,
                urgency=urgency,
                message=message
            )
            
            if 'attachments' in request.FILES:
                service_request.attachment = request.FILES['attachments']
            
            # Save and debug print
            service_request.save()
            print(f"Service request saved with ID: {service_request.id}")
            
            return JsonResponse({
                'status': 'success',
                'message': 'Service request saved successfully',
                'id': service_request.id
            })
            
        except Exception as e:
            print(f"Error saving service request: {str(e)}")
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method'
    }, status=400)
