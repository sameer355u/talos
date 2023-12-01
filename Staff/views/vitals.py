from Staff.models.consultation import Vitals,Symptoms,PreExisting,Document,Diagnosis,Prescription
from Patient.models.appointment import Appointment
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
import json

@require_POST
def vitals_modal_insert(request):
    response_data = {'success': False, 'message': 'An error occurred.'}

    if request.method == 'POST':
        try:
            # Accessing the form data from the request
            vitals_id = request.POST.get('vitals_id')
            appointment_id = request.POST.get('appointment_id')
            height = request.POST.get('height')
            weight = request.POST.get('weight')
            systolic = request.POST.get('systolic')
            diastolic = request.POST.get('diastolic')
            temperature = request.POST.get('temperature')
            pulse = request.POST.get('pulse')
            respiratory_rate = request.POST.get('respiratory_rate')
            random_blood_sugar = request.POST.get('random_blood_sugar')
            spo2 = request.POST.get('spo2')
            level_of_consciousness = request.POST.get('level_of_consciousness')
            pupillary_response = request.POST.get('pupillary_response')

            # Try to get the Vitals object for the given appointment_id
            vitals, created = Vitals.objects.get_or_create(
                vitals_id=vitals_id,
                appointment=Appointment.objects.get(appointment_id=appointment_id),
                defaults={
                    'height': height,
                    'weight': weight,
                    'systolic': systolic,
                    'diastolic': diastolic,
                    'temperature': temperature,
                    'pulse': pulse,
                    'respiratory_rate': respiratory_rate,
                    'random_blood_sugar': random_blood_sugar,
                    'spo2': spo2,
                    'level_of_consciousness': level_of_consciousness,
                    'pupillary_response': pupillary_response
                }
            )

            # If the object was not created, it means it already existed, so update it
            if not created:
                vitals.height = height
                vitals.weight = weight
                vitals.systolic = systolic
                vitals.diastolic = diastolic
                vitals.temperature = temperature
                vitals.pulse = pulse
                vitals.respiratory_rate = respiratory_rate
                vitals.random_blood_sugar = random_blood_sugar
                vitals.spo2 = spo2
                vitals.level_of_consciousness = level_of_consciousness
                vitals.pupillary_response = pupillary_response
                vitals.save()

            # Set success message
            response_data['success'] = True
            response_data['message'] = 'Vitals recorded successfully.'
        except Appointment.DoesNotExist:
            response_data['message'] = 'Appointment not found.'
        except Exception as e:
            pass
            # Log the exception for debugging purposes
            #print(f"Error saving vitals: {e}")

    return JsonResponse(response_data)
@require_POST
def symptoms_modal_insert(request):
    response_data = {'success': False, 'message': 'Symptoms recording failed.'}

    if request.method == 'POST':
        symptoms_id = request.POST.get('symptoms_id')
        symptoms_text = request.POST.get('symptoms')
        appointment_id = request.POST.get('appointment_id')
        
        if symptoms_text and appointment_id:
            try:
                # Try to get the Symptoms object for the given symptoms_id and appointment_id
                symptoms, created = Symptoms.objects.get_or_create(
                    symptoms_id=symptoms_id,
                    appointment=Appointment.objects.get(appointment_id=appointment_id),
                    defaults={'symptoms': symptoms_text}
                )

                # If the object was not created, it means it already existed, so update it
                if not created:
                    symptoms.symptoms = symptoms_text
                    symptoms.save()

                response_data['success'] = True
                response_data['message'] = 'Symptoms recorded successfully.'
            except Appointment.DoesNotExist:
                response_data['message'] = 'Appointment not found.'
            except Exception as e:
                pass
                # Log the exception for debugging purposes
                #print(f"Error saving symptoms: {e}")
        else:
            response_data['message'] = 'Symptoms text and appointment ID are required.'

    return JsonResponse(response_data)


@require_POST
def preexisting_modal_insert(request):
    response_data = {'success': False, 'message': 'An error occurred.'}

    if request.method == 'POST':
        try:
            preexisting_id = request.POST.get('preexisting_id')
            appointment_id = request.POST.get('appointment_id')

            # Accessing the form data from the request
            preexisting_info = request.POST.get('preexisting_info')

            # Try to get the PreExisting object for the given preexisting_id and appointment_id
            preexisting, created = PreExisting.objects.get_or_create(
                preexisting_id=preexisting_id,
                appointment=Appointment.objects.get(appointment_id=appointment_id),
                defaults={'preexisting_info': preexisting_info}
            )

            # If the object was not created, it means it already existed, so update it
            if not created:
                preexisting.preexisting_info = preexisting_info
                preexisting.save()

            # Set success message
            response_data['success'] = True
            response_data['message'] = 'Pre-Existing information recorded successfully.'
        except Appointment.DoesNotExist:
            response_data['message'] = 'Appointment not found.'
        except Exception as e:
            pass
            # Log the exception for debugging purposes
            #print(f"Error saving pre-existing information: {e}")

    return JsonResponse(response_data)


