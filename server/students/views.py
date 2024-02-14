from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializers
from django.http.response import JsonResponse
from .models import Student
from django.http.response import Http404
from rest_framework.response import Response
from sklearn.model_selection import train_test_split
from keras_preprocessing.image import ImageDataGenerator
import os
import joblib
import numpy as np
import pandas as pd
import librosa
import librosa.display
import glob as gb
import matplotlib
import gc
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# Create your views here.
model=joblib.load(os.path.join('./students/prediction.sav'))
class StudentView(APIView):

    def post(self,request):
        Student.objects.all().delete()
        directory = 'media/uploads'
        files = os.listdir(directory)
        for file_name in files:
            file_path = os.path.join(directory, file_name)
            os.remove(file_path)
        images_dir = 'images/'
        im = os.listdir(images_dir)
        for i_n in im:
            file_path = os.path.join(images_dir,i_n)
            os.remove(file_path)
  
        data = request.data
        serializer = StudentSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Student Created Successfully",safe=False)
        return JsonResponse("Failed to Add Student")
    

    def get(self,request):
        data = Student.objects.filter(Id=0)
        #print(data)
        sound_records=np.array(gb.glob("media/uploads/*.wav"))
        print(sound_records[0])
        
        index=0
        file_name = ""
        for file in sound_records[index:]:
            sfile_name = file.split('\\')[1].split('.')[0]
            file_name =sfile_name+'.jpg'
            print('Index:',sfile_name)
            plt.interactive(False)
            file_audio_series,sr = librosa.load(file,sr=None)
            image = plt.figure(figsize=[0.72,0.72])
            ax = image.add_subplot(111)
            ax.axes.get_xaxis().set_visible(False)
            ax.axes.get_yaxis().set_visible(False)
            ax.set_frame_on(False)
            spectogram = librosa.feature.melspectrogram(y=file_audio_series, sr=sr)
            librosa.display.specshow(librosa.power_to_db(spectogram, ref=np.max))
            image_name  = 'images/' + sfile_name + '.jpg'
            plt.savefig(image_name, dpi=400, bbox_inches='tight',pad_inches=0)
            plt.close() 
            image.clf()
            plt.close(image)
            plt.close('all')
            del file,sfile_name,file_audio_series,sr,image,ax,spectogram
        
        #model=joblib.load(os.path.join('./students/prediction.sav'))
        
        folder_path = 'C:/Users/LENOVO/OneDrive/Desktop/react-django/server/images'
        data_alls = pd.DataFrame(
            {
                'ID':[],
                'CLASS':[]
            }
        )
        data_alls.columns=['ID','CLASS']
        data_alls.loc[len(data_alls)] = [file_name, "none"]
        print(data_alls)
        print(data_alls["ID"].values[0])
        test_datas = ImageDataGenerator(rescale=1./255)

        generator =  test_datas.flow_from_dataframe(
            dataframe=data_alls,
            directory=folder_path,
            x_col="ID",
            y_col=None,
            batch_size=32,
            seed=42,
            shuffle=False,
            class_mode=None,
            target_size=(64,64)

        )
        print("the length is ",len(generator))

            #preprocessed_img = next(generator)
            #predictions = model.predict(preprocessed_img) 
        predictions = model.predict_generator(generator,steps=len(generator),verbose=1)
        pclass = np.argmax(predictions,axis=1)
        disease=""
        if(pclass[0]==0):
            disease="Asthma"
        elif(pclass[0]==1):
            disease="Bronchiectasis"
        elif(pclass[0]==2):
            disease="Bronchiectasis"
        elif(pclass[0]==3):
            disease="COPD"
        elif(pclass[0]==4):
            disease="Healthy"
        elif(pclass[0]==5):
            disease="Pneumonia"
        elif(pclass[0]==6):
            disease="URTI"
        
        


        


        answer = [{'id':0,'result':disease} for item in data]




        
        #data.save(update_fields=['Text'])
        #data.save()
        #serializer = StudentSerializers(data,many=True)
        #return Response(serializer.data)
        return JsonResponse(answer,safe=False)


'''''
    def get_student(self,pk):
        try:
            student = Student.objects.get(studentId=pk)
            return student
        except Student.DoesNotExist():
            raise Http404
    
    def get(self,request,pk=None):
        if pk :
            data = self.get_student(pk)
            serializer = StudentSerializers(data)
        else:
            data = Student.objects.all()
            
            serializer = StudentSerializers(data,many=True)
            #Student.objects.all().delete()
        return Response(serializer.data)
'''''


