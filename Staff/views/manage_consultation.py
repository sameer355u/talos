from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from CustomAuth.utility import get_user_menu
from Patient.views.manage_patient import calculate_age
from Staff.models.consultation import Vitals, Symptoms, PreExisting, Document, Diagnosis, Prescription
from Patient.models.appointment import Appointment
import json


@login_required(login_url="/accounts/login/")
def doctor_cons_list(request):
    doc_con_list = Appointment.objects.all()
    data = get_user_menu(request)
    return render(request, 'doctor_con.html', {'doc_con_list': doc_con_list, 'data': data})


@login_required(login_url="/accounts/login/")
def doctor_consultation(request, appointment_id):
    try:
        # Retrieve the appointment details or raise a 404 if not found
        appointment_detail = get_object_or_404(Appointment, AppointmentIDPK=appointment_id)
        print("appointment_detail", appointment_detail)

        try:
            vitals = Vitals.objects.get(appointment_id=appointment_id)
        except Vitals.DoesNotExist:
            vitals = None  # Set a default value or handle as needed

        try:
            # Assuming you have a ForeignKey relationship between Document and Appointment
            documents = Document.objects.filter(appointment_id=appointment_id)
        except Document.DoesNotExist:
            documents = None  # Set a default value or handle as needed

        try:
            # Assuming you have a ForeignKey relationship between Document and Appointment
            preexistings = PreExisting.objects.get(appointment_id=appointment_id)
        except PreExisting.DoesNotExist:
            preexistings = None  # Set a default value or handle as needed

        try:
            # Assuming you have a ForeignKey relationship between Document and Appointment
            diagnosis = Diagnosis.objects.get(appointment_id=appointment_id)
        except Diagnosis.DoesNotExist:
            diagnosis = None  # Set a default value or handle as needed

        try:
            symptoms = Symptoms.objects.get(appointment_id=appointment_id)
        except Symptoms.DoesNotExist:
            symptoms = None  # Set a default value or handle as needed

        try:
            prescription = Prescription.objects.get(appointment_id=appointment_id)
        except Prescription.DoesNotExist:
            prescription = None  # Set a default value or handle as needed

        # Assuming you have a serializer for your Appointment model
        # Adjust the serializer class based on your actual model structure

        # Calculate age based on date of birth and appointment date
        dob = appointment_detail.PatientIDFK.DOB
<<<<<<< HEAD
        age = calculate_age(dob)
=======
        age = calculate_age(dob, appointment_detail.Date)
>>>>>>> 8bd2625677363acd3021b60a4b29a30efde36d78

        serializer_data = {
            'patient_name': appointment_detail.PatientIDFK.FirstName+' '+ appointment_detail.PatientIDFK.LastName,
            'contact_number': request.user.phone,
            'gender': appointment_detail.PatientIDFK.Gender,
            'age': age,
            'appointment_date': appointment_detail.Date,
            'patient_image': appointment_detail.PatientIDFK.PatientProfileImage,
            'dob': dob,
            'patient_id': appointment_detail.PatientIDFK.PatientID,
            'appointment_id': appointment_id,
            'appointment_by': appointment_detail.CreatedBy,
            # 'appointment_type': appointment_detail.professional_Type  # Adjust this based on your model
        }
        # print(preexistings.preexisting_id)
        rx_data_list = []
        if prescription:
            rx_data_list = json.loads(prescription.rx_data)
            #print(prescription.rx_data)
        context = {'appointments': Appointment.objects.all(), 'appointment_detail': serializer_data, 'vitals': vitals,
                   'documents': documents, 'symptoms': symptoms, 'preexistings': preexistings, 'diagnosis': diagnosis,
                   'prescription': prescription, 'rx_data_list': rx_data_list}
        return render(request, 'doctor_consultation.html', context)

    except Appointment.DoesNotExist:
        context = {'appointments': Appointment.objects.all(), 'error_message': 'Appointment not found'}
        return render(request, 'doctor_consultation.html', context)

    except Exception as e:
        # Handle other exceptions (e.g., database errors) here
        #print(e)
        context = {'appointments': Appointment.objects.all(), 'error_message': f'Error: {str(e)}'}
        return render(request, 'doctor_consultation.html', context)