@require_POST
def diagnosis_modal_insert(request):
    response_data = {'success': False, 'message': 'An error occurred.'}

    if request.method == 'POST':
        try:
            diagnosis_id = request.POST.get('diagnosis_id')
            appointment_id = request.POST.get('appointment_id')
            clinical_notes = request.POST.get('clinical_notes')
            diagnosis_text = request.POST.get('diagnosis')

            # Try to get the Diagnosis object for the given diagnosis_id and appointment_id
            diagnosis, created = Diagnosis.objects.get_or_create(
                diagnosis_id=diagnosis_id,
                appointment=Appointment.objects.get(appointment_id=appointment_id),
                defaults={'clinical_notes': clinical_notes, 'diagnosis': diagnosis_text}
            )

            # If the object was not created, it means it already existed, so update it
            if not created:
                diagnosis.clinical_notes = clinical_notes
                diagnosis.diagnosis = diagnosis_text
                diagnosis.save()

            response_data['success'] = True
            response_data['message'] = 'Diagnosis information recorded successfully.'
        except Appointment.DoesNotExist:
            response_data['message'] = 'Appointment not found.'
        except Exception as e:
            pass
            # Log the exception for debugging purposes
            #print(f"Error saving diagnosis information: {e}")

    return JsonResponse(response_data)



@require_POST
def upload_documents(request):
    response_data = {'success': False, 'message': 'An error occurred.'}

    if request.method == 'POST':
        try:
            document_id = request.POST.get('document_id')
            appointment_id = request.POST.get('appointment_id')

            document_names = request.POST.getlist('Upload_Document_name')
            document_types = request.POST.getlist('Upload_Doc_Type')
            descriptions = request.POST.getlist('Upload_Description')
            remarks = request.POST.getlist('Upload_Remark')
            document_files = request.FILES.getlist('Upload_File')

            aid = Appointment.objects.get(appointment_id=appointment_id)

            fss = FileSystemStorage()
            #print(len(document_files))
            for i in range(len(document_names)):
                file = fss.save(document_files[i].name, document_files[i])
                document, created = Document.objects.get_or_create(
                    document_id=document_id,
                    appointment=aid,
                    defaults={
                        'document_name': document_names[i],
                        'document_type': document_types[i],
                        'description': descriptions[i],
                        'remark': remarks[i],
                        'document_file': file
                    }
                )

                # If the object was not created, it means it already existed, so update it
                if not created:
                    document.document_name = document_names[i]
                    document.document_type = document_types[i]
                    document.description = descriptions[i]
                    document.remark = remarks[i]
                    document.document_file = file
                    document.save()

            response_data['success'] = True
            response_data['message'] = 'Documents recorded successfully.'
        except Appointment.DoesNotExist:
            response_data['message'] = 'Appointment not found.'
        except Exception as e:
            pass
            # Log the exception for debugging purposes
            #print(f"Error saving documents: {e}")

    return JsonResponse(response_data)

@require_POST
def save_prescription(request):
    response_data = {'success': False, 'message': 'An error occurred.'}

    if request.method == 'POST':
        try:
            appointment_id = request.POST.get('appointment_id')
            lab_investigation = request.POST.get('lab_investigation')
            advice = request.POST.get('advice')
            follow_up_date = request.POST.get('follow_up_date')
            remark = request.POST.get('remark')

            medicine_list = request.POST.getlist('medicine')
            strength_list = request.POST.getlist('strength')
            dose_list = request.POST.getlist('dose')
            frequency_list = request.POST.getlist('frequency')
            duration_list = request.POST.getlist('duration')
            instruction_list = request.POST.getlist('instruction')

            # Assuming all lists have the same length
            data_list = []

            for i in range(len(medicine_list)):
                data_dict = {
                    'medicine': medicine_list[i],
                    'strength': strength_list[i],
                    'dose': dose_list[i],
                    'frequency': frequency_list[i],
                    'duration': duration_list[i],
                    'instruction': instruction_list[i],
                }
                data_list.append(data_dict)

            # Now 'data_list' is a list of dictionaries containing the data from the POST request
            rxdata_json = json.dumps(data_list)

            # Try to get the Prescription object for the given appointment_id
            prescription, created = Prescription.objects.get_or_create(
                appointment=Appointment.objects.get(appointment_id=appointment_id),
                defaults={'advice': advice, 'lab_investigation': lab_investigation,
                          'follow_up_date': follow_up_date, 'remark': remark, 'rx_data': rxdata_json}
            )

            # If the object was not created, it means it already existed, so update it
            if not created:
                prescription.advice = advice
                prescription.lab_investigation = lab_investigation
                prescription.follow_up_date = follow_up_date
                prescription.remark = remark
                prescription.rx_data = rxdata_json
                prescription.save()

            response_data['success'] = True
            response_data['message'] = 'Prescription saved successfully.'
        except Appointment.DoesNotExist:
            response_data['message'] = 'Appointment not found.'
        except Exception as e:
            pass
            # Log the exception for debugging purposes
            #print(f"Error saving prescription: {e}")

    return JsonResponse(response_data)


def get_vitals(request):
    if request.method == 'GET':
        appointment_id = request.GET.get('appointment_id')
        # tab_id = request.GET.get('tab_id')

        # Fetch data for the given appointment_id and tab_id
        # Replace this with your actual data fetching logic
        data = {
            'height': 'value1',
            'weight': '123',
            # Add more fields as needed
        }

        return JsonResponse(data)