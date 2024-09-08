from kivy.app import App 
from kivy.uix.widget import Widget
from kivy.uix.tabbedpanel import TabbedPanel
import sys
from kivy.core.window import Window
import firebase_admin
from firebase_admin import credentials, firestore

#Firebase setup
cred = credentials.Certificate("authfile/sak.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#Done


class MyLayout(TabbedPanel):
    def __init__(self,**kwargs):
        super(MyLayout, self).__init__(**kwargs)


    def search_fxn(self):
        
        city_from = self.ids._from.text.lower()
        city_to = self.ids._to.text.lower()

        print(f"{city_from} - {city_to}")


        doc_ref = db.collection(city_from).document(city_to)
        doc = doc_ref.get()

        if doc.exists:
            f = doc.to_dict()

            print(f)

            li = []
            for k,v in f.items():
                li.append(v)

            value = "BUS: "+(li[0].upper())+"    PRICE:"+str(li[1])
            self.ids._data.text = value

        else:
            print("Sorry,No data found!")



class BusApp(App):
    def build(self):
        return MyLayout()
    
if __name__=="__main__":
    BusApp().run()
    
